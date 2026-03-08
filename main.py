var  myForm = document.getElementById("myForm");
var myInput = document.gretElementById("myInput");
var myItem = document.gerElementById("myItem");

myForm.addEventListener("submit", function(event){
    event.preventDefult();
    createItem(myInput.value)
})

function createItem(inputItems){
    var items = <li>${inputItems}
    <button onclick="deldteElement(this)">Delete</button> </li>
    myItem.insertAdjacentHTML("beforeend", items)
    myInput.value = ""
    myInput.focus()
}

function deleteElement(ElementToDelete){
    ElementToDelete.parentElement.remove()
}