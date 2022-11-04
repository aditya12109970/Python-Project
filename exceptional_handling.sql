-- -- exceptional handling
-- declare 
-- c_id customers.customer_id%type := 9;
-- c_name customers.customername%type;
-- customer_addr customers.address%type;

-- begin
--   select customername, address into c_name, customer_addr
--     from customers
--     where customer_id = c_id;
--     dbms_output.put_line('Customer name: ' || c_name);
--     dbms_output.put_line('Customer address: ' || customer_addr);
--     exception
--       when no_data_found then
--         dbms_output.put_line('No customer found with id ' || c_id);
--         when invalid then
--           dbms_output.put_line('Invalid id ' || c_id);

--           when others then
--             dbms_output.put_line('Error!');

    

-- end;

-- -- cursor creation
-- declare
--   c_id customers.customer_id%type := 9;
--   c_name customers.customername%type;
--   customer_addr customers.address%type;
--   c1 customers%found;
  
-- begin





create table A(customer_id number, customername varchar2(20), address varchar2(20));

