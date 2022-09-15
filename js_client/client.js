const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndPoint = 'http://localhost:8000/api'
if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

if (searchForm) {
    // handle this search form
    searchForm.addEventListener('submit', handleSearch)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault()
    const loginEndPoint = `${baseEndPoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyStr)
    const options = {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: bodyStr
    }
    fetch(loginEndPoint, options)
        .then(response => {
            return response.json()
        })
        .then(authData => {
            handleAuthData(authData, getProductList)
        })
        .catch(err => {
            console.log('error', err)
        })
}

function handleSearch(event) {
    console.log(event)
    event.preventDefault()
    let searchFormData = new FormData(searchForm)
    let searchObjectData = Object.fromEntries(searchFormData)
    let searchParams = new URLSearchParams(searchObjectData)
    const searchEndPoint = `${baseEndPoint}/search/?${searchParams}`
    console.log(searchObjectData)
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access')
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: 'GET',
        headers: headers
    }
    fetch(searchEndPoint, options)
        .then(response => {
            return response.json()
        })
        .then(data => {
            const validData = !isTokenNotValid(data)
            if (validData && contentContainer) {
                contentContainer.innerHTML = ''
                if (data && data.hits && data.hits.length !== 0) {
                    let htmlStr = ''
                    for (let result of data.hits) {
                        htmlStr += '<li>' + result.title + '</li>'
                    }
                    contentContainer.innerHTML = htmlStr
                } else {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            }
            //writeToContainer(data)
        })
        .catch(err => {
            console.log('error', err)
        })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = '<pre>' + JSON.stringify(data, null, 4) + '</pre>'
    }
}

function isTokenNotValid(jsonData) {
    if (jsonData && jsonData.code === 'token_not_valid') {
        // Refresh token
        alert("Please login again")
        return true
    }
    return false
}

function getFetchOptions(method = 'GET', body = null) {
    return {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        },
        body: body
    }
}

function validateJWTToken() {
    // fetch
    const endpoint = `${baseEndPoint}/token/verify/`
    let body = {
        token: localStorage.getItem('access')
    }
    let bodyStr = JSON.stringify(body)
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: bodyStr
    }
    fetch(endpoint, options)
        .then(response => response.json())
        .then(verifyToken => {
            console.log(verifyToken)
            return isTokenNotValid(verifyToken) === false
        })
}

function getProductList() {
    const endpoint = `${baseEndPoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint, options)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const validData = !isTokenNotValid(data)
            if (validData) {
                writeToContainer(data)
            }
        })
}

const searchClient = algoliasearch('BAHZRR5VS3', 'cd1ea116f239bec0821e9ff426498ebc');
const search = instantsearch({
    indexName: 'cfe_Product',
    searchClient,
});
search.addWidgets([
    instantsearch.widgets.searchBox({
        container: '#searchbox',
    }),
    instantsearch.widgets.clearRefinements({
        container: "#clear-refinements"
    }),
    instantsearch.widgets.refinementList({
        container: "#user-list",
        attribute: 'user'
    }),
    instantsearch.widgets.refinementList({
        container: "#public-list",
        attribute: 'public'
    }),
    instantsearch.widgets.hits({
        container: '#hits',
        templates: {
            item: `
              <div>
                  <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
                  <div>{{#helpers.highlight}}{ "attribute": "content" }{{/helpers.highlight}}</div>
                  <p>{{ user }}</p><p>\${{ price }}
              </div>`
        }
    })
]);

search.start();