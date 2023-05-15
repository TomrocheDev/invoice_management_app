// Create functional button for opening the "add invoice" menu
const newInvoiceBtn = document.querySelector(".new-invoice");
const newInvoiceScreen = document.querySelector(".new-invoice-menu-container");
const darkener = document.querySelector(".darkener");
const closeNewInvoiceMenu = document.querySelector(".fa-circle-xmark");

newInvoiceBtn.addEventListener("click", () => {
  darkener.classList.toggle("darkened");
  newInvoiceScreen.style.top = "10%";
});

closeNewInvoiceMenu.addEventListener("click", () => {
  darkener.classList.remove("darkened");
  newInvoiceScreen.style.top = "-80%";
});
