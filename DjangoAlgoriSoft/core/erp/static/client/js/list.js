var tblClient
function getData() {
  // para guardar el datatable en una variable y ejecutar una funcion que ya tiene para recargar los datos de la tabla
  tblClient=$("#data").DataTable({
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: "POST",
      data: {
        action: "searchdata",
      },
      dataSrc: "",
    },
    columns: [
      { data: "id" },
      { data: "names" },
      { data: "surnames" },
      { data: "dni" },
      { data: "date_birthday" },
      { data: "gender" },
      { data: "id" },
    ],
    columnDefs: [
      {
        targets: [-1],
        class: "text-center",
        orderable: false,
        render: function (data, type, row) {
          var buttons =
            '<a href="#" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
          buttons +=
            '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {},
  });
}
$(function () {
  getData(); // para traer los datos
  
  $('#btnAdd').on('click', function () {
    $('input[name="action').val('add'); // para que la accion sea crear, porque cuando se haga el editar, va a cambiar su valor (value)
    $('form')[0].reset() // selecciono los formulario, solo hay uno pero se guardan como arreglo, selecciono el primero y unico ([0]) y aplico el reset para que cada vez que se abra el modal, el formulario se limpie
    $("#myModalClient").modal("show");
  })
  
  $("form").on("submit", function (e) {
    e.preventDefault();
    var parameters = new FormData(this);
    submit_with_ajax(
      window.location.pathname,
      "Guardar",
      `¿Desea guardar el cliente?`,
      parameters,
      function () {
        $("#myModalClient").modal("hide");
        tblClient.ajax.reload() // esta es una funcion de datatable, para no recargar toda la pagina
    });
  });
});