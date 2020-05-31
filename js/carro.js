console.log("link a carro.js funcionando :D");

var actualizarBtns = document.getElementsByClassName("actualizar-carro");

for (var i = 0; i < actualizarBtns.length; i++) {
  actualizarBtns[i].addEventListener("click", function () {
    var idProducto = this.dataset.producto;
    var accion = this.dataset.action;
    console.log(idProducto, accion, usuario);

    if (usuario == "AnonymousUser") {
      console.log("usuario anónimo");
    } else {
      actualizarOrdenUsuario();
    }
  });
}

function actualizarOrdenUsuario(idProducto, accion) {
  console.log("usuario registrado :D!");

  var url = "/actualizar_producto/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ idProducto: idProducto, accion: accion }),
  })
    .then((response) => response.json())

    .then((data) => {
      console.log("data:", data);
    });
}
