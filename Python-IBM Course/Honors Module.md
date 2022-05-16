## Exercise 1, Question 2
```sql
SELECT cd.CASE_NUMBER, cd.PRIMARY_TYPE, ps.COMMUNITY_AREA_NAME
FROM `ferrous-destiny-344108.ibm.chicago_crime_data` AS cd
JOIN `ferrous-destiny-344108.ibm.chicago_public_schools` AS ps
ON  cd.COMMUNITY_AREA_NUMBER = ps.COMMUNITY_AREA_NUMBER
WHERE cd.LOCATION_DESCRIPTION LIKE '%SCHOOL%'
```

## Exercise 2, Question 1
```sql
SELECT NAME_OF_SCHOOL, Leaders_Icon
FROM `ferrous-destiny-344108.ibm.chicago_public_schools`
```

