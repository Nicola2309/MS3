/*This code is inspired by my fellow student Ian M from his project "Larder" https://github.com/iainm342/milestone-3/blob/main/static/js/recipe.js */
$(document).ready(function() {
    console.log("SCRIPT STARTS");
	var max_ingr = 30;
    var wrapper_ingr  = $("#ingr-input");
	var add_ingr_button  = $(".add-ingr-buttn");
	
	var ingr = 1;
	 $(add_ingr_button).click(function(e){
	 	e.preventDefault();
	 	if(ingr < max_ingr) { 
	 		ingr++; 
	 		$(wrapper_ingr).append('<div class="col s11" style="float:right;"><input id="add-ingredients" type="text" name="add-ingredients" required/><label for="add-ingredients"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
	 	}
     });
/*
    $('.fa-plus').click(function(e){
        e.preventDefault();
        console.log("CLICK EVENT");
		$(test).append('<div class="col s11" style="float:right;"><input id="add-ingredients" type="text" name="add-ingredients" required/><label for="add-ingredients"></label><a href="#" class="remove_field"><i class="fas fa-trash-alt"></i></a></div>');
		
    });*/
	
	$(wrapper_ingr).on("click",".remove_field", function(e){ 
		e.preventDefault(); $(this).parent('div').remove(); ingr--;
	});
/*
	var max_meth      		= 40; 
	var wrapper_meth   		= $(".input_meth_wrap"); 
	var add_meth_button      = $(".add_meth_button");
	
	var meth = 1; 
	$(add_meth_button).click(function(e){ 
		e.preventDefault();
		if(meth < max_meth) {
			meth++; 
			$(wrapper_meth).append('<div class="col s12" id="wrap"><textarea id="recipe_method" type="text" name="recipe_method"/></textarea><label for="recipe_method"></label><a href="#" class="remove_field"><i class="far fa-trash-alt"></i></a></div>'); 
		}
	});
	
	$(wrapper_meth).on("click",".remove_field", function(e){
		e.preventDefault(); $(this).parent('div').remove(); meth--;
	});*/
});
