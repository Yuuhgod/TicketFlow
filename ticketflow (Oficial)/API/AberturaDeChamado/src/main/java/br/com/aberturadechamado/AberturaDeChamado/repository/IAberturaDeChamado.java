package br.com.aberturadechamado.AberturaDeChamado.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;

import br.com.aberturadechamado.AberturaDeChamado.model.AberturaDeChamado;

public interface IAberturaDeChamado extends JpaRepository<AberturaDeChamado, Integer>{

}
