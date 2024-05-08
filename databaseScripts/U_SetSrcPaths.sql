UPDATE Locations
   SET SrcPath = REPLACE(SrcPath, '<path>', '<your_value_here>')
 WHERE SrcPath LIKE '%<path>%';

SELECT *
  FROM Locations;