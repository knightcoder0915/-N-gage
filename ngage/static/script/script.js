form = document.querySelector('form')

form.addEventListener('submit', function(e) {
    e.preventDefault();
    inpValue = e.target.querySelector('input').value
    fetchData4mAPI(inpValue)
})

async function fetchData4mAPI(inpVal) {
    app_id = '0760fb86';
    app_key = '193c59ce9250c820b56298a67b4e4b05';
    baseURl = `https://api.edamam.com/search?q=${inpVal}&app_id=${app_id}&app_key=${app_key}&to=4`;
    result = await fetch(baseURl);
    datas = await result.json()
    console.log(datas)
    genrateHTML(datas.hits);
}

function genrateHTML(results) {
    showINHTML = '';
    results.map(result => {
        showINHTML += `
         
    
    <div class="card">
    
    <div class="image">
       <img src="${result.recipe.image}">
    </div>
    <div class="title">
     <h1>
     ${result.recipe.label}</h1>
    </div>
    <div class="des">
     <p>Calories: ${result.recipe.calories.toFixed(2)}</p>
     <a href='${result.recipe.url}'><button>View Recipe</button></a>

    </div>
    </div>
        
        `
        document.querySelector('#showRecipe').innerHTML = showINHTML;

    })
}