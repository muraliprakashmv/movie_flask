/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.17 : Database - rating
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`rating` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `rating`;

/*Table structure for table `director` */

DROP TABLE IF EXISTS `director`;

CREATE TABLE `director` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `loginid` int(11) NOT NULL,
  `directorname` varchar(25) NOT NULL,
  `housename` varchar(25) NOT NULL,
  `place` varchar(25) NOT NULL,
  `post` varchar(25) NOT NULL,
  `pin` int(11) NOT NULL,
  `gender` varchar(25) NOT NULL,
  `mobile` int(11) NOT NULL,
  `email` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `director` */

insert  into `director`(`id`,`loginid`,`directorname`,`housename`,`place`,`post`,`pin`,`gender`,`mobile`,`email`) values 
(1,2,'Lal Jose','Lal villa','Ernakulam','Ernakulam',671543,'Male',2147483647,'laljose@gmail.com'),
(2,3,'Omar Lulu','Lulu house','Kochi','Kochi',675432,'Male',2147483647,'luluomar@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'laljose','lalu123','Director'),
(3,'omarlulu','123','Director');

/*Table structure for table `movie` */

DROP TABLE IF EXISTS `movie`;

CREATE TABLE `movie` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `moviename` varchar(25) NOT NULL,
  `director` varchar(20) NOT NULL,
  `releasedate` date NOT NULL,
  `actors` varchar(50) NOT NULL,
  `location` varchar(25) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `movie` */

insert  into `movie`(`id`,`moviename`,`director`,`releasedate`,`actors`,`location`) values 
(1,'adaarlove','3','2019-12-01','Priya,Nourin,Roshan','Ernakulam,Kasargod,Payyan'),
(2,'anthampaathira','2','2020-04-14','chakochan','ekm');

/*Table structure for table `rating_tbl` */

DROP TABLE IF EXISTS `rating_tbl`;

CREATE TABLE `rating_tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `rate` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=latin1;

/*Data for the table `rating_tbl` */

insert  into `rating_tbl`(`id`,`mid`,`date`,`rate`) values 
(46,1,'2020-04-24',0),
(47,1,'2020-04-24',0),
(48,1,'2020-04-24',0),
(49,1,'2020-04-24',0),
(50,1,'2020-04-24',5),
(51,1,'2020-04-24',5),
(52,1,'2020-04-24',5),
(53,1,'2020-04-24',5),
(54,1,'2020-04-24',5),
(55,1,'2020-04-24',5),
(56,1,'2020-04-24',5),
(57,1,'2020-04-24',5),
(58,1,'2020-04-24',5),
(59,1,'2020-04-24',5);

/*Table structure for table `storyboard` */

DROP TABLE IF EXISTS `storyboard`;

CREATE TABLE `storyboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movieid` int(11) DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `emotion` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `storyboard` */

insert  into `storyboard`(`id`,`movieid`,`start_time`,`end_time`,`emotion`) values 
(2,1,'2020-04-23 00:00:23','2020-04-23 00:00:35','happy');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
