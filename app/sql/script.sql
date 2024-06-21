-- Adminer 4.8.1 MySQL 11.3.2-MariaDB-1:11.3.2+maria~ubu2204 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

-- -----------------------------------------------------
-- Database db
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `db` DEFAULT CHARACTER SET utf8 ;
USE `db`;

-- -----------------------------------------------------
-- Tabela db.categoria
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT 'Sem nome',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- -----------------------------------------------------
-- Tabela db.mercadoria
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mercadoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `categoriaId` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT 'Sem nome',
  `valor` int(6) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `fk_mercadoria_categoria` (`categoriaId`),
  CONSTRAINT `fk_mercadoria_categoria` FOREIGN KEY (`categoriaId`) REFERENCES `categoria` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;