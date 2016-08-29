// JavaScript Document
$(document).ready(function() {

  var active1 = false;
  var active2 = false;
  var active3 = false;
  var active4 = false;

    $('.radial-menu').on('mousedown touchstart', function() {
    
    if (!active1) $(this).find('.menu-item1').css({'background-color': 'gray', 'transform': 'translate(0px,125px)'});
    else $(this).find('.menu-item1').css({'background-color': 'dimGray', 'transform': 'none'}); 
     if (!active2) $(this).find('.menu-item2').css({'background-color': 'gray', 'transform': 'translate(60px,105px)'});
    else $(this).find('.menu-item2').css({'background-color': 'darkGray', 'transform': 'none'});
      if (!active3) $(this).find('.menu-item3').css({'background-color': 'gray', 'transform': 'translate(105px,60px)'});
    else $(this).find('.menu-item3').css({'background-color': 'silver', 'transform': 'none'});
      if (!active4) $(this).find('.menu-item4').css({'background-color': 'gray', 'transform': 'translate(125px,0px)'});
    else $(this).find('.menu-item4').css({'background-color': 'silver', 'transform': 'none'});
    active1 = !active1;
    active2 = !active2;
    active3 = !active3;
    active4 = !active4;
      
    });
});