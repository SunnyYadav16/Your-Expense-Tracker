const searchinput = document.querySelector("#searchinput");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
const tbody = document.querySelector(".table-body")
tableOutput.style.display = "none";


searchinput.addEventListener('keyup', (e)=>{
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0){

        tbody.innerHTML = "";
        // console.log('SearchValue', searchValue);

        fetch("search-expenses", {
      body: JSON.stringify({ searchText : searchValue }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);

        tableOutput.style.display = "block";
        appTable.style.display = "none";

        if (data.length===0){
            tableOutput.innerHTML = 'No Results Found!';
        }
        else{
            data.forEach(item=>{
                tbody.innerHTML += `
            
            <tr>
                <td>${item.amount}</td>
                <td>${item.category}</td>
                <td>${item.description}</td>
                <td>${item.date}</td>
            </tr>`;
            })

        }
      });
    }
        else{
            tableOutput.style.display = 'none';
            appTable.style.display = 'block';
        }
});