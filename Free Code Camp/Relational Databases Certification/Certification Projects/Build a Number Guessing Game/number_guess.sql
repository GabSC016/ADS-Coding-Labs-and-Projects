--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.4)

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

DROP DATABASE number_guess;
--
-- Name: number_guess; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE number_guess WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE number_guess OWNER TO freecodecamp;

\connect number_guess

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: game_info; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.game_info (
    user_id integer NOT NULL,
    username character varying(22) NOT NULL,
    games_played integer,
    best_game integer
);


ALTER TABLE public.game_info OWNER TO freecodecamp;

--
-- Name: game_info_user_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.game_info_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_info_user_id_seq OWNER TO freecodecamp;

--
-- Name: game_info_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.game_info_user_id_seq OWNED BY public.game_info.user_id;


--
-- Name: game_info user_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.game_info ALTER COLUMN user_id SET DEFAULT nextval('public.game_info_user_id_seq'::regclass);


--
-- Data for Name: game_info; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.game_info VALUES (1, 'Gabs', 1, 13);
INSERT INTO public.game_info VALUES (3, 'user_1788310483955', 1, 332);
INSERT INTO public.game_info VALUES (2, 'user_1788310483956', 4, 199);
INSERT INTO public.game_info VALUES (5, 'user_1788310491609', 1, 396);
INSERT INTO public.game_info VALUES (4, 'user_1788310491610', 4, 96);
INSERT INTO public.game_info VALUES (7, 'user_1788310565470', 1, 311);
INSERT INTO public.game_info VALUES (6, 'user_1788310565471', 4, 92);
INSERT INTO public.game_info VALUES (8, 'Leo', NULL, NULL);
INSERT INTO public.game_info VALUES (10, 'user_1788310940506', 1, 841);
INSERT INTO public.game_info VALUES (9, 'user_1788310940507', 4, 346);
INSERT INTO public.game_info VALUES (12, 'user_1788311171316', 2, 164);
INSERT INTO public.game_info VALUES (11, 'user_1788311171317', 5, 109);
INSERT INTO public.game_info VALUES (14, 'user_1788311231347', 2, 530);
INSERT INTO public.game_info VALUES (13, 'user_1788311231348', 5, 81);


--
-- Name: game_info_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.game_info_user_id_seq', 14, true);


--
-- Name: game_info game_info_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.game_info
    ADD CONSTRAINT game_info_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

