let url = 'https://jsonplaceholder.typicode.com/users/';
const randomUserApi = 'https://randomuser.me/api/';

fetch(url)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))

const mostrarData = (data) => {
    console.log(data)
    let body = ""
    for (var i = 0; i < data.length; i++) {
        let fotoUrl = `${randomUserApi}?inc=picture&gender=${data[i].gender}`;
        body += `<tr><td>${data[i].id}</td><td>${data[i].name}</td><td>${data[i].email}</td><td><img src="${fotoUrl}" /></td></tr>`
    }
    document.getElementById('data').innerHTML = body
}