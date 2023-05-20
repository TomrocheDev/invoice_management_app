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
const servicesContainer = document.querySelector(
  ".add-services-input-container"
);

let counter = 1;

addServiceBtn.addEventListener("click", () => {
  let newInputfield = document.createElement("div");
  newInputfield.classList.add("inputfield-row");
  newInputfield.innerHTML = `
              <div class="inputfield-col service-name">
                <label for="service-name">Service name:</label>
                <input
                  type="text"
                  class="service-input input-large"
                  name="service-name-${counter}"
                  id="service-name"
                  autocomplete="off" />
              </div>
              <div class="inputfield-col service-hours">
                <label for="service-hours">Hours:</label>
                <input
                  type="number"
                  class="service-input"
                  name="hours-${counter}"
                  id="hours" 
                  step=".01"/>
              </div>
              <div class="inputfield-col service-wage">
                <label for="wage">Wage per hour:</label>
                <input
                  type="number"
                  class="service-input"
                  name="wage-${counter}"
                  id="wage" 
                  step=".01" />
              </div>
  `;

  servicesContainer.append(newInputfield);

  counter++;
});

// When a client is selected, render that client's data in "client-info-container"
const clientInfoContainer = document.querySelector(".client-info-container");
const clientSelectInput = document.querySelector("select.client-info-input");
