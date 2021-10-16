// 1) Scroll Navigation
var aTags = document.querySelectorAll("header a");
for(var i = 0; i < aTags.length; i ++) {
    aTags[i].onclick = function(e) {
        e.preventDefault();
        var target = document.querySelector(this.getAttribute("href"));

        window.scrollTo({
            'behavior': 'smooth',
            'top': target.offsetTop
        })
    }
}

// $("header a").click(function(e) {
//     e.preventDefault();

//     var $target = $(this.hash);
//     // console.log($target);

//     $("html, body").animate({
//         scrollTop: $target.offset().top
//     }, "slow");
// })

var slider = document.querySelector("#slider");
var slides = slider.querySelector(".slides");
var slide = slides.querySelectorAll(".slide");

var currentSlide = 0;

setInterval(function() {
    var from = -(1024 * currentSlide);
    var to = from - 1024;
    slides.animate({
        marginLeft: [from + "px", to + "px"]
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    currentSlide++;
    if (currentSlide === (slide.length - 1)) {
        currentSlide = 0;
    }
}, 3000);

// var $slider = $("#slider");
// var $slides = $slider.find(".slides");
// var $slide = $slides.find(".slide");

// var currentSlide = 1;

// setInterval(function() {
//     $slides.animate({"margin-left" : "-=" + 1024}, 1000, function() {
//         currentSlide++;
//         if(currentSlide === $slide.length) {
//             currentSlide = 1;
//             $slides.css("margin-left", 0)
//         }
//     })
// }, 3000)


var links = document.querySelectorAll(".tabs-list li a")
var items = document.querySelectorAll(".tabs-list li")
for (var i = 0; i < links.length; i++) {
    links[i].onclick = function(e) {
        e.preventDefault();
    }
}

for (var i = 0; i < items.length; i++) {
    items[i].onclick = function() {
        var tabId = this.querySelector("a").getAttribute("href") ;
        console.log(this.classList);
        document.querySelectorAll(".tabs-list li, .tabs div.tab").forEach(function(item) {
            item.classList.remove("active");
            console.log(item);
        });
        document.querySelector(tabId).classList.add("active"); //href에 들어있는 아이디값 을 셀렉터로 찾아가 추가. 
        this.classList.add("active");
    }  
} 

// $(".tabs-list li a").click(function(e) {
//     e.preventDefault();
// });

// $(".tabs-list li").click(function() {
//     var $tabId = $(this).find("a").attr("href");

//     $(".tabs-list li, .tabs div.tab").removeClass("active");

//     $($tabId).addClass("active");
//     $(this).addClass("active");
// })

// 4) Click Image Slider
document.querySelector(".right-arrow").onclick = function () {
    var currentSlide = document.querySelector("#photo .slide.active");
    var nextSlide = currentSlide.nextElementSibling;
    if (nextSlide === null) {
        nextSlide = currentSlide.parentElement.firstElementChild;
    }
        currentSlide.animate({
        opacity: [1, 0]
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    currentSlide.classList.remove("active");
    nextSlide.animate({
        opacity: [0, 1]
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    nextSlide.classList.add("active");
}

//왼쪽 이미지 슬라이드 기능 구현
document.querySelector(".left-arrow").onclick = function () {
    var currentSlide = document.querySelector("#photo .slide.active");
    var nextSlide = currentSlide.previousElementSibling;
    if (nextSlide === null) {
        nextSlide = currentSlide.parentElement.lastElementChild;
    }
        currentSlide.animate({
        opacity: [1, 0]  // 투명도
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    currentSlide.classList.remove("active");
    nextSlide.animate({
        opacity: [0, 1]
    }, {
        duration: 500,
        easing: "ease",
        iterations: 1,
        fill: "both"
    });
    nextSlide.classList.add("active");
}

// $(".right-arrow").click(function() {
//     var $curSlide = $("#photo .slide.active");
//     var $nextSlide = $curSlide.next();

//     $curSlide.fadeOut().removeClass("active");
//     $nextSlide.fadeIn().addClass("active");

//     if( $nextSlide.length === 0){
//         $("#photo .slide").first().fadeIn().addClass("active");
//     }
// })
// $(".left-arrow").click(function() {
//     var $curSlide = $("#photo .slide.active");
//     var $prevSlide = $curSlide.prev();

//     $curSlide.fadeOut().removeClass("active");
//     $prevSlide.fadeIn().addClass("active");

//     if( $prevSlide.length === 0){
//         $("#photo .slide").last().fadeIn().addClass("active");
//     }
// })


// $(function() {
//     $("header a").click(function(e) {
//         e.preventDefault();

//         var $target = $(this.hash);
//         // console.log($target);
        
//         $("html, body").animate({ scrollTop: $target.offset().top }, "slow");
//     })

//     // 2
//     var $slider = $("#slider");
//     var $slides = $slider.find(".slides");
//     var $slide = $slides.find(".slide");

//     var currentSlide = 1;

//     setInterval(function() {
//         $slides.animate({"margin-left" : "-=" + 1024}, 1000, function() {
//             currentSlide++;
//             if(currentSlide === $slide.length) {
//                 currentSlide = 1;
//                 $slides.css("margin-left", 0)
//             }
//         })
//     }, 3000)

//     // 3
//     $(".tabs-list li a").click(function(e) {
//         e.preventDefault();
//     });

//     $(".tabs-list li").click(function() {
//         var $tabId = $(this).find("a").attr("href");

//         $(".tabs-list li, .tabs div.tab").removeClass("active");

//         $($tabId).addClass("active");
//         $(this).addClass("active");
//     })

//     // 4
//     $(".right-arrow").click(function() {
//         var $curSlide = $("#photo .slide.active");
//         var $nextSlide = $curSlide.next();

//         $curSlide.fadeOut().removeClass("active");
//         $nextSlide.fadeIn().addClass("active");

//         if( $nextSlide.length === 0){
//             $("#photo .slide").first().fadeIn().addClass("active");
//         }
//     })
//     $(".left-arrow").click(function() {
//         var $curSlide = $("#photo .slide.active");
//         var $prevSlide = $curSlide.prev();

//         $curSlide.fadeOut().removeClass("active");
//         $prevSlide.fadeIn().addClass("active");

//         if( $prevSlide.length === 0){
//             $("#photo .slide").last().fadeIn().addClass("active");
//         }
//     })
// });
