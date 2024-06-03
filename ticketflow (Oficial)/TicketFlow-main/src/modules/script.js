function voltar() {
  // Altere a URL para a página desejada
  window.location.href = '../options/index.html';
}

function formatarTelefone(input) {
  let telefone = input.value.replace(/\D/g, "");

  if (telefone.length >= 2) {
    telefone = telefone.replace(/^(\d{2})(\d)/, "($1) $2");
  }
  if (telefone.length >= 7) {
    telefone = telefone.replace(/^(.{4})(\d)/, "$1 $2");
  }
  if (telefone.length >= 11) {
    telefone = telefone.replace(/^(.{10})(\d)/, "$1-$2");
  }

  input.value = telefone;
}

function formatarHora(input) {
  let hora = input.value.replace(/\D/g, "");

  if (hora.length >= 3) {
    hora = hora.replace(/^(\d{2})(\d)/, "$1:$2");
  }

  input.value = hora;
}

function enviar() {
  alert("enviado!")
  // Limpa todas as informações do formulário
  document.querySelector('.chamado-form').reset();
}