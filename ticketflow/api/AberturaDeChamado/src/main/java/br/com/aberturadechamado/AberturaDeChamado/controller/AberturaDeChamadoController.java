package br.com.aberturadechamado.AberturaDeChamado.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.aberturadechamado.AberturaDeChamado.DAO.IAberturaDeChamado;
import br.com.aberturadechamado.AberturaDeChamado.model.AberturaDeChamado;

@RestController
@CrossOrigin("*")
@RequestMapping("/suporte")
public class AberturaDeChamadoController{
	
	@Autowired
	private IAberturaDeChamado dao;	
	
	@GetMapping
	public List<AberturaDeChamado> listaChamados() {
		return (List<AberturaDeChamado>) dao.findAll();
	}
	
	@PostMapping
	public AberturaDeChamado cadastrarChamado (@RequestBody AberturaDeChamado cadsolicitacao) {
		AberturaDeChamado novoChamado = dao.save(cadsolicitacao);
		return novoChamado;
	}
}