>>> sheet = file.parse('sales')
>>> print(sheet)
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400
>>> type(sheet)
<class 'pandas.core.frame.DataFrame'>
>>> print(sheets.Date)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(sheets.Date)
NameError: name 'sheets' is not defined
>>> print(sheet.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]
>>> sheet.Amount.sum()
10517
>>> sheet.loc[0]
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object
>>> sheet.loc[0, "Amount"]
1340
>>> sheet.set_index("Customer", inplace=True)
>>> sheet.loc
<pandas.core.indexing._LocIndexer object at 0x7f7f187e5f90>
>>> sheet.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900
>>> sheet = sheet.reset_index()
>>> sheet["Invoice"]
0     98
1     99
2    100
3    101
4    102
Name: Invoice, dtype: int64
>>> type(sheet["Invoice"])
<class 'pandas.core.series.Series'>
>>> sheet.loc[sheet["Invoice"] ==99)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> sheet.loc[sheet["Invoice"] ==99]
   Customer       Date  Invoice  Amount
1  MMC Inc. 2018-12-10       99    1900
>>> sheet.loc[sheet["Amount"] >2000)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> sheet.loc[sheet["Amount"] >2000]
           Customer       Date  Invoice  Amount
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet.loc[sheet["Amount"].idxmax()]
Customer       Steel & Iron LLC
Date        2018-12-21 00:00:00
Invoice                     102
Amount                     3400
Name: 4, dtype: object
>>>  sheet.loc[sheet["Amount"].idxmax()["Customer"]
	   
SyntaxError: unexpected indent
>>> sheet.loc[sheet["Amount"].idxmax()["Customer"]

h
	  
SyntaxError: invalid syntax
>>> sheet.loc[sheet["Amount"]>1800]
           Customer       Date  Invoice  Amount
1          MMC Inc. 2018-12-10       99    1900
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet.loc[sheet["Amount"]>1800]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)
>>> sheet.loc[sheet["Amount"]>1800]["Customer"].unique()[0]
'MMC Inc.'
>>> 
