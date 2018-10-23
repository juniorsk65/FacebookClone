-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Oct 23, 2018 at 04:31 AM
-- Server version: 8.0.12
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facebook`
--

-- --------------------------------------------------------

--
-- Table structure for table `Amizade`
--

CREATE TABLE `Amizade` (
  `idUsuario1` int(11) NOT NULL,
  `idUsuario2` int(11) NOT NULL,
  `bloqueio` tinyint(1) NOT NULL COMMENT 'se true, eles não podem se ver. se false, eles são amigos, se relacionamento não existe, não sao amigos \n',
  `status` tinyint(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Amizade`
--

INSERT INTO `Amizade` (`idUsuario1`, `idUsuario2`, `bloqueio`, `status`) VALUES
(1, 2, 1, 0),
(1, 3, 0, 1),
(4, 1, 0, 1),
(4, 2, 0, 1),
(4, 3, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `Grupo`
--

CREATE TABLE `Grupo` (
  `idGrupo` int(11) NOT NULL,
  `nomeGrupo` varchar(45) DEFAULT NULL,
  `descricaoGrupo` varchar(45) DEFAULT NULL,
  `foto` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Participacao`
--

CREATE TABLE `Participacao` (
  `Usuario_idUsuario` int(11) NOT NULL,
  `Grupo_idGrupo` int(11) NOT NULL,
  `Participacao` tinyint(3) DEFAULT NULL,
  `Administrador` tinyint(3) DEFAULT NULL,
  `status` tinyint(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PostagensGrupo`
--

CREATE TABLE `PostagensGrupo` (
  `idPostagem` int(255) NOT NULL,
  `Usuario_idUsuario` int(11) NOT NULL,
  `Grupo_idGrupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `PostagensUsuario`
--

CREATE TABLE `PostagensUsuario` (
  `idPostagemUsuario` int(11) NOT NULL,
  `usuarioProprietario` int(11) NOT NULL,
  `idUsuario2` int(11) NOT NULL,
  `conteudo` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Resposta`
--

CREATE TABLE `Resposta` (
  `idComentario` int(11) NOT NULL,
  `idPostagemUsuario` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `conteudo` text,
  `Reposta_idComentario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `RespostaPostagemGrupo`
--

CREATE TABLE `RespostaPostagemGrupo` (
  `RespostaUsuarioGrupo` int(11) NOT NULL,
  `PostagensGrupo_idPostagem` int(11) NOT NULL,
  `Usuario_idUsuario` int(11) NOT NULL,
  `RespostaUsuarioGrupo_RespostaUsuarioGrupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `Usuario`
--

CREATE TABLE `Usuario` (
  `idUsuario` int(11) NOT NULL,
  `nomeUsuario` varchar(255) NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `privacidade` tinyint(3) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `Usuario`
--

INSERT INTO `Usuario` (`idUsuario`, `nomeUsuario`, `cidade`, `privacidade`, `email`) VALUES
(1, 'Vinicius', 'São Paulo', 3, 'vinicius_gbapb@icloud.com'),
(2, 'Lucas', 'Fortaleza', 1, 'xX_lucas_pussy_slayer_Xx@myspace.com'),
(3, 'Luciano', 'João Pessoa', 1, 'lucino@hotmail.com'),
(4, 'Laura', 'João Pessoa', 1, 'lauuraaa@hotmail.com'),
(5, 'Cinthya', 'João Pessoa', 1, 'Cinthya@hotmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Amizade`
--
ALTER TABLE `Amizade`
  ADD PRIMARY KEY (`idUsuario1`,`idUsuario2`),
  ADD KEY `fk_Amizade_Usuario1_idx` (`idUsuario1`),
  ADD KEY `fk_Amizade_Usuario2_idx` (`idUsuario2`);

--
-- Indexes for table `Grupo`
--
ALTER TABLE `Grupo`
  ADD PRIMARY KEY (`idGrupo`);

--
-- Indexes for table `Participacao`
--
ALTER TABLE `Participacao`
  ADD PRIMARY KEY (`Usuario_idUsuario`,`Grupo_idGrupo`),
  ADD KEY `fk_Usuario_has_Grupo_Grupo1_idx` (`Grupo_idGrupo`),
  ADD KEY `fk_Usuario_has_Grupo_Usuario1_idx` (`Usuario_idUsuario`);

--
-- Indexes for table `PostagensGrupo`
--
ALTER TABLE `PostagensGrupo`
  ADD PRIMARY KEY (`idPostagem`,`Usuario_idUsuario`,`Grupo_idGrupo`),
  ADD KEY `fk_Usuario_has_Grupo_Grupo2_idx` (`Grupo_idGrupo`),
  ADD KEY `fk_Usuario_has_Grupo_Usuario2_idx` (`Usuario_idUsuario`);

--
-- Indexes for table `PostagensUsuario`
--
ALTER TABLE `PostagensUsuario`
  ADD PRIMARY KEY (`idPostagemUsuario`,`usuarioProprietario`,`idUsuario2`),
  ADD KEY `fk_PostagensUsuario_Usuario1_idx` (`usuarioProprietario`),
  ADD KEY `fk_PostagensUsuario_Usuario2_idx` (`idUsuario2`);

--
-- Indexes for table `Resposta`
--
ALTER TABLE `Resposta`
  ADD PRIMARY KEY (`idComentario`,`idPostagemUsuario`,`idUsuario`),
  ADD KEY `fk_Comentario_PostagensUsuario1_idx` (`idPostagemUsuario`),
  ADD KEY `fk_Reposta_Usuario1_idx` (`idUsuario`),
  ADD KEY `fk_Reposta_Reposta1_idx` (`Reposta_idComentario`);

--
-- Indexes for table `RespostaPostagemGrupo`
--
ALTER TABLE `RespostaPostagemGrupo`
  ADD PRIMARY KEY (`RespostaUsuarioGrupo`,`PostagensGrupo_idPostagem`,`Usuario_idUsuario`),
  ADD KEY `fk_RespostaUsuarioGrupo_PostagensGrupo1_idx` (`PostagensGrupo_idPostagem`),
  ADD KEY `fk_RespostaUsuarioGrupo_Usuario1_idx` (`Usuario_idUsuario`),
  ADD KEY `fk_RespostaUsuarioGrupo_RespostaUsuarioGrupo1_idx` (`RespostaUsuarioGrupo_RespostaUsuarioGrupo`);

--
-- Indexes for table `Usuario`
--
ALTER TABLE `Usuario`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Usuario`
--
ALTER TABLE `Usuario`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Amizade`
--
ALTER TABLE `Amizade`
  ADD CONSTRAINT `fk_Amizade_Usuario1` FOREIGN KEY (`idUsuario1`) REFERENCES `Usuario` (`idusuario`),
  ADD CONSTRAINT `fk_Amizade_Usuario2` FOREIGN KEY (`idUsuario2`) REFERENCES `Usuario` (`idusuario`);

--
-- Constraints for table `Participacao`
--
ALTER TABLE `Participacao`
  ADD CONSTRAINT `fk_Usuario_has_Grupo_Grupo1` FOREIGN KEY (`Grupo_idGrupo`) REFERENCES `Grupo` (`idgrupo`),
  ADD CONSTRAINT `fk_Usuario_has_Grupo_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `Usuario` (`idusuario`);

--
-- Constraints for table `PostagensGrupo`
--
ALTER TABLE `PostagensGrupo`
  ADD CONSTRAINT `fk_PostagensGrupo_has_Grupo` FOREIGN KEY (`Grupo_idGrupo`) REFERENCES `Grupo` (`idgrupo`),
  ADD CONSTRAINT `fk_PostagensGrupo_has_Usuario` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `Usuario` (`idusuario`);

--
-- Constraints for table `PostagensUsuario`
--
ALTER TABLE `PostagensUsuario`
  ADD CONSTRAINT `fk_PostagensUsuario_Usuario1` FOREIGN KEY (`usuarioProprietario`) REFERENCES `Usuario` (`idusuario`),
  ADD CONSTRAINT `fk_PostagensUsuario_Usuario2` FOREIGN KEY (`idUsuario2`) REFERENCES `Usuario` (`idusuario`);

--
-- Constraints for table `Resposta`
--
ALTER TABLE `Resposta`
  ADD CONSTRAINT `fk_Comentario_PostagensUsuario1` FOREIGN KEY (`idPostagemUsuario`) REFERENCES `PostagensUsuario` (`idpostagemusuario`),
  ADD CONSTRAINT `fk_Reposta_Reposta1` FOREIGN KEY (`Reposta_idComentario`) REFERENCES `Resposta` (`idcomentario`),
  ADD CONSTRAINT `fk_Reposta_Usuario1` FOREIGN KEY (`idUsuario`) REFERENCES `Usuario` (`idusuario`);

--
-- Constraints for table `RespostaPostagemGrupo`
--
ALTER TABLE `RespostaPostagemGrupo`
  ADD CONSTRAINT `fk_RespostaUsuarioGrupo_PostagensGrupo1` FOREIGN KEY (`PostagensGrupo_idPostagem`) REFERENCES `PostagensGrupo` (`idpostagem`),
  ADD CONSTRAINT `fk_RespostaUsuarioGrupo_RespostaUsuarioGrupo1` FOREIGN KEY (`RespostaUsuarioGrupo_RespostaUsuarioGrupo`) REFERENCES `RespostaPostagemGrupo` (`respostausuariogrupo`),
  ADD CONSTRAINT `fk_RespostaUsuarioGrupo_Usuario1` FOREIGN KEY (`Usuario_idUsuario`) REFERENCES `Usuario` (`idusuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
