if(localStorage.getItem("horizontal")){
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

if(localStorage.getItem("sidebar-mini")){
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
    localStorage.setItem("sidebar-mini", "True");
    menuClick();
    checkHoriMenu();
}

if(localStorage.getItem("horizontal-hover")){
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

if(localStorage.getItem("color-menu")){
    $('body').addClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('dark-menu');
    $('body').removeClass('gradient-menu');
}

if(localStorage.getItem("dark-menu")){
    $('body').addClass('dark-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('gradient-menu');
}

if(localStorage.getItem("gradient-menu")){
    $('body').addClass('gradient-menu');
    $('body').removeClass('color-menu');
    $('body').removeClass('light-menu');
    $('body').removeClass('dark-menu');
}

if(localStorage.getItem("light-header")){
    $('body').addClass('light-header');
    $('body').removeClass('color-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('gradient-header');
}

if(localStorage.getItem("color-header")){
    $('body').addClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('dark-header');
    $('body').removeClass('gradient-header');
}

if(localStorage.getItem("dark-header")){
    $('body').addClass('dark-header');
    $('body').removeClass('color-header');
    $('body').removeClass('light-header');
    $('body').removeClass('gradient-header');
}

if(localStorage.getItem("layout-fullwidth")){
    $('body').addClass('layout-fullwidth');
    checkHoriMenu();
    $('body').removeClass('layout-boxed');
}

if(localStorage.getItem("layout-boxed")){
    $('body').addClass('layout-boxed');
    checkHoriMenu();
    $('body').removeClass('layout-fullwidth');
}

if(localStorage.getItem("fixed-layout")){
    $('body').addClass('fixed-layout');
    $('body').removeClass('scrollable-layout');
}

if(localStorage.getItem("scrollable-layout")){
    $('body').addClass('scrollable-layout');
    $('body').removeClass('fixed-layout');
}

if(localStorage.getItem("default-menu")){
    $('body').addClass('default-menu');
    hovermenu();
    $('body').removeClass('closed-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('sidenav-toggled');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(localStorage.getItem("closed-menu")){
    $('body').addClass('closed-menu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(localStorage.getItem("icontext-menu")){
    $('body').addClass('icontext-menu');
    icontext();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(localStorage.getItem("sideicon-menu")){
    $('body').addClass('sideicon-menu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
    $('body').removeClass('hover-submenu1');
}

if(localStorage.getItem("hover-submenu")){
    $('body').addClass('hover-submenu');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu1');
}

if(localStorage.getItem("hover-submenu1")){
    $('body').addClass('hover-submenu1');
    hovermenu();
    $('body').addClass('sidenav-toggled');
    $('body').removeClass('default-menu');
    $('body').removeClass('icontext-menu');
    $('body').removeClass('sideicon-menu');
    $('body').removeClass('closed-menu');
    $('body').removeClass('hover-submenu');
}