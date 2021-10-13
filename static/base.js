const images = document.querySelectorAll(".product-img");

const lightbox = document.createElement("div");
lightbox.id = "lightbox";

images.forEach(image => {

    image.addEventListener("click", e => {

        let clicked_image = document.createElement("img");
        clicked_image.src = image.src;
        clicked_image.id = "image-showcase";

        if (lightbox.firstChild) {
            lightbox.removeChild(lightbox.firstChild)
        }

        lightbox.appendChild(clicked_image);

        document.body.appendChild(lightbox);
    });
});

lightbox.addEventListener("click", e => {
    lightbox.remove();
});
