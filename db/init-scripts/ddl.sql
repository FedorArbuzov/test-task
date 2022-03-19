CREATE TABLE public.requests (
    id serial NOT NULL,
    code varchar NOT NULL,
    info json NOT NULL,
    duplicates int NOT NULL,
    CONSTRAINT users_user_pkey PRIMARY KEY (id)
);
