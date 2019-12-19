use sakila;
show tables;
select category.name as Kategori, count(distinct film.film_id) as JumlahMovie,
avg(film.rental_rate) from category inner join film_category 
on category.category_id = film_category.category_id 
inner join film on film_category.film_id = film.film_id group by category.name 
order by jumlahMovie desc;

