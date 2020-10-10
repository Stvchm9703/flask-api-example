/*
 Navicat MySQL Data Transfer

 Source Server         : ipr_local
 Source Server Type    : MySQL
 Source Server Version : 100134
 Source Host           : localhost:3306
 Source Schema         : uno_web

 Target Server Type    : MySQL
 Target Server Version : 100134
 File Encoding         : 65001

 Date: 16/04/2019 18:45:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user_infos
-- ----------------------------
DROP TABLE IF EXISTS `user_infos`;
CREATE TABLE `user_infos`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `user_status` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email_confirmed_at` datetime(0) NULL DEFAULT NULL,
  `first_name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `last_name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `user_desc` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_name`(`user_name`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_infos
-- ----------------------------
INSERT INTO `user_infos` VALUES (1, 'admin', '$5$rounds=535000$DGYsY0cgBEPuCvMI$s9GgYkC1oIYAjnJfZWWovaCowBraSus17/lOEuANUI3', 'active', 1, 'admin@system.com', NULL, 'Admin', 'A', 'first admin');
INSERT INTO `user_infos` VALUES (2, 'user', '$5$rounds=535000$H6l1lc1ainVPSYmT$EW5JEjLpQXj8ltTtiTAi9wUhp8nfFXkqn/ebIYS7hE4', 'active', 1, 'user@system.com', NULL, 'User', 'A', 'first User');
INSERT INTO `user_infos` VALUES (3, 'super', '$5$rounds=535000$j20gy7VGJifkYkcJ$7N./7taBDK1jhSSIZboGuGlWFmS1jEXOwiVwSWanTg3', 'active', 1, 'super@system.com', NULL, 'Super', 'A', 'first Super User');

SET FOREIGN_KEY_CHECKS = 1;
