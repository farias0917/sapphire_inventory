-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2023 a las 10:10:39
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sapphireinventory`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categories`
--

INSERT INTO `categories` (`category_id`, `category_name`) VALUES
(1, 'Lacteos'),
(2, 'Granos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `entries`
--

CREATE TABLE `entries` (
  `entry_id` int(11) NOT NULL,
  `purchase_price` decimal(10,2) NOT NULL,
  `entry_qty` int(11) NOT NULL,
  `entry_date` datetime NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `entries`
--

INSERT INTO `entries` (`entry_id`, `purchase_price`, `entry_qty`, `entry_date`, `product_id`) VALUES
(1, 1500.00, 5, '2023-11-30 03:28:41', 1),
(2, 2000.00, 15, '2023-11-30 03:30:03', 2),
(3, 2500.00, 40, '2023-11-30 03:34:21', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_mark` varchar(100) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_desc` varchar(100) NOT NULL,
  `product_qty` int(11) NOT NULL,
  `product_date` datetime NOT NULL,
  `product_img` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`product_id`, `product_mark`, `product_name`, `product_desc`, `product_qty`, `product_date`, `product_img`, `category_id`) VALUES
(1, 'alpina', 'yogurt griego', 'rico yogurt', 15, '2023-11-30 03:28:03', '2023032803_yogurt.webp', 1),
(2, 'Roa', 'arroz', 'arroz roa', 0, '2023-11-30 03:28:21', '2023032821_arroz.png', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sales`
--

CREATE TABLE `sales` (
  `sale_id` int(11) NOT NULL,
  `sale_price` decimal(10,2) NOT NULL,
  `sale_qty` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sales`
--

INSERT INTO `sales` (`sale_id`, `sale_price`, `sale_qty`, `fecha`, `product_id`, `user_id`) VALUES
(1, 4000.00, 15, '2023-11-30 03:33:33', 2, 0),
(2, 4000.00, 15, '2023-11-30 03:33:51', 2, 0),
(3, 2500.00, 55, '2023-11-30 03:34:36', 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_lastName` varchar(100) DEFAULT NULL,
  `user_phoneNumber` int(10) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_pass` varchar(100) NOT NULL,
  `user_img` varchar(100) DEFAULT NULL,
  `user_rol` int(11) NOT NULL DEFAULT 2
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`user_id`, `user_name`, `user_lastName`, `user_phoneNumber`, `user_email`, `user_pass`, `user_img`, `user_rol`) VALUES
(1, 'Emanuel', 'Farias', 3124222, 'emanue@mail.com', '123', NULL, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indices de la tabla `entries`
--
ALTER TABLE `entries`
  ADD PRIMARY KEY (`entry_id`),
  ADD KEY `emtries_ibfk_1` (`product_id`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `products_ibfk_1` (`category_id`);

--
-- Indices de la tabla `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`sale_id`),
  ADD KEY `sales_ibfk_1` (`product_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `entries`
--
ALTER TABLE `entries`
  MODIFY `entry_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `sales`
--
ALTER TABLE `sales`
  MODIFY `sale_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `entries`
--
ALTER TABLE `entries`
  ADD CONSTRAINT `emtries_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`);

--
-- Filtros para la tabla `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


select * from entries;

select * from products;
select * from sales;

select e.entry_id, p.product_name, e.entry_qty, e.purchase_price, sum(e.purchase_price * e.entry_qty) as total, e.entry_date from entries as e inner join
products as p on e.product_id = p.product_id group by e.entry_id;


select s.sale_id, p.product_name, s.sale_qty, s.sale_price, sum(s.sale_price * s.sale_qty) as total, s.fecha from sales as s inner join
products as p on s.product_id = p.product_id group by s.sale_id;

create trigger agregarEntrada_AI after insert on entries for each row update products
set product_qty = product_qty + 10 where product_id = 3;


SELECT SUM(sale_price * sale_qty) as totalGanado FROM sales
