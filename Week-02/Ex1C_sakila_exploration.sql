/*
a) actor_id, first_name, last_name, last_update
b) film_id, title, description, release_year, language_id, original_language, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update
c) film_actor
d) it includes all the columns under rental and it is easy to read because it is organized.
e) It has four categories/columns and it is a bit more difficult to read due to its simple numbers and not having very distinct ID's.
f) You need the film and rental tables. They are related through FK being used as a link.
*/

SELECT film_id FROM film;
SELECT rental_id FROM rental;