$(document).ready(function () {
   $('.sidenav').sidenav({
      edge: "right"
   });
   $('select').formSelect();
   $('.modal').modal();
   $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true,
   });
   setInterval(function () {
      $('.carousel').carousel('next');
   }, 3000);

   validateMaterializeSelect();

   /* Code from CI lesson to use validate class on dropdowns menu's in Materialize, here the github link : https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js */
   function validateMaterializeSelect() {

      /* Setting two new variables with CSS styles that will match the
      Materialize validation. Valid=green, invalid=red*/

      let classValid = {
         "border-bottom": "1px solid #4caf50",
         "box-shadow": "0 1px 0 0 #4caf50"
      };
      let classInvalid = {
         "border-bottom": "1px solid #f44336",
         "box-shadow": "0 1px 0 0 #f44336"
      };

      /* If any elements have
      the 'required' property Unhide the selected elements hidden by default by Materialize. 
      We hide it unhide it for the DOM but hide it for the human user, giving the element no width nor height*/

      if ($("select.validate").prop("required")) {
         $("select.validate").css({
            "display": "block",
            "height": "0",
            "padding": "0",
            "width": "0",
            "position": "absolute"
         });
      }

      // We traverse the DOM with parents and children selectors 
      $(".select-wrapper input.select-dropdown").on("focusin", function () {
         $(this).parent(".select-wrapper").on("change", function () {
            /* if one of the list-items is selected but is not disabled
            we apply the classValid class */
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
               $(this).children("input").css(classValid);
            }
         });
      }).on("click", function () {
         /* we apply a green class again if there aren't any valid or invalid classes applyed */
         if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
            /*If the user didn't properly select anything the classInvalid and the red color is applied */
         } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
               if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                  if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                     $(this).parent(".select-wrapper").children("input").css(classInvalid);
                  }
               }
            });
         }
      });
   }
});

/* Scrolling navbar code inspired from the tutorial by Techno Solution at this link https://www.youtube.com/watch?v=HINs4W_pGGU&ab_channel=ConorBailey */

$(window).scroll(function () {

   $('nav').toggleClass('scrolled', $(this).scrollTop() > 42);
});