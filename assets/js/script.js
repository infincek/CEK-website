$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.carousel.carousel-slider').carousel({
    	fullWidth: true,
    	indicators:true
  	});
    $('.materialboxed').materialbox();
    $('.dropdown-trigger').dropdown({
    	hover: true,
    	coverTrigger: false,
    	constrainWidth: false
    });
});