const allbtns = document.querySelector(".btns")
if(allbtns){
    allbtns.addEventListener("click",function(e){
        const targ = e.target;
        if (targ.classList.contains("reg") || targ.classList.contains("log")){
            btn = document.querySelector(".reg")
            form = document.querySelector(".form-reg")
            btn.classList.toggle("btn-active")
            form.classList.toggle("form_active")
            btn_no = document.querySelector(".log")
            form_no = document.querySelector(".form-log")
            btn_no.classList.toggle("btn-active")
            form_no.classList.toggle("form_active")
        }
    })
}

const labels = document.querySelectorAll(".form_part .form-label");

labels.forEach((label)=>{
    label.innerHTML = label.innerText
    .split("")
    .map(
        (letter,idx) => 
            `<span style="transition-deley:${idx * 50}ms">${letter}</span>`
    )
    .join("");
});