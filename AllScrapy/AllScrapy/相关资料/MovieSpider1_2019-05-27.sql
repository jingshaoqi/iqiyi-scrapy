# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.24)
# Database: MovieSpider1
# Generation Time: 2019-05-26 17:38:33 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table actor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `actor`;

CREATE TABLE `actor` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `character` varchar(200) DEFAULT NULL,
  `actorid` int(11) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `saveimageurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table category
# ------------------------------------------------------------

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `categories_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `subType` int(11) DEFAULT NULL,
  `subName` varchar(20) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `qipuId` int(11) DEFAULT NULL,
  `parentId` int(11) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table director
# ------------------------------------------------------------

DROP TABLE IF EXISTS `director`;

CREATE TABLE `director` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `directorid` int(11) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `saveimageurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table main_charactor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `main_charactor`;

CREATE TABLE `main_charactor` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `character` varchar(200) DEFAULT NULL,
  `maincharactorid` varchar(200) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `saveimageurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table movietable
# ------------------------------------------------------------

DROP TABLE IF EXISTS `movietable`;

CREATE TABLE `movietable` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `movieid` decimal(20,0) DEFAULT NULL,
  `channelld` int(11) DEFAULT NULL,
  `description` text,
  `name` varchar(100) DEFAULT NULL,
  `playurl` varchar(100) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  `focus` varchar(100) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `secondInfo` text,
  `formatPeriod` varchar(200) DEFAULT NULL,
  `siteId` varchar(200) DEFAULT NULL,
  `issuetime` int(100) DEFAULT NULL,
  `imageurl` varchar(100) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `saveimageurl` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table performerdetail
# ------------------------------------------------------------

DROP TABLE IF EXISTS `performerdetail`;

CREATE TABLE `performerdetail` (
  `name` varchar(100) DEFAULT NULL,
  `jobtitle` varchar(200) DEFAULT NULL,
  `width` varchar(20) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `blood` varchar(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `imageurl` varchar(200) DEFAULT NULL,
  `des` text,
  `saveimageurl` varchar(200) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `performerid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table screen_writer
# ------------------------------------------------------------

DROP TABLE IF EXISTS `screen_writer`;

CREATE TABLE `screen_writer` (
  `id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `screen_writer_id` int(11) DEFAULT NULL,
  `imageurl` varchar(100) DEFAULT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `saveimageurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
