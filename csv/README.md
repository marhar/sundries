```
csv2awk simple.csv
FirstName~~~LastName~~~Title~~~ReportsTo.Email~~~Birthdate~~~Description
Tom~~~Jones~~~Senior Director~~~buyer@salesforcesample.com~~~1940-06-07Z~~~Self-described as "the top" branding guru on the West Coast
Ian~~~Dury~~~Chief Imagineer~~~cto@salesforcesample.com~~~~~~World-renowned expert in fuzzy logic design. Influential in technology purchases.

csv2awk --skip-header simple.csv
Tom~~~Jones~~~Senior Director~~~buyer@salesforcesample.com~~~1940-06-07Z~~~Self-described as "the top" branding guru on the West Coast
Ian~~~Dury~~~Chief Imagineer~~~cto@salesforcesample.com~~~~~~World-renowned expert in fuzzy logic design. Influential in technology purchases.

csv2awk --skip-header simple.csv |awk '-F~~~' '{print NF}'
6
6
```
