const fileInput = document.querySelector('#file-js-example input[type=file]');
if (fileInput) {
  fileInput.onchange = () => {
    if (fileInput.files.length > 0) {
      const fileName = document.querySelector('#file-js-example .file-name');
      fileName.textContent = fileInput.files[0].name;
      
      const button = document.querySelector('#submit-button');
      button.disabled = false;
      button.onclick = () => {
        button.className += ' is-loading';
      };
    }
  }
}
