const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector('.table-output');
const PaginationContainer = document.querySelector('.pagination-container');
const appTable = document.querySelector('.app-table');
tableOutput.style.display = 'none';


searchField.addEventListener('keyup', (e)=>{
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0){
        PaginationContainer.style.display = 'none';
        console.log('SearchValue', searchValue);

        fetch("/search-expenses", {
      body: JSON.stringify({ searchText : searchValue }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);

        tableOutput.style.display = 'block';
        appTable.style.display = 'none';

        if (data.length===0){
            tableOutput.innerHTML = 'No Results Found!';
        }
      });
        else{
            tableOutput.style.display = 'none';
            appTable.style.display = 'block';
            PaginationContainer.style.display = 'block';
        }
    }
})