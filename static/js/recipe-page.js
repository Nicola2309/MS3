/*This code is inspired by my fellow student Ian M from his project "Larder" https://github.com/iainm342/milestone-3/blob/main/static/js/recipe.js */
$(document).ready(function() {
	var max_ingr         = 30;
    var wrapper_ingr     = $(".ingr-input");
	var add_ingr_button  = $(".add-ingr-buttn");
	
	var ingr = 1;
	 $(add_ingr_button).click(function(e){
	 	e.preventDefault();
	 	if(ingr < max_ingr) { 
	 		ingr++; 
	 		$(wrapper_ingr).append('<div class="col s12 input-field" style="float: none;width: 78%;padding-left: 6%;"><input id="add_ingredients" type="text" name="add_ingredients" required/><label for="add_ingredients"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
	 	}
     });

	
	$(wrapper_ingr).on("click",".remove_field", function(e){ 
		e.preventDefault(); $(this).parent('div').remove(); ingr--;
	});

	var max_steps      = 30; 
	var wrapper_step   = $(".step-input"); 
	var add_step_buttn = $(".add-step-buttn");
	
	var step = 1; 
	$(add_step_buttn).click(function(e){ 
		e.preventDefault();
		if(step < max_steps) {
			step++; 
			$(wrapper_step).append('<div class="input-field col s12" style="float: none;width: 78%;padding-left: 6%;"><textarea id="recipe_step" type="text" name="recipe_step"/></textarea><label for="recipe_step"></label><a href="#" class="remove_field"><i class="far fa-trash-alt"></i></a></div>'); 
		}
	});
	
	$(wrapper_step).on("click",".remove_field", function(e){
		e.preventDefault(); $(this).parent('div').remove(); step--;
	});
});
