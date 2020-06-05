var actualizarBtns = document.getElementsByClassName("actualizar-carro");

for (var i = 0; i < actualizarBtns.length; i++) {
  actualizarBtns[i].addEventListener("click", function () {
    var idProducto = this.dataset.producto;
    var accion = this.dataset.accion;
    console.log(
      "id producto:",
      idProducto,
      "accion:",
      accion,
      "usuariox",
      usuario
    );

    if (usuario == "AnonymousUser") {
      console.log("usuario anónimo");
    } else {
      actualizarOrdenUsuario(idProducto, accion);
      // console.log("accion:", accion);
    }
  });
}

function actualizarOrdenUsuario(idProducto, accion) {
  console.log("funcion actualizarOrdenUsuario...");

  var url = "/actualizar_producto/";

  console.log(JSON.stringify({ idProducto: idProducto, accion: accion }));

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ idProducto: idProducto, accion: accion }),
  })
    .then((response) => {
      console.log("RESPUESTA:", response);
      return response.json();
    })

    .then((data) => {
      console.log("dataaa:", data);
      location.reload();
    });
}
