--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-0+deb12u1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-0+deb12u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: wiley
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO wiley;

--
-- Name: log_entry; Type: TABLE; Schema: public; Owner: wiley
--

CREATE TABLE public.log_entry (
    date_created timestamp with time zone DEFAULT now() NOT NULL,
    level character varying NOT NULL,
    module character varying,
    line integer,
    message character varying NOT NULL,
    pid integer,
    tid bigint,
    stack character varying
);


ALTER TABLE public.log_entry OWNER TO wiley;

--
-- Name: option; Type: TABLE; Schema: public; Owner: wiley
--

CREATE TABLE public.option (
    date_created timestamp with time zone DEFAULT now() NOT NULL,
    date_updated timestamp with time zone DEFAULT now(),
    db_version character varying,
    port integer,
    wizlock boolean,
    code_version character varying
);


ALTER TABLE public.option OWNER TO wiley;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: wiley
--

COPY public.alembic_version (version_num) FROM stdin;
cc539ecc4805
\.


--
-- Data for Name: log_entry; Type: TABLE DATA; Schema: public; Owner: wiley
--

COPY public.log_entry (date_created, level, module, line, message, pid, tid, stack) FROM stdin;
2023-07-10 14:40:37.953-07	INFO	wiley	71	Testing the SQL handler	205042	140106213802048	\N
2023-07-10 14:40:37.963-07	INFO	wiley	74	System was up for 0:00:00.444702	205042	140106213802048	\N
2023-07-10 14:40:37.967-07	CRITICAL	wiley	77	System halting.	205042	140106213802048	\N
\.


--
-- Data for Name: option; Type: TABLE DATA; Schema: public; Owner: wiley
--

COPY public.option (date_created, date_updated, db_version, port, wizlock, code_version) FROM stdin;
2023-07-10 09:37:21.152511-07	2023-07-10 14:40:37.945379-07	cc539ecc4805	4400	f	0.008
\.


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: wiley
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: log_entry log_entry_pkey; Type: CONSTRAINT; Schema: public; Owner: wiley
--

ALTER TABLE ONLY public.log_entry
    ADD CONSTRAINT log_entry_pkey PRIMARY KEY (date_created);


--
-- Name: option option_pkey; Type: CONSTRAINT; Schema: public; Owner: wiley
--

ALTER TABLE ONLY public.option
    ADD CONSTRAINT option_pkey PRIMARY KEY (date_created);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

