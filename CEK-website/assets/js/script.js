$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.carousel.carousel-slider').carousel({
    	fullWidth: true,
			indicators:true,
  	});
    $('.materialboxed').materialbox();
	
		$('.dropdown-trigger').dropdown({
			hover: true,
			closeOnClick: true,
    	coverTrigger: false,
    	constrainWidth: false
		});
		$("#mobile a[data-target]").each(function(){
			var li = $(this).parent();
			var target = $(this).attr("data-target");
			var dd = $("#"+target).clone();
			dd.removeAttr("id");
			li.append(dd);
			$(this).removeAttr("data-target");
			$(this).click(function(e){
				e.preventDefault();
				li.find(".dropdown-content").slideToggle(150);
			})
		})
		var navTop = $("nav").offset().top;
		$(window).scroll(function(){
			if($(this).scrollTop() >= navTop){
				$("nav").addClass("fixed");
			}else{
				$("nav").removeClass("fixed");
			}
		})
});