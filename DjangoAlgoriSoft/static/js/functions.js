function message_error(obj) {
  var html = "";
  if (typeof obj === "object") {
    //si es un objeto, lo itero
    html = '<ul style="text-align: Left; ">';
    $.each(obj, function (key, value) {
      html += "<li>" + key + ": " + value + "</li>";
    });
    html += "</ul>";
  } else {
    //sino, puede ser un string, solo se lo paso
    html = "<p>" + obj + "</p>";
  }

  Swal.fire({
    title: "¡Error!",
    //ya no le paso un "text", sino un "html" porque construi uno para los errores
    html: html,
    icon: "error",
  });
}
