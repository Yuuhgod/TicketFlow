package br.com.aberturadechamado.AberturaDeChamado.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "cadsolicitacao")
public class AberturaDeChamado {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(name = "ordemsolicitacao")
	private Integer ordemsolicitacao;
	
	@Column(name = "data", nullable = true)
	private String data;
	
	@Column(name = "solicitante", length = 30, nullable = true)
	private String solicitante;

	@Column(name = "codigoparceiro", length = 8, nullable = true )
	private String codigoparceiro;
	
	@Column(name = "descricao", length = 40, nullable = true)
	private String descricao;
	
	@Column(name = "situacao", length = 20, nullable = true)
	private String situacao;
	
	@Column(name = "situacaosuporte", length = 20, nullable = true)
	private String situacaosuporte;
	
	@Column(name = "correcaosuporte", length = 300, nullable = true)
	private String correcaosuporte;
	
	@Column(name = "sistema", length = 10, nullable = true)
	private String sistema;
	
	@Column(name = "email", length = 100, nullable = true)
	private String email;
	
	@Column(name = "cnpj", length = 14, nullable = true)
	private String cnpj;

	

	public Integer getOrdemsolicitacao() {
		return ordemsolicitacao;
	}

	public void setOrdemsolicitacao(Integer ordemsolicitacao) {
		this.ordemsolicitacao = ordemsolicitacao;
	}

	public String getData() {
		return data;
	}

	public void setData(String data) {
		this.data = data;
	}

	public String getSolicitante() {
		return solicitante;
	}

	public void setSolicitante(String solicitante) {
		this.solicitante = solicitante;
	}

	public String getCodigoparceiro() {
		return codigoparceiro;
	}

	public void setCodigoparceiro(String codigoparceiro) {
		this.codigoparceiro = codigoparceiro;
	}

	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public String getSituacao() {
		return situacao;
	}

	public void setSituacao(String situacao) {
		this.situacao = situacao;
	}

	public String getSituacaosuporte() {
		return situacaosuporte;
	}

	public void setSituacaosuporte(String situacaosuporte) {
		this.situacaosuporte = situacaosuporte;
	}

	public String getCorrecaosuporte() {
		return correcaosuporte;
	}

	public void setCorrecaosuprote(String correcaosuporte) {
		this.correcaosuporte = correcaosuporte;
	}
	
	public String getSistema() {
		return sistema;
	}

	public void setSistema(String sistema) {
		this.sistema = sistema;
	}
	
	public void setCorrecaosuporte(String correcaosuporte) {
		this.correcaosuporte = correcaosuporte;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getCnpj() {
		return cnpj;
	}

	public void setCnpj(String cnpj) {
		this.cnpj = cnpj;
	}

	
}
