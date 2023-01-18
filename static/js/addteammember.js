function dropdown() {
  return {
    options: [],
    selected: [],
    show: false,
    open() {
      this.show = true;
    },
    close() {
      this.show = false;
    },
    isOpen() {
      return this.show === true;
    },
    select(index, event) {
      if (!this.options[index].selected) {
        this.options[index].selected = true;
        this.options[index].element = event.target;
        this.selected.push(index);
      } else {
        this.selected.splice(this.selected.lastIndexOf(index), 1);
        this.options[index].selected = false;
      }
    },
    remove(index, option) {
      this.options[option].selected = false;
      this.selected.splice(index, 1);
    },
    loadOptions() {
      const options = document.getElementById("select").options;
      for (let i = 0; i < options.length; i++) {
        this.options.push({
          value: options[i].value,
          text: options[i].innerText,
          selected:
            options[i].getAttribute("selected") != null
              ? options[i].getAttribute("selected")
              : false,
        });
      }
    },
    selectedValues() {
      return this.selected.map((option) => {
        return this.options[option].value;
      });
    },
  };
}
// The DOM element you wish to replace with Tagify
var input = document.querySelector('input[name=basic]');

// initialize Tagify on the above input node reference
new Tagify(input)
tinymce.init({
  selector: 'textarea',
  plugins: 'anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss',
  toolbar: 'undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat',
  tinycomments_mode: 'embedded',
  tinycomments_author: 'Author name',
  mergetags_list: [
    { value: 'First.Name', title: 'First Name' },
    { value: 'Email', title: 'Email' },
  ],
  // content_css : '../static/css/texteditor.css'
  content_style: 'div { margin: 10px; border: 5px solid red; padding: 3px; } ' +
    '.blue { color: blue; } .red { color: red; }'
});