import Cropper from 'cropperjs';
import 'cropperjs/dist/cropper.min.css';

let cropper;
const imageInput = document.getElementById('id_profile_image');
const previewImage = document.getElementById('cropper-preview');
const croppedImageInput = document.getElementById('cropped_image_input');

imageInput.addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = () => {
    previewImage.src = reader.result;
    previewImage.style.display = 'block';

    if (cropper) {
      cropper.destroy();
    }

    cropper = new Cropper(previewImage, {
      aspectRatio: 1,
      viewMode: 1,
      autoCropArea: 1,
      cropend: function () {
        const canvas = cropper.getCroppedCanvas({
          width: 300,
          height: 300
        });
        canvas.toBlob(function (blob) {
          const newFile = new File([blob], "profile.jpg", { type: "image/jpeg" });
          const dataTransfer = new DataTransfer();
          dataTransfer.items.add(newFile);
          imageInput.files = dataTransfer.files;
        });
      }
    });
  };

  reader.readAsDataURL(file);
});