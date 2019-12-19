use sakila;
show tables;
select film.rating, count(film.film_id) from film 
group by film.rating order by film.rating asc;