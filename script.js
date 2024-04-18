let currentImageIndex = 0;
const images = ['fiction1.jpg','fiction2.jpg','fiction3.jpg','history3.png'];

function prevImage() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateImage();
}

function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateImage();
}

function updateImage(){
    const sliderImage = document.getElementById('slider-image');
    sliderImage.src = images[currentImageIndex];
}