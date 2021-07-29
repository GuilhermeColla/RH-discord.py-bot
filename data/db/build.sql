CREATE TABLE IF NOT EXISTS exp(
    UserID integer PRIMARY KEY,
    XP integer DEFAULT 0,
    Level integer DEFAULT 0,
    XPLock text DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS strikes(
    UserID integer PRIMARY KEY,
    Strike1_ID integer,
    Strike2_ID integer,
    Mute_Day date
);

CREATE TABLE IF NOT EXISTS strike_cd(
    UserID integer PRIMARY KEY,
    Last_strike_ID integer,
    Last_strike_date text
);

-- Não podemos fazer uma TABLE com apenas 1 coluna. Isso vai ficar aqui
-- até que eu volte a desenvolver a parte referente a ela.
--CREATE TABLE IF NOT EXISTS Guild_Settings(
--    GuildID integer PRIMARY KEY,
--);
