//import a select from select.js and create a new custom select
import Select from './select.js';

const selectElements = document.querySelectorAll('[data-custom]');

selectElements.forEach((selectElement) => {
	new Select(selectElement);
});
