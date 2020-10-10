INSERT INTO `user_group_desp` VALUES (1, 'AA', 'AA_maintainer');
INSERT INTO `user_group_desp` VALUES (2, 'CS', 'Custom');

INSERT INTO `user_role_desp` VALUES (1, 'admin', 'admin');
INSERT INTO `user_role_desp` VALUES (2, 'user', 'user');
INSERT INTO `user_role_desp` VALUES (3, 'superuser', 'Super user');


INSERT INTO `user_infos` VALUES (1, 'admin', '$5$rounds=535000$DGYsY0cgBEPuCvMI$s9GgYkC1oIYAjnJfZWWovaCowBraSus17/lOEuANUI3', 'active', 1, 'admin@system.com', NULL, 'Admin', 'A', 'first admin');
INSERT INTO `user_infos` VALUES (2, 'user', '$5$rounds=535000$H6l1lc1ainVPSYmT$EW5JEjLpQXj8ltTtiTAi9wUhp8nfFXkqn/ebIYS7hE4', 'active', 1, 'user@system.com', NULL, 'User', 'A', 'first User');
INSERT INTO `user_infos` VALUES (3, 'super', '$5$rounds=535000$j20gy7VGJifkYkcJ$7N./7taBDK1jhSSIZboGuGlWFmS1jEXOwiVwSWanTg3', 'active', 1, 'super@system.com', NULL, 'Super', 'A', 'first Super User');

INSERT INTO `user_groups` VALUES (1, 1);
INSERT INTO `user_groups` VALUES (2, 2);
INSERT INTO `user_groups` VALUES (3, 1);

INSERT INTO `user_roles` VALUES (1, 1);
INSERT INTO `user_roles` VALUES (2, 2);
INSERT INTO `user_roles` VALUES (3, 3);



-- for your dummy data checking 
SELECT 
	A.* ,
	B.`name` as 'Group_Name',
	C.`name` as 'Role_Name'
FROM 		`user_infos`		A
Left JOIN 	`user_groups` 		B1 	ON 	A.`id` = B1.`user_id`
INNER JOIN 	`user_group_desp`   B 	ON 	B1.`group_id` = B.`id`
LEFT JOIN  	`user_roles` 		C1 	ON 	A.`id` = C1.`user_id`
INNER JOIN 	`user_role_desp` 	C 	ON 	C1.`role_id` = C.`id`
;