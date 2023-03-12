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

CREATE TABLE IF NOT EXISTS Guild_Settings(
    GuildID integer PRIMARY KEY,
    HOF_channel_ID integer,
    Command_channel_ID integer,
    Strike1_role_ID integer,
    Strike2_role_ID integer
);

CREATE TABLE IF NOT EXISTS hall_of_fame(
    Root_message_ID integer PRIMARY KEY,
    Hall_message_ID integer,
    Stars integer DEFAULT 0
);