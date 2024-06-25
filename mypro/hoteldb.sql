-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 03, 2024 at 09:21 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hoteldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ref` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `postcode` int(11) NOT NULL,
  `mobile` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `nationality` varchar(70) NOT NULL,
  `idproof` varchar(70) NOT NULL,
  `idnumber` int(11) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ref`, `name`, `gender`, `postcode`, `mobile`, `email`, `nationality`, `idproof`, `idnumber`, `address`) VALUES
(2619, 'hetvi', 'female', 365678, 2147483647, 'hetvi@mail.com', 'India', 'Driving licence', 201, 'khijdiya'),
(3486, 'nina', 'female', 12345, 987001691, 'sssss', 'India', 'Aadhar Card', 12, 'amreli'),
(4368, 'nisha', 'female', 365601, 988978788, 'nisha@gmail.com', 'USA', 'Driving licence', 201, 'mangvapal'),
(5343, 'vedant', 'male', 676545, 2147483647, 'ved@mail.com', 'India', 'Aadhar Card', 100, 'Banglore'),
(9079, 'mansi', 'female', 3545, 898888889, 'mansi@gmail.com', 'India', 'passpirt', 122, 'chital');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `sec_que` varchar(100) DEFAULT NULL,
  `sec_ans` varchar(100) DEFAULT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `sec_que`, `sec_ans`, `created_at`) VALUES
('nisha', 'patel', NULL, NULL, '2024-01-01 18:31:51');

-- --------------------------------------------------------

--
-- Table structure for table `login1`
--

CREATE TABLE `login1` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login1`
--

INSERT INTO `login1` (`username`, `password`) VALUES
('nisha', 'patel');

-- --------------------------------------------------------

--
-- Table structure for table `roombook`
--

CREATE TABLE `roombook` (
  `contact` varchar(100) NOT NULL,
  `checkin` varchar(100) NOT NULL,
  `checkout` varchar(100) NOT NULL,
  `roomtype` varchar(100) NOT NULL,
  `availableroom` int(100) NOT NULL,
  `meal` varchar(100) NOT NULL,
  `noofday` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roombook`
--

INSERT INTO `roombook` (`contact`, `checkin`, `checkout`, `roomtype`, `availableroom`, `meal`, `noofday`) VALUES
('988978788', '20/09/2023', '29/09/2023', 'single', 1004, 'dinner', '9'),
('987001691', '12/09/2024', '19/09/2024', 'luxury', 1008, 'breakfast', '7'),
('988978788', '12/09/2023', '30/09/2023', 'single', 1009, 'dinner', '18'),
('988978788', '12/09/2023', '30/09/2023', 'double', 1011, 'lunch', '18');

-- --------------------------------------------------------

--
-- Table structure for table `roomdetail`
--

CREATE TABLE `roomdetail` (
  `floor` varchar(100) NOT NULL,
  `roomno` varchar(100) NOT NULL,
  `roomtype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `user` varchar(30) NOT NULL,
  `pass` text NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `user`, `pass`, `name`, `address`) VALUES
(0, 'nisha', '123', 'nii', 'hidd'),
(0, 'nishaa', '1234', 'nilll', 'njbj');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `roombook`
--
ALTER TABLE `roombook`
  ADD PRIMARY KEY (`availableroom`);

--
-- Indexes for table `roomdetail`
--
ALTER TABLE `roomdetail`
  ADD PRIMARY KEY (`floor`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `ref` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9130;

--
-- AUTO_INCREMENT for table `roombook`
--
ALTER TABLE `roombook`
  MODIFY `availableroom` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1012;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
