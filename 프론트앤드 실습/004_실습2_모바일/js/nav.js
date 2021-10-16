(function() {

    // 내비게이션
    $('.left').click(function(){
        $("#side_nav").animate({ left : "0"})
    })

    $('.close_btn').click(function(){
        $("#side_nav").animate({ left : "-200px"})
    })

})();