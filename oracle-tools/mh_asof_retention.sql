create or replace function mh_asof_retention return number as
-- return number of hours back an "as of" query will work
--
-- ORA-01555: snapshot too old: ...
-- ORA-08180: no snapshot found based on specified time
-- ORA-01466: unable to read data - table definition has changed
--
  hours    number;
  maxhours number;
  rrr      number;  
begin
  -- snapnums=[1555,8180]
  -- tblchange=[1466]

  maxhours := 24 * 30;           -- check for max 30 days
  for hours in 0..maxhours loop
      begin
          select rownum into rrr from lc$actor as of timestamp sysdate-(hours/24) where rownum=1;
      exception
        when others then
            if sqlcode IN (-1555,-8180,-1466) then
                exit;
            else
                raise_application_error(sqlcode, 'unexpected exception code: '||-20000-sqlcode);
            end if;
      end;
  end loop;
  return maxhours-1;
end mh_asof_retention;
