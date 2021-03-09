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

/* Scrolling navbar code inspired from the tutorial at this link https://www.youtube.com/watch?v=HINs4W_pGGU&ab_channel=ConorBailey */

$(window).scroll(function(){

    $('nav').toggleClass('scrolled', $(this).scrollTop()>42);
});

// Transition Functions 
/*function scrollAppear(){
    let textSlideInit = document.querySelector('.text-1-slide-init');
    let beginPosition = textSlideInit.getBoundingClientRect().top;
    let screenPosition = window.innerHeight / 1.5;

    if(beginPosition < screenPosition){
        textSlideInit.classList.add('.text-1-slide-end')
    }
}

 window.addEventListener('scroll', scrollAppear);*/


//Source code https://www.taniarascia.com/smooth-scroll-to-id-with-jquery/
/*$('a[href*="#"]').on('click', function (e) {
  e.preventDefault()

  $('html, body').animate(
    {
      scrollTop: $($(this).attr('href')).offset().top,
    },
    800,
    'linear'
  )
});*/
