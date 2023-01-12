let options = {
    startAngle: -1.55,
    size: 100,
    value: 0.89,
    fill: {gradient: ['#fff', '#fff']}
  }
  $(".circle .bar").circleProgress(options).on('circle-animation-progress',
  function(event, progress, stepValue){
    $(this).parent().find("span").text(String(stepValue.toFixed(2).substr(2)) + "%");
  });
  $(".grade .bar").circleProgress({
    value: 0.70,
    fill: {gradient: ['#00FFFF', '#00FFFF']}
  });
  $(".technique .bar").circleProgress({
    value: 0.90,
    fill: {gradient: ['#C0C0C0', '#C0C0C0']}
  });      
//   $(".react .bar").circleProgress({
//     value: 0.60
//   });

function toggleModal(modalID){
  document.getElementById(modalID).classList.toggle("hidden");
  document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
  document.getElementById(modalID).classList.toggle("flex");
  document.getElementById(modalID + "-backdrop").classList.toggle("flex");
}
// toggleModal("modal-id");