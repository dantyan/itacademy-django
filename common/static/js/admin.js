django.jQuery(function () {
    ClassicEditor
        .create(document.querySelector('#id_content'), {
            // toolbar: [ 'heading', '|', 'bold', 'italic', 'link' ]
        })
        .then(editor => {
            window.editor = editor;
        })
        .catch(err => {
            console.error(err.stack);
        });

});
