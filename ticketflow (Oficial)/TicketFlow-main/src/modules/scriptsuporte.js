
const formulario = document.querySelector("form");
const Isuporte_solicitante = document.querySelector(".suporte_solicitante");
const Isuporte_telefone = document.querySelector(".suporte_telefone"); 
const Isuporte_sistema = document.querySelector(".suporte_sistema");
const Isuporte_email = document.querySelector(".suporte_email");
const Isuporte_cnpj = document.querySelector(".suporte_cnpj");
const Isuporte_horario = document.querySelector(".suporte_horario");
const Isuporte_descricao = document.querySelector(".suporte_descricao");



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

// Função para formatar o CNPJ
function formatarCNPJ(input) {
  // Remove caracteres não numéricos do valor do input
  let cnpj = input.value.replace(/\D/g, "");

  // Atualiza o valor do input com o CNPJ formatado
  input.value = cnpj;
}




function cadastrar() {
  let dataAtual = new Date().toISOString().slice(0, 10); // Formato YYYY-MM-DD
  console.log("Data Atual:", dataAtual);
  console.log("Solicitante:", Isuporte_solicitante.value);
  console.log("Telefone:", Isuporte_telefone.value);
  console.log("Sistema:", Isuporte_sistema.value);
  console.log("E-mail:", Isuporte_email.value);
  console.log("Cnpj:", Isuporte_cnpj.value);
  console.log("Horário:", Isuporte_horario.value);
  console.log("Descrição:", Isuporte_descricao.value);

  fetch("http://localhost:8080/suporte", {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: "POST",
    body: JSON.stringify({
      solicitante: Isuporte_solicitante.value,
      telefone: Isuporte_telefone.value, // Adicionado campo telefone
      sistema: Isuporte_sistema.value,
      email: Isuporte_email.value,
      cnpj: Isuporte_cnpj.value,
      horario: Isuporte_horario.value, // Adicionado campo horário
      descricao: Isuporte_descricao.value,
      codigoparceiro: "00000003",
      situacao: "Suporte",
      situacaosuporte: "Pendente Suporte",
      data: dataAtual // Alterado para usar a data atual
    })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Problema na resposta do servidor');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    alert("Dados enviados com sucesso!");
    document.querySelector('.chamado-form').reset();
    // window.location.href = "../options/index.html";
  })
  .catch(error => {
    console.error('Falha ao enviar dados:', error);
  });
}

function limpar() {
  alert("Dados enviados com sucesso!");
  // Limpa todas as informações do formulário
  document.querySelector('.chamado-form').reset();
   //window.location.href = "../options/index.html";
};