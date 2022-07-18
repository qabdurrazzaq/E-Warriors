(function($){

"use strict";

    // Animsition
    var Animsition = function() {

        // Handle Animsition Function
        var handleAnimsitionFunction = function() {
            if( /MSIE\s/.test(navigator.userAgent) && parseFloat(navigator.appVersion.split("MSIE")[1]) < 10 ){
                // IE < 10
                $('.animsition').removeClass('animsition');
                return;
            }

            //$('.animsition').css('opacity', 1);
            $(".animsition").animsition({
                inClass: 'fade-in',
                outClass: 'fade-out',
                inDuration: 1500,
                outDuration: 800,
                loading: true,
                loadingParentElement: 'body',
                loadingClass: 'animsition-loading',
                // loadingInner: '', // e.g '<img src="loading.svg" />'
                timeout: false,
                timeoutCountdown: 0,
                onLoadEvent: true,
                browser: [
                    'animation-duration',
                    '-webkit-animation-duration',
                    '-moz-animation-duration',
                    '-o-animation-duration'
                    ],
                overlay: false,
                overlayClass: 'animsition-overlay-slide',
                overlayParentElement: 'body',
                transition: function(url){ window.location.href = url; }
            });

            $(".animsition").on('animsition.inEnd', function(){
                // var $thisAn = $(this);
                // setTimeout( function(){
                    $(this).addClass('animsition-ended');
                // }, 1500); // = inDuration
            })

            // $(".animsition").on('animsition.inStart', function(){
            //     //$('.animsition').css('opacity',1);
            //     setTimeout( function(){

            //         if( $('.ark-boxed__body-wrapper').size() > 0 ){

            //             $('.animsition').animate({opacity:1},400);
            //         }
            //     }, 100);
            // });

            // $(".animsition").on('animsition.inEnd', function(){

            // });
        }

        return {
            init: function() {
                handleAnimsitionFunction(); // initial setup for animsition function
            }
        }
    }();


    Animsition.init();
    

})(jQuery);