-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2020-07-24 11:42:15
-- サーバのバージョン： 10.4.11-MariaDB
-- PHP のバージョン: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `tennis`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `score`
--

CREATE TABLE `score` (
  `player1` int(11) DEFAULT NULL,
  `player2` int(11) DEFAULT NULL,
  `tieplayer1` int(11) DEFAULT NULL,
  `tieplayer2` int(11) DEFAULT NULL,
  `tiecheck` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- テーブルのデータのダンプ `score`
--

INSERT INTO `score` (`player1`, `player2`, `tieplayer1`, `tieplayer2`, `tiecheck`) VALUES
(1, NULL, NULL, NULL, NULL),
(1, NULL, NULL, NULL, NULL),
(1, NULL, NULL, NULL, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, 1, NULL, NULL),
(NULL, NULL, NULL, 2, NULL),
(NULL, NULL, NULL, NULL, 1),
(NULL, NULL, NULL, NULL, 1),
(NULL, NULL, NULL, 2, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
