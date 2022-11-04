-- -- explicit cursors
-- declare
-- c_id emp_data.empid%type;
-- c_name emp_data.emp_name%type;
-- c_ta emp_data.ta%type;

-- cursor c_cust is
-- select empid,emp_name,ta from emp_data;
-- begin
--   open c_cust;
--   loop
--     fetch c_cust into c_id,c_name,c_ta;
--     exit when c_cust%notfound;
--     dbms_output.put_line(c_id||' '||c_name||' '||c_ta);
--   end loop;
-- end;


alter table customers add(salary number(10));
select *from customers;
  update customers set salary = 10000 where customerid=1;
declare
total_rows number(2);
begin
update customers
set salary = salary + 500;
if sql%notfound then
dbms_output.put_line('no customers selected');

else if sql%found then
total_rows := sql%rowcount;
dbms_output.put_line(total_rows || 'customers selected');
end if;

end;