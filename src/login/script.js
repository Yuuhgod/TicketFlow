// Função para formatar o CNPJ
function formatarCNPJ(input) {
  // Remove caracteres não numéricos do valor do input
  let cnpj = input.value.replace(/\D/g, "")

  // Aplica a formatação do CNPJ conforme a quantidade de dígitos
  if (cnpj.length >= 2) {
    cnpj = cnpj.replace(/^(\d{2})(\d)/, "$1.$2")
  }
  if (cnpj.length >= 6) {
    cnpj = cnpj.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3")
  }
  if (cnpj.length >= 9) {
    cnpj = cnpj.replace(/^(\d{2})\.(\d{3})\.(\d{3})(\d)/, "$1.$2.$3/$4")
  }
  if (cnpj.length >= 13) {
    cnpj = cnpj.replace(
      /^(\d{2})\.(\d{3})\.(\d{3})\/(\d{4})(\d)/,
      "$1.$2.$3/$4-$5"
    )
  }

  // Atualiza o valor do input com o CNPJ formatado
  input.value = cnpj
}

// Função para enviar o formulário
function enviar() {
  // Obtém o elemento do input de CNPJ
  var cnpjInput = document.getElementById("cnpj")

  // Obtém o valor do CNPJ
  var cnpj = cnpjInput.value

  // Verifica se o CNPJ começa com "1"
  if (cnpj.startsWith("1")) {
    // Redireciona para a página de opções se o CNPJ começa com "1"
    window.location.href = "../options/index.html"
  } else {
    // // Exibe mensagem de erro se o CNPJ não começa com "1"
    alert(
      "Desculpe, não conseguimos encontrar o CNPJ na nossa base de dados. Por favor, verifique o número digitado e tente novamente."
    )
  }
}
