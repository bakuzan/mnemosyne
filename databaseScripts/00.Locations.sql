CREATE TABLE IF NOT EXISTS "Locations" (
	"Id"	        	    INTEGER NOT NULL UNIQUE,
	"Name"				    TEXT    NOT NULL UNIQUE,
	"SrcPath"		        TEXT    NOT NULL UNIQUE,
	"DestName"		        TEXT    NOT NULL,
	"IsWhitelistRequired"	BIT     NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT)
);