-- Locations
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Analytics", "C:\<path>\Analytics", "Analytics", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Books", "C:\<path>\Books", "Books", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Browser_Backups", "C:\<path>\Browser_Backups", "Browser_Backups", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Comics", "C:\<path>\Comics", "Comics", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Comics (New)", "C:\<path>\Comics\#temp", "Comics", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Data", "C:\<path>\Data", "Data", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("DB_Backups", "C:\<path>\DB_Backups", "DB_Backups", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Manga", "C:\<path>\Manga", "Manga", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Manga (New)", "C:\<path>\Manga\#temp", "Manga", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Music", "C:\<path>\Music", "Music", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Pictures", "C:\<path>\Pictures", "Pictures", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Podcasts", "C:\<path>\Music\#temp", "Podcasts", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Research", "C:\<path>\Research", "Research", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Videos - Misc", "C:\<path>\Videos", "Videos - Misc", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Videos - Misc (New)", "C:\<path>\Videos\#temp\Videos - Misc", "Videos - Misc", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Videos", "C:\<path>\Videos\#temp\# backup", "Videos", 0);
INSERT INTO Locations ('Name', 'SrcPath', 'DestName', 'IsWhitelistRequired')
VALUES ("Writing", "C:\<path>\Writing", "Writing", 0);

-- Blacklist
INSERT INTO Blacklist ('LocationId', 'Name')
VALUES (NULL, "#temp");
INSERT INTO Blacklist ('LocationId', 'Name')
VALUES (NULL, "# already copied");
INSERT INTO Blacklist ('LocationId', 'Name')
VALUES (NULL, "# bulk single issues");
INSERT INTO Blacklist ('LocationId', 'Name')
VALUES (NULL, "# backup");
INSERT INTO Blacklist ('LocationId', 'Name')
VALUES (NULL, "# no copy");

-- Blacklist, location specific
INSERT INTO Blacklist ('LocationId', 'Name')
SELECT Id, 'Audio Clips'
  FROM Locations
 WHERE Name = 'Music';
INSERT INTO Blacklist ('LocationId', 'Name')
SELECT Id, 'iTunes'
  FROM Locations
 WHERE Name = 'Music'; 

-- Whitelist
INSERT INTO Whitelist ('LocationId', 'Name')
VALUES (0, "");
