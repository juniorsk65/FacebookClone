CREATE DATABASE  IF NOT EXISTS `facebook` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `facebook`;
-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: facebook
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `PostagensUsuario`
--

DROP TABLE IF EXISTS `PostagensUsuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PostagensUsuario` (
  `idPostagemUsuario` int(11) NOT NULL AUTO_INCREMENT,
  `usuarioProprietario` int(11) NOT NULL,
  `idUsuario2` int(11) NOT NULL,
  `conteudo` text,
  PRIMARY KEY (`idPostagemUsuario`,`usuarioProprietario`,`idUsuario2`),
  KEY `fk_PostagensUsuario_Usuario1_idx` (`usuarioProprietario`),
  KEY `fk_PostagensUsuario_Usuario2_idx` (`idUsuario2`),
  CONSTRAINT `fk_PostagensUsuario_Usuario1` FOREIGN KEY (`usuarioProprietario`) REFERENCES `Usuario` (`idUsuario`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_PostagensUsuario_Usuario2` FOREIGN KEY (`idUsuario2`) REFERENCES `Usuario` (`idUsuario`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PostagensUsuario`
--

LOCK TABLES `PostagensUsuario` WRITE;
/*!40000 ALTER TABLE `PostagensUsuario` DISABLE KEYS */;
INSERT INTO `PostagensUsuario` VALUES (1,1,1,'Teste pelo workbench'),(2,1,1,'enesima tentativa pelo terminal'),(3,1,1,'deu certo é tetra'),(4,1,1,'teste da postagem numero 12312312'),(5,1,1,'vai ter reuniao hoje?'),(6,1,1,'fiz postagem'),(7,1,1,'asçdlas'),(8,1,1,'aasldfasdf'),(9,3,3,'minha primeira postagem'),(10,3,3,'teste de postagem'),(11,6,6,'Eu amo Ingrid S2 S2'),(12,5,5,'teste de postagem');
/*!40000 ALTER TABLE `PostagensUsuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 15:00:01
