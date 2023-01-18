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
var input = document.querySelector("input[name=basic]");
// initialize Tagify on the above input node reference
const tagify1 = new Tagify(input);

var input2 = document.querySelector("input[name=groupsortags]");
const tagify2 = new Tagify(input2);

tinymce.init({
  selector: "textarea",
  plugins:
    "anchor autolink charmap codesample emoticons image link lists media searchreplace table visualblocks wordcount checklist mediaembed casechange export formatpainter pageembed linkchecker a11ychecker tinymcespellchecker permanentpen powerpaste advtable advcode editimage tinycomments tableofcontents footnotes mergetags autocorrect typography inlinecss",
  toolbar:
    "undo redo | blocks fontfamily fontsize | bold italic underline strikethrough | link image media table mergetags | addcomment showcomments | spellcheckdialog a11ycheck typography | align lineheight | checklist numlist bullist indent outdent | emoticons charmap | removeformat",
  tinycomments_mode: "embedded",
  tinycomments_author: "Author name",
  mergetags_list: [
    { value: "First.Name", title: "First Name" },
    { value: "Email", title: "Email" },
  ],
  // content_css : '../static/css/texteditor.css'
  content_style:
    "div { margin: 10px; border: 5px solid red; padding: 3px; } " +
    ".blue { color: blue; } .red { color: red; }",
});

$(function () {
  $("#dropzone").on("dragover", function () {
    $(this).addClass("hover");
  });

  $("#dropzone").on("dragleave", function () {
    $(this).removeClass("hover");
  });

  $("#dropzone input").on("change", function (e) {
    var file = this.files[0];

    $("#dropzone").removeClass("hover");

    if (this.accept && $.inArray(file.type, this.accept.split(/, ?/)) == -1) {
      return alert("File type not allowed.");
    }

    $("#dropzone").addClass("dropped");
    $("#dropzone img").remove();

    if (/^image\/(gif|png|jpeg)$/i.test(file.type)) {
      var reader = new FileReader(file);

      reader.readAsDataURL(file);

      reader.onload = function (e) {
        var data = e.target.result,
          $img = $("<img />").attr("src", data).fadeIn();

        $("#dropzone div").html($img);
      };
    } else {
      var ext = file.name.split(".").pop();

      $("#dropzone div").html(ext);
    }
  });

  // ----------------------------------------------------
  $("#dropzone-athlete").on("dragover", function () {
    $(this).addClass("hover");
  });

  $("#dropzone-athlete").on("dragleave", function () {
    $(this).removeClass("hover");
  });

  $("#dropzone-athlete input").on("change", function (e) {
    var file = this.files[0];

    $("#dropzone-athlete").removeClass("hover");

    if (this.accept && $.inArray(file.type, this.accept.split(/, ?/)) == -1) {
      return alert("File type not allowed.");
    }

    $("#dropzone-athlete").addClass("dropped");
    $("#dropzone-athlete img").remove();

    if (/^image\/(gif|png|jpeg)$/i.test(file.type)) {
      var reader = new FileReader(file);

      reader.readAsDataURL(file);

      reader.onload = function (e) {
        var data = e.target.result,
          $img = $("<img />").attr("src", data).fadeIn();

        $("#dropzone-athlete div").html($img);
      };
    } else {
      var ext = file.name.split(".").pop();

      $("#dropzone-athlete div").html(ext);
    }
  });

  // ----------------------------------------------------
  $("#dropzone-doc").on("dragover", function () {
    $(this).addClass("hover");
  });

  $("#dropzone-doc").on("dragleave", function () {
    $(this).removeClass("hover");
  });

  $("#dropzone-doc input").on("change", function (e) {
    var file = this.files[0];

    $("#dropzone-doc").removeClass("hover");

    if (this.accept && $.inArray(file.type, this.accept.split(/, ?/)) == -1) {
      return alert("File type not allowed.");
    }

    $("#dropzone-doc").addClass("dropped");
    $("#dropzone-doc img").remove();

    if (/^image\/(gif|png|jpeg)$/i.test(file.type)) {
      var reader = new FileReader(file);

      reader.readAsDataURL(file);

      reader.onload = function (e) {
        var data = e.target.result,
          $img = $("<img />").attr("src", data).fadeIn();

        $("#dropzone-doc div").html($img);
      };
    } else {
      var ext = file.name.split(".").pop();

      $("#dropzone-doc div").html(ext);
    }
  });
});
