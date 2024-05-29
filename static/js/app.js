  function confirmarBorrado(id) {
    const respuesta = confirm("¿Estás seguro de que deseas borrar el registro?");
    if (respuesta) {
      window.location.href = `/borrar/${id}`;
    }

  }