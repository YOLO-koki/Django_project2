const nav_elements = document.querySelectorAll('.nav_element');

for(const nav_element of nav_elements){
    nav_element.addEventListener("click", function(e) {
        // e.preventDefault();
        for(let i = 0; i <nav_elements.length; i++){
            nav_elements[i].classList.remove("current");
        }
        console.log('current');
        nav_element.classList.add("current");
    });
}