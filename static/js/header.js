document.querySelectorAll(".msg-hover").forEach(function(event){
    event.addEventListener("mouseover",function(){
        this.querySelector("div .box-in-out").classList.toggle("hidden");
    });
    event.addEventListener("mouseout",function(){
        this.querySelector("div .box-in-out").classList.toggle("hidden");
    })
})