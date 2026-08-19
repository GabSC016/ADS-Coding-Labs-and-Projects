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

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

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
-- Name: asteroid; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.asteroid (
    asteroid_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    distance_from_earth_in_km integer NOT NULL
);


ALTER TABLE public.asteroid OWNER TO freecodecamp;

--
-- Name: astroid_astroid_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.astroid_astroid_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.astroid_astroid_id_seq OWNER TO freecodecamp;

--
-- Name: astroid_astroid_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.astroid_astroid_id_seq OWNED BY public.asteroid.asteroid_id;


--
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    galaxy_type character varying(30) NOT NULL,
    age_in_millions_of_years numeric(6,0) NOT NULL
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    age_in_millions_of_years numeric(6,0) NOT NULL,
    orbital_period_in_days integer NOT NULL,
    planet_id integer NOT NULL
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    has_life boolean NOT NULL,
    is_spherical boolean NOT NULL,
    orbital_period_in_days integer NOT NULL,
    star_id integer NOT NULL
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(30) NOT NULL,
    description text NOT NULL,
    age_in_millions_of_years numeric(6,0) NOT NULL,
    star_types character varying(30) NOT NULL,
    galaxy_id integer NOT NULL
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: asteroid asteroid_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.asteroid ALTER COLUMN asteroid_id SET DEFAULT nextval('public.astroid_astroid_id_seq'::regclass);


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: asteroid; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.asteroid VALUES (1, 'Ceres', 'The largest object in the asteroid belt between Mars and Jupiter.', 264000000);
INSERT INTO public.asteroid VALUES (2, 'Vesta', 'One of the largest objects in the asteroid belt.', 224000000);
INSERT INTO public.asteroid VALUES (3, 'Pallas', 'One of the largest asteroids in the Solar System.', 300000000);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'Milky Way', 'The galaxy that contains the Solar System and billions of other stars.', 'Spiral', 13600);
INSERT INTO public.galaxy VALUES (2, 'Andromeda', 'A spiral galaxy that is the nearest major galaxy to the Milky Way.', 'Spiral', 10000);
INSERT INTO public.galaxy VALUES (3, 'Triangulum', 'A spiral galaxy located in the Local Group of galaxies.', 'Spiral', 13000);
INSERT INTO public.galaxy VALUES (4, 'Sombrero', 'A galaxy known for its bright central bulge and dark dust lane.', 'Spiral', 9000);
INSERT INTO public.galaxy VALUES (5, 'Whirlpool', 'A grand-design spiral galaxy with prominent spiral arms.', 'Spiral', 10000);
INSERT INTO public.galaxy VALUES (6, 'Large Magellanic Cloud', 'A small irregular galaxy that orbits the Milky Way.', 'Irregular', 13000);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Moon', 'Earth''s only natural satellite.', 4530, 27, 1);
INSERT INTO public.moon VALUES (2, 'Phobos', 'The larger and closer moon of Mars.', 4500, 0, 4);
INSERT INTO public.moon VALUES (3, 'Deimos', 'The smaller and more distant moon of Mars.', 4500, 1, 4);
INSERT INTO public.moon VALUES (4, 'Io', 'A volcanic moon of Jupiter.', 4500, 2, 5);
INSERT INTO public.moon VALUES (5, 'Europa', 'An icy moon of Jupiter that may have a subsurface ocean.', 4500, 4, 5);
INSERT INTO public.moon VALUES (6, 'Ganymede', 'The largest moon in the Solar System.', 4500, 7, 5);
INSERT INTO public.moon VALUES (7, 'Callisto', 'A heavily cratered moon of Jupiter.', 4500, 17, 5);
INSERT INTO public.moon VALUES (8, 'Titan', 'The largest moon of Saturn and the only moon with a dense atmosphere.', 4500, 16, 6);
INSERT INTO public.moon VALUES (9, 'Enceladus', 'An icy moon of Saturn known for its water-rich plumes.', 4500, 1, 6);
INSERT INTO public.moon VALUES (10, 'Rhea', 'The second-largest moon of Saturn.', 4500, 5, 6);
INSERT INTO public.moon VALUES (11, 'Iapetus', 'A moon of Saturn known for its two-tone surface.', 4500, 79, 6);
INSERT INTO public.moon VALUES (12, 'Dione', 'An icy moon of Saturn with bright ice cliffs.', 4500, 3, 6);
INSERT INTO public.moon VALUES (13, 'Tethys', 'An icy moon of Saturn with a large impact crater.', 4500, 2, 6);
INSERT INTO public.moon VALUES (14, 'Mimas', 'A small moon of Saturn with a large impact crater.', 4500, 1, 6);
INSERT INTO public.moon VALUES (15, 'Ariel', 'One of the major moons of Uranus.', 4500, 3, 7);
INSERT INTO public.moon VALUES (16, 'Umbriel', 'A dark moon of Uranus with a heavily cratered surface.', 4500, 4, 7);
INSERT INTO public.moon VALUES (17, 'Titania', 'The largest moon of Uranus.', 4500, 9, 7);
INSERT INTO public.moon VALUES (18, 'Oberon', 'The outermost major moon of Uranus.', 4500, 14, 7);
INSERT INTO public.moon VALUES (19, 'Triton', 'The largest moon of Neptune and an icy world.', 4500, 6, 8);
INSERT INTO public.moon VALUES (20, 'Nereid', 'A distant moon of Neptune with a highly eccentric orbit.', 4500, 360, 8);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Earth', 'The third planet from the Sun and the only known planet to support life.', true, true, 365, 1);
INSERT INTO public.planet VALUES (2, 'Mercury', 'The smallest planet and the closest planet to the Sun.', false, true, 88, 1);
INSERT INTO public.planet VALUES (3, 'Venus', 'The second planet from the Sun and the hottest planet in the Solar System.', false, true, 225, 1);
INSERT INTO public.planet VALUES (4, 'Mars', 'The fourth planet from the Sun, known as the Red Planet.', false, true, 687, 1);
INSERT INTO public.planet VALUES (5, 'Jupiter', 'The largest planet in the Solar System.', false, true, 4333, 1);
INSERT INTO public.planet VALUES (6, 'Saturn', 'The second-largest planet, known for its prominent ring system.', false, true, 10759, 1);
INSERT INTO public.planet VALUES (7, 'Uranus', 'An ice giant with a unique sideways rotation.', false, true, 30687, 1);
INSERT INTO public.planet VALUES (8, 'Neptune', 'The farthest known planet from the Sun in the Solar System.', false, true, 60190, 1);
INSERT INTO public.planet VALUES (9, 'Sirius b', 'A white dwarf star companion of Sirius.', false, true, 50, 2);
INSERT INTO public.planet VALUES (10, 'Proxima b', 'An exoplanet orbiting Proxima Centauri in the habitable zone.', false, true, 11, 3);
INSERT INTO public.planet VALUES (11, 'Kepler-186f', 'An exoplanet similar in size to Earth.', false, true, 130, 3);
INSERT INTO public.planet VALUES (12, 'Vega b', 'A hypothetical exoplanet associated with the star Vega.', false, true, 20, 6);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'Sun', 'The star at the center of the Solar System.', 4600, 'G', 1);
INSERT INTO public.star VALUES (2, 'Sirius', 'The brightest star in the night sky.', 242, 'A', 1);
INSERT INTO public.star VALUES (3, 'Proxima Centauri', 'The closest known star to the Sun.', 4850, 'M', 1);
INSERT INTO public.star VALUES (4, 'Betelgeuse', 'A red supergiant star in the constellation Orion.', 10, 'M', 1);
INSERT INTO public.star VALUES (5, 'Rigel', 'A blue supergiant star in the constellation Orion.', 8, 'B', 1);
INSERT INTO public.star VALUES (6, 'Vega', 'A bright white star in the constellation Lyra.', 455, 'A', 1);


--
-- Name: astroid_astroid_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.astroid_astroid_id_seq', 3, true);


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 6, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 6, true);


--
-- Name: asteroid asteroid_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.asteroid
    ADD CONSTRAINT asteroid_name_key UNIQUE (name);


--
-- Name: asteroid asteroid_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.asteroid
    ADD CONSTRAINT asteroid_pkey PRIMARY KEY (asteroid_id);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: moon moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_name_key UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--

