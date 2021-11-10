Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlob
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import matplotlob
ModuleNotFoundError: No module named 'matplotlob'
>>> import matplotlib
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib
>>> import matplotlib.pyplot as plt
>>> x =[1,2,3, 4]
>>> y = [1500, 1800, 2000, 2100]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x7f955147bb20>]
>>> plt.show()
>>> legend = ["Monday", "Tuesday", "Wednesday", "Thursday"]
>>> plt.xticks(x, legend)
([<matplotlib.axis.XTick object at 0x7f9530163970>, <matplotlib.axis.XTick object at 0x7f9530163940>, <matplotlib.axis.XTick object at 0x7f95514dfee0>, <matplotlib.axis.XTick object at 0x7f9530197430>], [Text(1, 0, 'Monday'), Text(2, 0, 'Tuesday'), Text(3, 0, 'Wednesday'), Text(4, 0, 'Thursday')])
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x7f953019d0d0>]
>>> plt.show
<function show at 0x7f9551439940>
>>> plt.show()
>>> plt.bar(x,y)
<BarContainer object of 4 artists>
>>> plt.ylabel("sales in US")
Text(0, 0.5, 'sales in US')
>>> plt.title("My first chart")
Text(0.5, 1.0, 'My first chart')
>>> plt.show()
>>> plt.show()
>>> plt.bar(x,y)
<BarContainer object of 4 artists>
>>> plt.show()
>>> 
================================ RESTART: Shell ================================
>>> 