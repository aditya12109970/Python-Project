-- triggers
 create table cust_new(custid int, custname varchar2(50), salary int, newsalary number(20),oldsal number(20));
 insert into cust_new values(1,'A',10000,11000,10000);
    insert into cust_new values(2,'B',20000,21000,20000);

    create or replace trigger cust_salary_changes
    before delete or update  on cust_new
    for each row
    when (new.custid>0) then 
    declare
    sal_diff number(20);
    begin
    sal_diff:=new.sal-old.sal;
    dbms_output.put_line('old salary is '||old.sal);
    dbms_output.put_line('new salary is '||new.sal);
    dbms_output.put_line('Salary difference is '||sal_diff);
    end;