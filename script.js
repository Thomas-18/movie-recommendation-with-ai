async function recommend() {

    const genre =
        document.getElementById("genre").value;

    const mood =
        document.getElementById("mood").value;

    if(!genre || !mood){
        alert("Please enter genre and mood");
        return;
    }

    const loading =
        document.getElementById("loading");

    const result =
        document.getElementById("result");

    loading.classList.remove("hidden");
    result.innerHTML = "";

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/recommend",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    genre,
                    mood
                })
            }
        );

        const data = await response.json();

        loading.classList.add("hidden");

        result.innerHTML = `
            <div class="movie-card">
                <h3>AI Recommendations</h3>
                <p>${data.recommendations.replace(/\n/g,"<br>")}</p>
            </div>
        `;

    }
    catch(error){

        loading.classList.add("hidden");

        result.innerHTML = `
            <div class="movie-card">
                <h3>Error</h3>
                <p>Could not fetch recommendations.</p>
            </div>
        `;
    }
}