-- Adminer 4.8.1 MySQL 11.3.2-MariaDB-1:11.3.2+maria~ubu2204 dump

SET NAMES utf8;
SET time_zone = '-03:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

-- -----------------------------------------------------
-- Database db
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `db-flask` DEFAULT CHARACTER SET utf8 ;
USE `db-flask`;

-- -----------------------------------------------------
-- Tabela db.usuario
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT 'Não Informado',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- -----------------------------------------------------
-- Tabela db.produto
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `produto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuarioId` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT 'Não Informado',
  PRIMARY KEY (`id`),
  KEY `fk_produto_usuario` (`usuarioId`),
  CONSTRAINT `fk_produto_usuario` FOREIGN KEY (`usuarioId`) REFERENCES `usuario` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;