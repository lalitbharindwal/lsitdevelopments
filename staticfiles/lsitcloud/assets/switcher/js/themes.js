
var theam = {
    "nevigation_style": ""
}
function apply_theme(){
   const nevigation_style = document.querySelector('input[name="onoffswitch15"]:checked');
   if(nevigation_style.id == 'myonoffswitch34'){
    theam["nevigation_style"] = "sidebar-mini";
   }else if(nevigation_style.id == 'myonoffswitch35'){
    theam["nevigation_style"] = "horizontal";
   }else if(nevigation_style.id == 'myonoffswitch111'){
    theam["nevigation_style"] = "horizontal-hover";
   }

    // Get the selected radio button for theme style
    const selectedThemeStyle1 = document.querySelector('input[name="onoffswitch1"]:checked');
    if (selectedThemeStyle1) {
        if(selectedThemeStyle1.id == 'myonoffswitch1'){
            theam.themeStyle = "light";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const selectedThemeStyle2 = document.querySelector('input[name="onoffswitch1"]:checked');
    if (selectedThemeStyle2) {
        if(selectedThemeStyle2.id == 'myonoffswitch2'){
            theam.themeStyle = "dark";
            theam.darkPrimary = localStorage.getItem("darkPrimary");
            theam.darkprimaryTransparent = localStorage.getItem("darkprimaryTransparent");
        }
    }

    const selectedThemeStyle3 = document.querySelector('input[name="onoffswitch1"]:checked');
    if (selectedThemeStyle3 && !(localStorage.getItem("BgImage"))) {
        if(selectedThemeStyle3.id == 'myonoffswitchTransparent'){
            theam.themeStyle = "transperent";
            theam.transparentPrimary = localStorage.getItem("transparentPrimary");
            theam.transparentBgColor = localStorage.getItem("transparentBgColor");
            theam.transparentThemeColor = localStorage.getItem("transparentThemeColor");
            theam.transparentprimaryTransparent = localStorage.getItem("transparentprimaryTransparent");
        }
    }

    const leftmenustyle1 = document.querySelector('input[name="onoffswitch2"]:checked');
    if (leftmenustyle1) {
        if(leftmenustyle1.id == 'myonoffswitch3'){
            theam.leftmenustyle = "light-menu";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const leftmenustyle2 = document.querySelector('input[name="onoffswitch2"]:checked');
    if (leftmenustyle2) {
        if(leftmenustyle2.id == 'myonoffswitch4'){
            theam.leftmenustyle = "color-menu";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const leftmenustyle3 = document.querySelector('input[name="onoffswitch2"]:checked');
    if (leftmenustyle3) {
        if(leftmenustyle3.id == 'myonoffswitch5'){
            theam.leftmenustyle = "dark-menu";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const leftmenustyle4 = document.querySelector('input[name="onoffswitch2"]:checked');
    if (leftmenustyle4) {
        if(leftmenustyle4.id == 'myonoffswitch25'){
            theam.leftmenustyle = "gradient-menu";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const headerstyle1 = document.querySelector('input[name="onoffswitch3"]:checked');
    if (headerstyle1) {
        if(headerstyle1.id == 'myonoffswitch6'){
            theam.headerstyle = "light-header";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const headerstyle2 = document.querySelector('input[name="onoffswitch3"]:checked');
    if (headerstyle2) {
        if(headerstyle2.id == 'myonoffswitch7'){
            theam.headerstyle = "color-header";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const headerstyle3 = document.querySelector('input[name="onoffswitch3"]:checked');
    if (headerstyle3) {
        if(headerstyle3.id == 'myonoffswitch8'){
            theam.headerstyle = "dark-header";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const headerstyle4 = document.querySelector('input[name="onoffswitch3"]:checked');
    if (headerstyle4) {
        if(headerstyle4.id == 'myonoffswitch26'){
            theam.headerstyle = "gradient-header";
            theam.primaryColor = localStorage.getItem("primaryColor");
            theam.primaryBorderColor = localStorage.getItem("primaryBorderColor");
            theam.primaryHoverColor = localStorage.getItem("primaryHoverColor");
            theam.primaryTransparent = localStorage.getItem("primaryTransparent");
        }
    }

    const layoutwidthstyle1 = document.querySelector('input[name="onoffswitch4"]:checked');
    if (layoutwidthstyle1) {
        if(layoutwidthstyle1.id == 'myonoffswitch9'){
            theam.layoutwidthstyle = "layout-fullwidth";
        }
    }

    const layoutwidthstyle2 = document.querySelector('input[name="onoffswitch4"]:checked');
    if (layoutwidthstyle2) {
        if(layoutwidthstyle2.id == 'myonoffswitch10'){
            theam.layoutwidthstyle = "layout-boxed";
        }
    }

    const layoutposition1 = document.querySelector('input[name="onoffswitch5"]:checked');
    if (layoutposition1) {
        if(layoutposition1.id == 'myonoffswitch11'){
            theam.layoutposition = "fixed-layout";
        }
    }

    const layoutposition2 = document.querySelector('input[name="onoffswitch5"]:checked');
    if (layoutposition2) {
        if(layoutposition2.id == 'myonoffswitch12'){
            theam.layoutposition = "scrollable-layout";
        }
    }

    const sidemenulayout1 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout1) {
        if(sidemenulayout1.id == 'myonoffswitch13'){
            theam.sidemenulayout = "default-menu";
        }
    }

    const sidemenulayout2 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout2) {
        if(sidemenulayout2.id == 'myonoffswitch30'){
            theam.sidemenulayout = "closed-menu";
        }
    }

    const sidemenulayout3 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout3) {
        if(sidemenulayout3.id == 'myonoffswitch14'){
            theam.sidemenulayout = "icon-with-text";
        }
    }

    const sidemenulayout4 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout4) {
        if(sidemenulayout4.id == 'myonoffswitch15'){
            theam.sidemenulayout = "icon-overlay";
        }
    }

    const sidemenulayout5 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout5) {
        if(sidemenulayout5.id == 'myonoffswitch32'){
            theam.sidemenulayout = "hover-submenu-text";
        }
    }

    const sidemenulayout6 = document.querySelector('input[name="onoffswitch6"]:checked');
    if (sidemenulayout6) {
        if(sidemenulayout6.id == 'myonoffswitch33'){
            theam.sidemenulayout = "hover-submenu-icon";
        }
    }

   fetch('save_theme', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()  // Add CSRF token to the request headers
        },
        body: JSON.stringify(theam), // The JSON object you want to save
    })
    .then(response => response.json())
    .then(data => {
        console.log('Theme saved successfully:', data);
    })
    .catch(error => {
        console.error('Error saving theme:', error);
    });
}

function handleBgImageClick(imageId) {
    theam.themeStyle = "bg-img";
    theam.BgImage = imageId;
    theam.transparentBgImgPrimary = localStorage.getItem("transparentBgImgPrimary");
    theam.transparentBgImgprimaryTransparent = localStorage.getItem("transparentBgImgprimaryTransparent");
}

// Function to get the CSRF token from the meta tag
function getCSRFToken() {
    return document.querySelector('[name=csrf-token]').getAttribute('content');
}

const decodedData = JSON.parse(default_theme.replace(/&quot;/g, '"')); // Replace &quot; with "
localStorage.clear();
sessionStorage.clear();
Object.entries(decodedData).forEach(([key, value]) => {
    if(key == "primaryColor" || key == "primaryBorderColor" || key == "primaryHoverColor" || key == "primaryTransparent" || key == "darkPrimary" || key == "darkprimaryTransparent" || key == "transparentPrimary" || key == "transparentprimaryTransparent" || key == "transparentBgImgPrimary" || key == "transparentBgImgprimaryTransparent" || key == "transparentBgColor" || key == "transparentThemeColor"){
        localStorage.setItem(key, value !== null ? value : "null");
    }else{
        sessionStorage.setItem(key, value !== null ? value : "null");    
    }
});

//nevigation_style
if(sessionStorage.getItem("nevigation_style") == "sidebar-mini"){
    $('body').removeClass('horizontal');
    $('body').removeClass('horizontal-hover');
    $(".main-content").removeClass("horizontal-content");
    $(".main-content").addClass("app-content");
    $(".main-container").removeClass("container");
    $(".main-container").addClass("container-fluid");
    $(".main-header").removeClass("hor-header");
    $(".main-header").addClass("side-header");
    $(".app-sidebar").removeClass("horizontal-main");
    $(".main-sidemenu").removeClass("container");
    $('#slide-left').removeClass('d-none');
    $('#slide-right').removeClass('d-none');
    $('body').addClass('sidebar-mini');
    menuClick();
    checkHoriMenu();
}

if(sessionStorage.getItem("nevigation_style") == "horizontal"){
    $('body').addClass('horizontal');
    $(".main-content").addClass("horizontal-content");
    $(".main-content").removeClass("app-content");
    $(".main-container").addClass("container");
    $(".main-container").removeClass("container-fluid");
    $(".main-header").addClass("hor-header");
    $(".main-header").removeClass("side-header");
    $(".app-sidebar").addClass("horizontal-main");
    $(".main-sidemenu").addClass("container");
    $('body').removeClass('sidebar-mini');
    $('body').removeClass('sidenav-toggled');
    $('#slide-left').removeClass('d-none');
    $('#slide-right').removeClass('d-none');
    $('body').removeClass('horizontal-hover');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    document.querySelector('.horizontal .side-menu').style.flexWrap = 'noWrap';
    menuClick();
    checkHoriMenu();
}

if(sessionStorage.getItem("nevigation_style") == "horizontal-hover"){
      var li = document.querySelectorAll('.side-menu li');
      li.forEach(function (e, i) {
        e.classList.remove('is-expanded');
      });
      var animationSpeed = 300; // first level

      var parent = $("[data-bs-toggle='sub-slide']").parents('ul');
      var ul = parent.find('ul:visible').slideUp(animationSpeed);
      ul.removeClass('open');
      var parent1 = $("[data-bs-toggle='sub-slide2']").parents('ul');
      var ul1 = parent1.find('ul:visible').slideUp(animationSpeed);
      ul1.removeClass('open'); // let dd = document.querySelectorAll('.sub-slide-menu');
      // dd.forEach((e,i)=>{
      // 	let eVal = e.classList[0]
      // 	var ul1 = $('.'+eVal).find('ul:visible').slideUp(animationSpeed);
      // 	ul1.removeClass('open');
      // })

      $('body').addClass('horizontal-hover');
      $('body').addClass('horizontal');
      var subNavSub = document.querySelectorAll('.sub-slide-menu');
      subNavSub.forEach(function (e) {
        e.style.display = '';
      });
      var subNav = document.querySelectorAll('.slide-menu');
      subNav.forEach(function (e) {
        e.style.display = '';
      }); // $('#slide-left').addClass('d-none');
      // $('#slide-right').addClass('d-none');

      document.querySelector('.horizontal .side-menu').style.flexWrap = 'nowrap';
      $(".main-content").addClass("horizontal-content");
      $(".main-content").removeClass("app-content");
      $(".main-container").addClass("container");
      $(".main-container").removeClass("container-fluid");
      $(".main-header").addClass("hor-header");
      $(".main-header").removeClass("side-header");
      $(".app-sidebar").addClass("horizontal-main");
      $(".main-sidemenu").addClass("container");
      $('body').removeClass('sidebar-mini');
      $('body').removeClass('sidenav-toggled');
      $('body').removeClass('closed-menu');
      $('body').removeClass('hover-submenu');
      $('body').removeClass('hover-submenu1');
      $('body').removeClass('icontext-menu');
      $('body').removeClass('sideicon-menu');
      HorizontalHovermenu();
      checkHoriMenu();
}

//themestyle
if(sessionStorage.getItem("themeStyle") == "light"){
    $('body').addClass('light-theme');
    $('#myonoffswitch3').prop('checked', true);
    $('#myonoffswitch6').prop('checked', true);
    $('body').removeClass('dark-theme');
    $('body').removeClass('transparent-theme');
    $('body').removeClass('light-menu');
    $('body').removeClass('dark-theme');
    $('body').removeClass('color-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('dark-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('gradient-header');
    $('body').removeClass('color-menu');
}

if(sessionStorage.getItem("themeStyle") == "dark"){
    $('body').addClass('dark-theme');
    $('#myonoffswitch5').prop('checked', true);
    $('#myonoffswitch8').prop('checked', true);
    $('body').removeClass('light-theme');
    $('body').removeClass('transparent-theme');
    $('body').removeClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header'); // remove light theme properties
}

if(sessionStorage.getItem("themeStyle") == "transperent"){
    $('body').addClass('transparent-theme');
    $('#myonoffswitch3').prop('checked', false);
    $('#myonoffswitch6').prop('checked', false);
    $('#myonoffswitch5').prop('checked', false);
    $('#myonoffswitch8').prop('checked', false);
    $('body').removeClass('dark-theme');
    $('body').removeClass('light-theme'); // remove light theme properties
}

if(sessionStorage.getItem("BgImage") == "bg-img1 bg-img"){
    $('body').addClass('bg-img1');
    $('body').removeClass('bg-img2');
    $('body').removeClass('bg-img3');
    $('body').removeClass('bg-img4');
    $('body').removeClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
    $('body').addClass('scrollable-layout');
    document.querySelector('body').classList.add('transparent-theme');
    $('#myonoffswitch2').prop('checked', false);
    $('#myonoffswitch1').prop('checked', false);
    $('#myonoffswitchTransparent').prop('checked', true);
}

if(sessionStorage.getItem("BgImage") == "bg-img2 bg-img"){
    $('body').addClass('bg-img2');
    $('body').removeClass('bg-img1');
    $('body').removeClass('bg-img3');
    $('body').removeClass('bg-img4');
    $('body').removeClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
    $('body').addClass('scrollable-layout');
    $('#myonoffswitch2').prop('checked', false);
    $('#myonoffswitch1').prop('checked', false);
    $('#myonoffswitchTransparent').prop('checked', true);
}

if(sessionStorage.getItem("BgImage") == "bg-img3 bg-img"){
    $('body').addClass('bg-img3');
    $('body').removeClass('bg-img1');
    $('body').removeClass('bg-img2');
    $('body').removeClass('bg-img4');
    $('body').removeClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
    $('body').addClass('scrollable-layout');
    $('#myonoffswitch2').prop('checked', false);
    $('#myonoffswitch1').prop('checked', false);
    $('#myonoffswitchTransparent').prop('checked', true);
}

if(sessionStorage.getItem("BgImage") == "bg-img4 bg-img"){
    $('body').addClass('bg-img4');
    $('body').removeClass('bg-img1');
    $('body').removeClass('bg-img2');
    $('body').removeClass('bg-img3');
    $('body').removeClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('gradient-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
    $('body').addClass('scrollable-layout');
    $('#myonoffswitch2').prop('checked', false);
    $('#myonoffswitch1').prop('checked', false);
    $('#myonoffswitchTransparent').prop('checked', true);
}

//leftmenustyle
if(sessionStorage.getItem("leftmenustyle") == "light-menu"){
    $('body').addClass('light-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('gradient-menu');
}

if(sessionStorage.getItem("leftmenustyle") == "color-menu"){
    $('body').addClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('gradient-menu');
}

if(sessionStorage.getItem("leftmenustyle") == "dark-menu"){
    $('body').addClass('dark-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('gradient-menu');
}

if(sessionStorage.getItem("leftmenustyle") == "gradient-menu"){
    $('body').addClass('gradient-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('dark-menu');
}


//headerstyle
if(sessionStorage.getItem("headerstyle") == "light-header"){
    $('body').addClass('light-header');
    $('body').removeClass('color-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('gradient-header');
}

if(sessionStorage.getItem("headerstyle") == "color-header"){
    $('body').addClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('gradient-header');
}

if(sessionStorage.getItem("headerstyle") == "dark-header"){
    $('body').addClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
}

if(sessionStorage.getItem("headerstyle") == "gradient-header"){
    $('body').addClass('gradient-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
}

//layoutwidthstyle
if(sessionStorage.getItem("layoutwidthstyle") == "layout-fullwidth"){
    $('body').addClass('layout-fullwidth');
    checkHoriMenu();
    $('body').removeClass('layout-boxed');
}

if(sessionStorage.getItem("layoutwidthstyle") == "layout-boxed"){
    $('body').addClass('layout-boxed');
    checkHoriMenu();
    $('body').removeClass('layout-fullwidth');
}

//layoutposition
if(sessionStorage.getItem("layoutposition") == "fixed-layout"){
    $('body').addClass('fixed-layout');
    $('body').removeClass('scrollable-layout');
}

if(sessionStorage.getItem("layoutposition") == "scrollable-layout"){
    $('body').addClass('scrollable-layout');
    $('body').removeClass('fixed-layout');
}

//sidemenu
if(sessionStorage.getItem("sidemenulayout") == "default-menu"){
    $('body').addClass('default-menu');
    hovermenu();
    $('body').removeClass('closed-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('sidenav-toggled');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(sessionStorage.getItem("sidemenulayout") == "closed-menu"){
    $('body').addClass('closed-menu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(sessionStorage.getItem("sidemenulayout") == "icon-with-text"){
    $('body').addClass('icontext-menu');
    icontext();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(sessionStorage.getItem("sidemenulayout") == "icon-overlay"){
    $('body').addClass('sideicon-menu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(sessionStorage.getItem("sidemenulayout") == "hover-submenu-text"){
    $('body').addClass('hover-submenu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu1');
}

if(sessionStorage.getItem("sidemenulayout") == "hover-submenu-icon"){
    $('body').addClass('hover-submenu1');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
}