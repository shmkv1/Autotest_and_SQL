



scooter_rent=#
     SELECT c.login, COUNT(o.id) AS "DeleveryCount" FROM "Couriers" AS c LEFT OUTER JOIN "Orders" AS o ON c.id=o."courierId" WHERE o."inDelivery"=true GROUP BY c.login;
 login  | DeleveryCount
--------+---------------
 ninja  |            10
 ninja1 |             4
(2 rows)


scooter_rent=#
     SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders";
 track  | status
--------+--------
 504741 |      0
 292361 |      0
  12100 |      0
 841867 |      1
 841867 |      1
 110120 |      1
 110120 |      1
 572945 |      1
 572945 |      1
 406172 |      1
 406172 |      1
 712664 |      1
 712664 |      1
 702739 |      1
 702739 |      1
 702853 |      1
 702853 |      1
(17 rows)
