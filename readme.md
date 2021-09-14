# Day1
13/09/2021

### Intro
- Formateur : Dominique LIARD - [Koor.fr](https://koor.fr)
- [Cours de Python](https://koor.fr/Python/SupportPython/slide1.wp)
- [Cours de Python-Qt](https://koor.fr/Python/SupportPythonQt/slide1.wp)
- Site officiel : [python.org](https://www.python.org)

### Env
vEnv :
```
python -m venv venv
venv\Scripts\activate.bat
pip install PySide6
pip install scipy
pip freeze > req.txt
pip install -r req.txt
```
UDE :
- PyCharm (JetBrains)
- PyDev (Eclipse)
- VisualStudioCode

PEP (Python Enhancement Proposals)
- PEP 8 : Development Style Guide
- PEP 20 : Zen of Python (architecture concepts)

### POO
- See [Rational.py](src/Rational.py) (language, objects, typing)
- See [Typing.py](src/Typing.py) (typing)
- Static typing analysis : `mypy Rational.py Typing.py`
- See [Person.py](src/Person.py) (heritage)



# Day 2

### Intro
- [Descriptif des modules à connaitre](https://koor.fr/Python/API/Index.wp)
- Packages (directories), modules (Py files), aliases
- [Exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

### POO suite
- See [TestExceptions.py](src/TestExceptions.py)
- See [TestWith.py](src/TestWith.py)
- Iterator implementation (for / while) using `__iter__` & `__next__`

### Testing
- See [Usage.py](src/Usage.py) -> PyDoc for doc & DocTests for testing examples
- unittest (based on JUnit3)
- 