const btn = document.querySelector(".user_image");

if(btn){
    btn.addEventListener("click",function(e){
        form = document.querySelector(".changeimg");
        form.classList.add('changeimg-active');
    })
}

const closed = document.querySelector(".close")
if(closed){
    closed.addEventListener("click",function (e) {
        form = document.querySelector(".changeimg");
        form.classList.remove('changeimg-active');
    })
}

const closess = document.querySelector(".closes")
if(closess){
    closess.addEventListener("click",function(e){
        block = document.querySelector(".active");
        block.classList.add("closing");
    })
}

function droch() {
    block = document.querySelector(".active");
    block.classList.add("closing");
}