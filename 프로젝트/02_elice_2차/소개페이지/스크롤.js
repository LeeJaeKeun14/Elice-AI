var firstTextOffsetTop = document.querySelector(".fade_out").offsetTop; // 첫 번째 p 요소의 offsetTop 값
// console.log(firstTextOffsetTop);
// 516
window.onscroll = function() { // 윈도우 스크롤이 발생하면 실행..
  console.log(window.pageYOffset);
  
  var threshold = firstTextOffsetTop - 450
  console.log(threshold * 1.2);
  if (window.pageYOffset > threshold) { // 이미지가 전부 보이는것 보다 일찍 페이트 아웃 시작
    var fade_out = ((window.pageYOffset - threshold * 1.2) / (firstTextOffsetTop - threshold * 1.2)); // 
    var fade_in = ((firstTextOffsetTop - threshold * 1.5) / (window.pageYOffset - threshold * 1.2));  

    console.log(fade_out);
    console.log(fade_in);
    // 선형 그라디언트로 rgba 를 적용, 그라디언트 위에서 아래가 기본값으로 방향 생략함, 텍스트가 있는 영역에 가까울수록 opacity 증가. 즉, 1이 될때까지...
    console.log(document.getElementsByClassName("fade_out")[0].style.backgroundColor);
    if (fade_out < 0.55){
        document.getElementsByClassName("fade_out")[0].style.background = "linear-gradient(rgba(50, 50, 50, " + fade_out + "), rgba(50, 50, 50, " + fade_out + ")), url(./img/코로나_지도_2020.png) no-repeat";
    } else {
        document.getElementsByClassName("fade_out")[0].style.background = "linear-gradient(rgba(50, 50, 50, " + fade_in + "), rgba(50, 50, 50, " + fade_in + ")), url(./img/코로나_지도_2021.png) no-repeat";
    }
  }
}
