use company;


select * from countries;

select phone_number,email from employees;

select * from employees where last_name like '%Fay';

select hire_date from employees where last_name like '%Fay' or 'Whalen';

select employees.first_name,employees.last_name from employees INNER JOIN jobs ON employees.job_id=jobs.job_id where job_title="Shipping Clerk";

select * from employees INNER JOIN departments ON employees.department_id=departments.department_id where employees.department_id=8;

select * from departments order by department_id desc;

select * from employees where last_name like 'k%';