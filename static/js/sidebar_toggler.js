let sidebarToggler = document.querySelector('.sidebar-toggler');

let flag = true

sidebarToggler.addEventListener('click', ()=>{
    console.log("Side bar clicked")
    flag = flag === false ? true:false;
    if(flag===true){
        console.log("True");
        document.querySelector('.content-wrapper').style.marginLeft = "17%";
        document.querySelector('.page-sidebar').style.width = "230px";

    }
    else{
        console.log("False");
        document.querySelector('.content-wrapper').style.marginLeft = "0%";
    }
})