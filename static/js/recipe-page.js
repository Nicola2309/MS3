/*This code is inspired by my fellow student Ian M from his project "Larder" https://github.com/iainm342/milestone-3/blob/main/static/js/recipe.js */
$(document).ready(function () {
	var max_ingr = 30;
	var wrapper_ingr = $(".ingredient-row");
	var add_ingr_button = $(".add-ingr-buttn");

	// Function appending a a new line of ingredients as a div
	// to a an upper row
	var ingr = 1;
	$(add_ingr_button).click(function (e) {
		e.preventDefault();
		if (ingr < max_ingr) {
			ingr++;
			$(wrapper_ingr).append('<div class="input-field col s12 ingr-input"><input id="ingredients" type="text" name="ingredients"/><label for="ingredients"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
		}
	});

	// Function to eliminate the appended lines
	$(wrapper_ingr).on("click", ".remove_field", function (e) {
		e.preventDefault();
		$(this).parent('div').remove();
		ingr--;
	});

	// This function helps the user append a text area to 
	// the preparation row, to add extra recipe steps
	var max_steps = 30;
	var wrapper_step = $(".prep-row");
	var add_step_buttn = $(".add-step-buttn");

	var step = 1;
	$(add_step_buttn).click(function (e) {
		e.preventDefault();
		if (step < max_steps) {
			step++;
			$(wrapper_step).append('<div class="input-field col s12 step-input"><textarea id="preparation" type="text" name="preparation"/></textarea><label for="preparation"></label><a href="#" class="remove_field"><i class="far fa-trash-alt"></i></a></div>');
		}
	});


	// Function that helps the user remove the preparation text area
	$(wrapper_step).on("click", ".remove_field", function (e) {
		e.preventDefault();
		$(this).parent('div').remove();
		step--;
	});


	// This function allows the user to delete recipe steps 
	// from the edit_recipe page
	var edit_prep = $(".edit-prep-row");
	var add_edit_step_buttn = $(".add_edit_step_buttn");
	$(edit_prep).on("click", ".remove_field", function (e) {
		e.preventDefault();
		$(this).parent('div').remove();
		step--;
	});

	// This function allows the user to add extra rows in the edit_recipe page
	// if the number is inferior to the max_steps
	var edit_prep_step = 1
	$(add_edit_step_buttn).click(function (e) {
		e.preventDefault();
		if (edit_prep_step < max_steps) {
			edit_prep_step++;
			$(edit_prep).append('<div class="input-field col s12 step-input"><textarea id="preparation" type="text" name="preparation"/></textarea><label for="preparation"></label><a href="#" class="remove_field"><i class="far fa-trash-alt"></i></a></div>');
		}
	});

	// This function allows the user to remove a line to the ingredients Array
	// from the edit_recipe page
	var edit_ingr = $(".edit-ingr-row");
	var add_edit_ingr_buttn = $(".add-edit-ingr-buttn");
	$(edit_ingr).on("click", ".remove_field", function (e) {
		e.preventDefault();
		$(this).parent('div').remove();
		step--;
	});

	// This function let the user add extra ingredient lines in 
	// the edit_recipe page
	var edit_ingr_step = 1;
	$(add_edit_ingr_buttn).click(function (e) {
		e.preventDefault();
		if (edit_ingr_step < max_ingr) {
			edit_ingr_step++;
			$(edit_ingr).append('<div class="input-field col s12 ingr-input"><input id="ingredients" type="text" name="ingredients"/><label for="ingredients"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
		}
	});
});