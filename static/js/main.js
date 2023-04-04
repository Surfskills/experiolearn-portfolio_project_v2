(function ($) {
    "use strict";

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 40) {
            $('.navbar').addClass('sticky-top');
        } else {
            $('.navbar').removeClass('sticky-top');
        }
    });
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        items: 1,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
    });
    
})(jQuery);

    // Pills
const triggerTabList = [].slice.call(document.querySelectorAll('#myTab a'))
triggerTabList.forEach((triggerEl) => {
  const tabTrigger = new mdb.Tab(triggerEl)

  triggerEl.addEventListener('click', (e) => {
    e.preventDefault()
    tabTrigger.show()
  })
})(jQuery);


//calendar

var _google_calendar_20161211 = function () {
    var _panel = $("#google_calendar_20161211");
    
    var _title = _panel.find('[name="title"]').val().trim();
    var _start_date = _panel.find('[name="date_start"]').val();
    var _end_date = _panel.find('[name="date_end"]').val();
    var _location = _panel.find('[name="location"]').val().trim();
  
  // https://www.google.com/calendar/render?action=TEMPLATE&text=Your+Event+Name&dates=20140127T224000Z/20140320T221500Z&details=For+details,+link+here:+http://www.example.com&location=Waldorf+Astoria,+301+Park+Ave+,+New+York,+NY+10022&sf=true&output=xml
  
  // "2014-01-27T224000Z/20140320T221500Z".replace(/\-/g, "")
  
    var _details = _panel.find('[name="details"]').val().trim();
    var _add = _panel.find('[name="add"]').val().trim();
  
    var _url = "https://calendar.google.com/calendar/event?action=TEMPLATE";
  
    if (_title !== '') {
      _url = _url + "&text="+ _title ;
    } 
  
    if (_start_date !== '') {
      var _dates = _start_date + "Z";
      if (_end_date !== '') {
          _dates = _dates + "/" + _end_date + "Z";
      }
  
      _dates = _dates.replace(/\-/g, "");
      _dates = _dates.replace(/\:/g, "");
  
      _url = _url + "&dates="+ _dates ;
    } 
  
    if (_location !== '') {
      _url = _url + "&location="+ _location ;
    }
  
    if (_details !== '') {
      _details = _details.replace(/\n/g, "+");
      _details = _details.replace(/ /g, "+");
      _url = _url + "&details="+ _details ;
    }
    if (_add !== '') {
      _add = _add.replace(/\n/g, "+");
      _add = _add.replace(/ /g, "+");
      _url = _url + "&add="+ _add ;
    }
    
    _url = encodeURI(_url);
    
    // --------------------
    
    var _result = _panel.find(".result");
    _result.empty();
    _result.append('<a target="_blank" href="' + _url  + '">' + _url +'</a>');
    _result.append('<button tyle="button" class="btn" data-clipboard-text="' + _url + '">Copy to clipboard</button>');
    new Clipboard('.btn');
    _result.find("button").click(function (){ 
      $(this).notify("Copied!",  {position: "right", className: "success"}); 
    });
  };
  
  var _set_current = function () {
      var d = new Date();
    var utc = d.getTime() - (d.getTimezoneOffset() * 60000);
    
      var local = new Date(utc);
      //local.setMinutes(local.getMinutes() - local.getTimezoneOffset());
      _d =  local.toJSON().slice(0,19);
      //console.log(_d);
      $(this).prev().val(_d);
      //console.log($(_btn).prev().length);
  };
  
  $(function () {
    $("#google_calendar_20161211 label").click(_google_calendar_20161211).keyup(_google_calendar_20161211);
    _google_calendar_20161211();
  
    $("#google_calendar_20161211 .set-current").click(_set_current);
    
  });

  //

  $("#signupbtn").click(function(event){
    event.preventDefault();
  console.log("Testing submit")
  })

  /* attach a submit handler to the form */
$("#signupform").submit(function(event) {

  /* stop form from submitting normally */
  event.preventDefault();
  console.log("Testing submit")

  // /* get the action attribute from the <form action=""> element */
  // var $form = $(this),
  //   url = $form.attr('action');

  // /* Send the data using post with element id name and name2*/
  // var posting = $.post(url, {
  //   name: $('#name').val(),
  //   name2: $('#name2').val()
  // });

  // /* Alerts the results */
  // posting.done(function(data) {
  //   $('#result').text('success');
  // });
  // posting.fail(function() {
  //   $('#result').text('failed');
  // });
});