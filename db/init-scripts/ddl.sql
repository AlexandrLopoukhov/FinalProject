CREATE TABLE public.compound (
    id serial NOT NULL,
    compound varchar(400) NOT NULL,
    name varchar(400) NOT NULL,
    formula varchar(400) NOT NULL,
    inchi varchar(400) NOT NULL,
    inchi_key varchar(400) NOT NULL,
    smiles varchar(400) NOT NULL,
    cross_links_count integer NOT NULL,
    CONSTRAINT users_user_pkey PRIMARY KEY (id)
);
