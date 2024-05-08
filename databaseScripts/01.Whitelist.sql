CREATE TABLE IF NOT EXISTS "Whitelist" (
	"Id"	        	    INTEGER NOT NULL UNIQUE,
    "LocationId"            INT     NULL,
	"Name"				    TEXT    NOT NULL UNIQUE,
	PRIMARY KEY("Id" AUTOINCREMENT),
    FOREIGN KEY("LocationId") REFERENCES "Locations"("Id")
);