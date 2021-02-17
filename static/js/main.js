(function ($) {
	"use strict";
	var nav = $('nav');
  var navHeight = nav.outerHeight();
  
  $('.navbar-toggler').on('click', function() {
    if( ! $('#mainNav').hasClass('navbar-reduce')) {
      $('#mainNav').addClass('navbar-reduce');
    }
  })

  // Preloader
  $(window).on('load', function () {
    if ($('#preloader').length) {
      $('#preloader').delay(100).fadeOut('slow', function () {
        $(this).remove();
      });
    }
  });

  // Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });
  $('.back-to-top').click(function(){
    $('html, body').animate({scrollTop : 0},1500, 'easeInOutExpo');
    return false;
  });

	/*--/ Star ScrollTop /--*/
	$('.scrolltop-mf').on("click", function () {
		$('html, body').animate({
			scrollTop: 0
		}, 1000);
	});

	/*--/ Star Counter /--*/
	$('.counter').counterUp({
		delay: 15,
		time: 2000
	});

	/*--/ Star Scrolling nav /--*/
	$('a.js-scroll[href*="#"]:not([href="#"])').on("click", function () {
		if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			if (target.length) {
				$('html, body').animate({
					scrollTop: (target.offset().top - navHeight + 5)
				}, 1000, "easeInOutExpo");
				return false;
			}
		}
	});

	// Closes responsive menu when a scroll trigger link is clicked
	$('.js-scroll').on("click", function () {
		$('.navbar-collapse').collapse('hide');
	});

	// Activate scrollspy to add active class to navbar items on scroll
	$('body').scrollspy({
		target: '#mainNav',
		offset: navHeight
	});
	/*--/ End Scrolling nav /--*/

	/*--/ Navbar Menu Reduce /--*/
	$(window).trigger('scroll');
	$(window).on('scroll', function () {
		var pixels = 50; 
		var top = 1200;
		if ($(window).scrollTop() > pixels) {
			$('.navbar-expand-md').addClass('navbar-reduce');
			$('.navbar-expand-md').removeClass('navbar-trans');
		} else {
			$('.navbar-expand-md').addClass('navbar-trans');
			$('.navbar-expand-md').removeClass('navbar-reduce');
		}
		if ($(window).scrollTop() > top) {
			$('.scrolltop-mf').fadeIn(1000, "easeInOutExpo");
		} else {
			$('.scrolltop-mf').fadeOut(1000, "easeInOutExpo");
		}
	});

	/*--/ Star Typed /--*/
	if ($('.text-slider').length == 1) {
    var typed_strings = $('.text-slider-items').text();
		var typed = new Typed('.text-slider', {
			strings: typed_strings.split(','),
			typeSpeed: 80,
			loop: true,
			backDelay: 1100,
			backSpeed: 30
		});
	}

	/*--/ Testimonials owl /--*/
	$('#testimonial-mf').owlCarousel({
		margin: 20,
		autoplay: true,
		autoplayTimeout: 4000,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 1,
			}
		}
	});

	/* function for ajax request */
	function ajaxRequest(method, data, success) {
		$.ajax({
		  	url: '',
	  		type: method,
	  		data: data,
	  		success: success
		});
	}

	//Contact
  	$('form.contactForm').submit( function(event) {
	    var f = $(this).find('.form-group');
      	var ferror = false;
      	var emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

      	// walk through all inputs
	    f.children('input').each( function() {
	    	
	    	// current input
	        var i = $(this);
	      	var rule = i.attr('data-rule');

		    if (rule !== undefined) {
		    	// error flag for current input
		        var ierror = false;
		        var pos = rule.indexOf(':', 0);
	        	if (pos >= 0) {
	          		var exp = rule.substr(pos + 1, rule.length);
	          		rule = rule.substr(0, pos);
	        	} else {
	          		rule = rule.substr(pos + 1, rule.length);
	        	}

		        switch (rule) {
		          case 'required':
		            if (i.val() === '') {
		            	ferror = ierror = true;
		            }
		            break;

		          case 'minlen':
		            if (i.val().length < parseInt(exp)) {
		              	ferror = ierror = true;
		            }
		            break;

		          case 'email':
		            if (!emailExp.test(i.val())) {
		              	ferror = ierror = true;
		            }
		            break;

		          case 'checked':
		            if (! i.is(':checked')) {
		              	ferror = ierror = true;
		            }
		            break;

		          case 'regexp':
		            exp = new RegExp(exp);
		            if (!exp.test(i.val())) {
		              	ferror = ierror = true;
		            }
		            break;
		        }
	        	i.next('.validation').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
	      	}
	    });

	    // walk through all inputs
	    f.children('textarea').each(function() {
	    // current input
	    var i = $(this);
	    var rule = i.attr('data-rule');

	    if (rule !== undefined) {
	      	// error flag for current input
	        var ierror = false;
	        var pos = rule.indexOf(':', 0);
	        if (pos >= 0) {
	          	var exp = rule.substr(pos + 1, rule.length);
	          	rule = rule.substr(0, pos);
	        } else {
	          	rule = rule.substr(pos + 1, rule.length);
	        }

	        switch (rule) {
	          	case 'required':
	            	if (i.val() === '') {
	              		ferror = ierror = true;
	            	}
	            	break;

	          	case 'minlen':
	            	if (i.val().length < parseInt(exp)) {
	              		ferror = ierror = true;
	            	}
	            	break;
	        }
	        	i.next('.validation').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
	      	}
    	});
    	var obj= {};
	    if (ferror) {
	    	return false;
	    	alert(form_data);
	    	event.preventDefault();
	    } else {
	    	var data = $("form").serialize().split("&");
    		for(var key in data) {
        		obj[data[key].split("=")[0]] = data[key].split("=")[1];
    		}
	 	}

	    let success = response => {
	        if (response.message == 'OK') {
		        $("#sendmessage").addClass("show");
		        $("#errormessage").removeClass("show");
		        $('.contactForm').find("input, textarea").val("");
		        event.preventDefault();
	        } else {
		        $("#sendmessage").removeClass("show");
		        $("#errormessage").addClass("show");
		        $('#errormessage').html(response.message);
		        event.preventDefault();
	        }
      	}
	    ajaxRequest('POST', obj, success);
	    return false;
	});
})(jQuery);
