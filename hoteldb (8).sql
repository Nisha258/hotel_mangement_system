-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2024 at 01:50 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

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
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_no` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `roomtype` varchar(100) NOT NULL,
  `roomno` int(11) NOT NULL,
  `cost` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`bill_no`, `name`, `contact`, `date`, `roomtype`, `roomno`, `cost`) VALUES
(281, 'sbgd', 12, '2024-03-12 12:14:48', 'double', 101, 50),
(1377, 'krina', 987898989, '2024-03-12 12:00:48', 'double', 101, 1000),
(2447, 'njnj', 2147483647, '2024-03-12 12:08:54', 'double', 101, 100),
(3623, 'wd', 12222, '2024-03-12 12:10:16', 'double', 101, 100),
(4189, 'nisha', 122, '2024-02-12 22:10:13', 'luxury', 101, 120),
(5307, 'asa', 12222, '2024-03-12 12:12:09', 'double', 101, 100),
(6452, 'nisha', 2147483647, '2024-03-12 12:03:16', 'double', 101, 1000),
(6870, 'bh', 909090, '2024-03-12 12:16:37', 'double', 101, 70),
(8511, 'nill', 11, '2024-02-12 22:09:43', 'double', 101, 120);

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
(2619, 'hetvi', 'female', 3656, 2147483647, 'hetvi@mail.com', 'India', 'Driving licence', 201, 'khijdiya'),
(3486, 'nina', 'female', 8907, 987001691, 'sssss', 'India', 'Aadhar Card', 12, 'amreli'),
(4368, 'nisha', 'female', 365601, 988978788, 'nisha@gmail.com', 'USA', 'Driving licence', 201, 'mangvapal'),
(5343, 'vedant', 'male', 676545, 2147483647, 'ved@mail.com', 'India', 'Aadhar Card', 100, 'Banglore'),
(7704, 'aarefa', 'male', 565656, 2147483647, 'aarefdi@gmail.com', 'USA', 'passpirt', 120, 'banglore'),
(9079, 'mansi', 'female', 3545, 898888889, 'mansi@gmail.com', 'India', 'passpirt', 122, 'chital');

-- --------------------------------------------------------

--
-- Table structure for table `empdetail1`
--

CREATE TABLE `empdetail1` (
  `empcon` int(11) NOT NULL,
  `empid` int(10) NOT NULL,
  `empdept` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `empdetail1`
--

INSERT INTO `empdetail1` (`empcon`, `empid`, `empdept`) VALUES
(1, 0, 'hh'),
(9080898, 0, 'hh'),
(98888889, 2, 'food'),
(2147483647, 12, 'managment');

-- --------------------------------------------------------

--
-- Table structure for table `emps`
--

CREATE TABLE `emps` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(100) NOT NULL,
  `emp_dept` varchar(100) NOT NULL,
  `emp_add` varchar(100) NOT NULL,
  `emp_gen` varchar(100) NOT NULL,
  `emp_mail` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emps`
--

INSERT INTO `emps` (`emp_id`, `emp_name`, `emp_dept`, `emp_add`, `emp_gen`, `emp_mail`) VALUES
(98888889, 'nisha', 'food', 'xsxs', 'male', 'nihhh'),
(98888889, 'nisha', 'food', 'xsxs', 'male', 'nihhh');

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
('nisha', 'patel', NULL, NULL, '2024-01-01 18:31:51'),
('mansi', 'password', NULL, NULL, '0000-00-00 00:00:00');

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
  `room_id` int(11) NOT NULL,
  `roomtype` varchar(100) NOT NULL,
  `meal` varchar(100) NOT NULL,
  `noofday` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roombook`
--

INSERT INTO `roombook` (`contact`, `checkin`, `checkout`, `room_id`, `roomtype`, `meal`, `noofday`) VALUES
('987001691', '22/09/2024', '27/09/2024', 101, 'double', 'breakfast', '5'),
('987001691', '29/09/2024', '01/10/2024', 102, 'luxury', 'dinner', '2'),
('987001691', '12/09/2001', '18/09/2001', 101, 'single', 'lunch', '6');

-- --------------------------------------------------------

--
-- Table structure for table `roomdetail`
--

CREATE TABLE `roomdetail` (
  `floor` int(11) NOT NULL,
  `roomno` int(100) NOT NULL,
  `roomtype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roomdetail`
--

INSERT INTO `roomdetail` (`floor`, `roomno`, `roomtype`) VALUES
(1, 101, 'double'),
(1, 102, 'luxury'),
(1, 103, 'double'),
(1, 104, 'single'),
(1, 105, 'luxury'),
(2, 106, 'single'),
(2, 107, 'double'),
(2, 108, 'luxury'),
(2, 109, 'single'),
(2, 110, 'double');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_no`),
  ADD KEY `roomno` (`roomno`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `empdetail1`
--
ALTER TABLE `empdetail1`
  ADD PRIMARY KEY (`empcon`);

--
-- Indexes for table `emps`
--
ALTER TABLE `emps`
  ADD KEY `emp_id` (`emp_id`);

--
-- Indexes for table `roombook`
--
ALTER TABLE `roombook`
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `roomdetail`
--
ALTER TABLE `roomdetail`
  ADD PRIMARY KEY (`roomno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `bill_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8512;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `ref` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9130;

--
-- AUTO_INCREMENT for table `empdetail1`
--
ALTER TABLE `empdetail1`
  MODIFY `empcon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`roomno`) REFERENCES `roomdetail` (`roomno`);

--
-- Constraints for table `emps`
--
ALTER TABLE `emps`
  ADD CONSTRAINT `emps_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `empdetail1` (`empcon`);

--
-- Constraints for table `roombook`
--
ALTER TABLE `roombook`
  ADD CONSTRAINT `roombook_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `roomdetail` (`roomno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
