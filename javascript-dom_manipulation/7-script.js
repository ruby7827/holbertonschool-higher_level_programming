const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');

fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  });
