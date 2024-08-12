const createMemoButton = document.getElementById("create-memo-button");
const customModal = document.getElementById("customModal");
const closeModalButton = customModal.querySelector(".fa-window-close");



createMemoButton.addEventListener("click", function(){
    customModal.classList.remove("hidden")
});

closeModalButton.addEventListener("click", function(){
    customModal.classList.add("hidden")
})


