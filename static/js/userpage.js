content_home = document.querySelector(".content-home")
content_profile = document.querySelector(".content-profile")
content_delivery = document.querySelector(".content-delivery")

contents = [content_home, content_profile, content_delivery]
contents.forEach(element => {
    if (element != content_home) { 
        element.style.display = "none"
    }
});

function home(){
    contents.forEach(element => {
        element.style.display = "none"
    });
    content_home.style.display = "block"
}

function profile(){
    contents.forEach(element => {
        element.style.display = "none"
    });
    content_profile.style.display = "block"
}

function delivery(){
    contents.forEach(element => {
        element.style.display = "none"
    });
    content_delivery.style.display = "block"
}
