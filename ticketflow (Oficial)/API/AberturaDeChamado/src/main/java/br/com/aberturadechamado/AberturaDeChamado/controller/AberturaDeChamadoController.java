package br.com.aberturadechamado.AberturaDeChamado.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.aberturadechamado.AberturaDeChamado.model.AberturaDeChamado;
import br.com.aberturadechamado.AberturaDeChamado.repository.IAberturaDeChamado;

@RestController
@CrossOrigin("*")
@RequestMapping("/suporte")
public class AberturaDeChamadoController{
	
	@Autowired
	private IAberturaDeChamado dao;	
	
	@GetMapping
	public ResponseEntity<List<AberturaDeChamado>> listaChamados() {
		List<AberturaDeChamado> lista=  dao.findAll();
		 return ResponseEntity.status(200).body(lista);
	}
	
	@PostMapping
	public ResponseEntity <AberturaDeChamado> cadastrarChamado (@RequestBody AberturaDeChamado cadsolicitacao) {
		AberturaDeChamado novoChamado = dao.save(cadsolicitacao);
		return ResponseEntity.status(201).body(novoChamado);
	}
}