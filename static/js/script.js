$(document).ready(function(){
    $('.sidenav').sidenav({ edge:"right" });
    $('select').formSelect();
    $('.modal').modal();
    $('.carousel.carousel-slider').carousel(
    {
    fullWidth: true,
    indicators: true,
  });
  setInterval(function() {
    $('.carousel').carousel('next');
  }, 3000);    

});

/* Scrolling navbar code inspired from the tutorial by Techno Solution at this link https://www.youtube.com/watch?v=HINs4W_pGGU&ab_channel=ConorBailey */

$(window).scroll(function(){

    $('nav').toggleClass('scrolled', $(this).scrollTop()>42);
});


