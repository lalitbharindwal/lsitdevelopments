
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
    if (selectedThemeStyle3) {
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
            theam.layoutwidthstyle1 = "layout-fullwidth";
        }
    }

    const layoutwidthstyle2 = document.querySelector('input[name="onoffswitch4"]:checked');
    if (layoutwidthstyle2) {
        if(layoutwidthstyle2.id == 'myonoffswitch10'){
            theam.layoutwidthstyle1 = "layout-boxed";
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
   console.log(theam)
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