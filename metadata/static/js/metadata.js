$( document ).ready(function(){
	var toggleButton = $('a#menu-toggle');
	var sidebar = $('nav#sidebar');
	
	toggleButton.click(function(){
		sidebar.toggleClass('slideIn');
	});
});