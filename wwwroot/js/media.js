console.log("media.js loaded...");


function DownloadFile(url, fileName) {
    const link = document.getElementById("link");
    link.href = url;
    link.download = fileName; 
    link.click(); 

}

function ScrollToBottom(none)
{

    const cmdBox = document.getElementById('command_box');
        cmdBox.scrollTop = cmdBox.scrollHeight;
}
    
 
function UploadFile() {
    var fileInput = document.getElementById('file');
    var formData = new FormData();
    var filePaths = [];

    for (var i = 0; i < fileInput.files.length; i++) {
        var file = fileInput.files[i];
        filePaths.push(file.name); // Collect the file name or path
        formData.append('files', file); // Include the file in FormData if needed
        //   console.log(file.name);
    }
    //console.log(filePaths);
    // Create a comma-separated list of file names
    formData.append('filePaths', filePaths.join(','));
    alert('Files to be uploaded: ' + filePaths.join(', '));

    fetch('/upload', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => response.text())
        .then(data => {
            console.log('Success:', data);
            // alert('Files uploaded successfully!');
            // window.history.back();
        })
        .catch(error => console.error('Error:', error));
}