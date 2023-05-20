// Create functional button for opening the "add invoice" menu
const newInvoiceBtn = document.querySelector(".new-invoice");
const newInvoiceScreen = document.querySelector(".new-invoice-menu-container");
const darkener = document.querySelector(".darkener");
const closeNewInvoiceMenu = document.querySelector(".exit-new-invoice");

newInvoiceBtn.addEventListener("click", () => {
  darkener.classList.toggle("darkened");
  newInvoiceScreen.style.top = "10%";
});

closeNewInvoiceMenu.addEventListener("click", () => {
  darkener.classList.remove("darkened");
  newInvoiceScreen.style.top = "-90%";
});

// Generate new inputfields in add-service-section when button "add a service" is clicked
const addServiceBtn = document.querySelector(".add-service-btn");
const servicesContainer = document.querySelector(".new-invoice-services");

let counter = 2;

addServiceBtn.addEventListener("click", () => {
  let newInputfield = document.createElement("div");
  newInputfield.classList.add("inputfield-row");
  newInputfield.innerHTML = `
    <input
      type="text"
      class="new-invoice-service-name"
      name="service-name-${counter}"
      autocomplete="off"
      placeholder="Service name"
      required />
    <input
      type="number"
      class="new-invoice-hours"
      name="hours-${counter}"
      step=".01"
      placeholder="Hours"
      required />
    <input
      type="number"
      class="new-invoice-wage"
      name="wage-${counter}"
      step=".01"
      placeholder="Wage"
      required />
    <button class="service-input new-invoice-delete-service">
      <i class="fa-regular fa-trash-can"></i>
    </button>
  `;

  servicesContainer.append(newInputfield);

  counter++;
});

// When a client is selected, render that client's data in "client-info-container"
const clientInfoContainer = document.querySelector(".client-info-container");
const clientSelectInput = document.querySelector("select.client-info-input");
