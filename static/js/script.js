/*const nav = document.querySelector("nav"),
    toggleBtn = nav.querySelector(".toggle-btn");

    toggleBtn.addEventListener("click",() => {
        nav.classList.toggle("open");
    });
*/


 /*   function onDrag({movementY}){
        const navStyle = window.getComputedStyle(nav),
            navTop= parseInt(navStyle.Top),
            navHeight= parseInt(navStyle.height),
            windHeight=window.innerHeight;
            nav.style.top = navTop > 0 ? '${navTop + movementY}px' : "1px";
            if(navStyle > windHeight - navHeight){
                nav.style.top = '${windHeight - navHeight}px';
            }
        }

    nav.addEventListener("mousedown", () => {
        nav.addEventListener("mousemove",onDrag)
    })

    nav.addEventListener("mouseup", () => {
        nav.removeEventListener("mousemove",onDrag)
    })

    nav.addEventListener("mouseleave", () => {
        nav.removeEventListener("mousemove",onDrag)
    })
*/

function habilitar(value)
{
    if(value=="2")
    {
        // habilitamos
        document.getElementById("id_beneficio").disabled=false;
        document.getElementById("id_beneficio").style.display="inline";
        document.getElementById("pid_beneficio").style.display="inline";
    }else {
        // deshabilitamos
        document.getElementById("id_beneficio").disabled=true;
        document.getElementById("id_beneficio").style.display="none"
        document.getElementById("pid_beneficio").style.display="none"
    }
}

