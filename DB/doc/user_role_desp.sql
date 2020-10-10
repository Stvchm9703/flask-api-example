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

 Date: 16/04/2019 18:44:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user_role_desp
-- ----------------------------
DROP TABLE IF EXISTS `user_role_desp`;
CREATE TABLE `user_role_desp`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `desp` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user_role_desp
-- ----------------------------
INSERT INTO `user_role_desp` VALUES (1, 'admin', 'admin');
INSERT INTO `user_role_desp` VALUES (2, 'user', 'user');
INSERT INTO `user_role_desp` VALUES (3, 'superuser', 'Super user');

SET FOREIGN_KEY_CHECKS = 1;
