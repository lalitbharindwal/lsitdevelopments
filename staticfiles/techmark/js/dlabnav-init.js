"use strict"

var dlabSettingsOptions = {};

(function($) {

	"use strict"
	
	/* var direction =  getUrlParams('dir');
	
	if(direction == 'rtl')
	{
        direction = 'rtl'; 
    }else{
        direction = 'ltr'; 
    } */

	dlabSettingsOptions = {};
	
	if(localStorage.getItem("version")||localStorage.getItem("sidebarStyle")||localStorage.getItem("layout")||localStorage.getItem("primary")||localStorage.getItem("headerBg")||localStorage.getItem("navheaderBg")||localStorage.getItem("sidebarBg")||localStorage.getItem("sidebarStyle")||localStorage.getItem("sidebarPosition")||localStorage.getItem("headerPosition")||localStorage.getItem("containerLayout")){
		dlabSettingsOptions = {
			typography: localStorage.getItem("typography"),
			version: localStorage.getItem("version"),
			layout: localStorage.getItem("layout"),
			primary: localStorage.getItem("primary"),
			headerBg: localStorage.getItem("headerBg"),
			navheaderBg: localStorage.getItem("navheaderBg"),
			sidebarBg: localStorage.getItem("sidebarBg"),
			sidebarStyle: localStorage.getItem("sidebarStyle"),
			sidebarPosition: localStorage.getItem("sidebarPosition"),
			headerPosition: localStorage.getItem("headerPosition"),
			containerLayout: localStorage.getItem("containerLayout")
		};
	}else{
		dlabSettingsOptions = {
			typography: "poppins",
			version: "light",
			layout: "vertical",
			primary: "color_1",
			headerBg: "color_1",
			navheaderBg: "color_1",
			sidebarBg: "color_1",
			sidebarStyle: "full",
			sidebarPosition: "fixed",
			headerPosition: "fixed",
			containerLayout: "full",
		};
	}
	
	new dlabSettings(dlabSettingsOptions); 

	jQuery(window).on('resize',function(){
        /*Check container layout on resize */
		///alert(dlabSettingsOptions.primary);
        dlabSettingsOptions.containerLayout = $('#container_layout').val();
        /*Check container layout on resize END */
        
		new dlabSettings(dlabSettingsOptions); 
	});
	
})(jQuery);