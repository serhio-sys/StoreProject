const closed = document.querySelector(".form-activator")
if(closed){
    closed.addEventListener("click",function (e) {
        form = document.querySelector(".form-filtr");
        form.classList.toggle('filtr-active');
        if (form.classList.contains('filtr-active')){
            document.querySelector('.form-activator').innerHTML = '<';
            document.querySelector('body').style.overflow="hidden";
        }
        else{
            document.querySelector('.form-activator').innerHTML = '>';
            document.querySelector('body').style.overflow="visible";
        }
    })
}
