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
- Iterator implementation (`for` / `while`) using `__iter__` & `__next__`

### Testing
- See [Usage.py](src/Usage.py) -> PyDoc for doc & DocTests for testing examples
- See [RationalTest.py](test/RationalTest.py) -> unittest (based on JUnit3)
- Tests :
  1. unit test -> unittest (component testing)
  2. integration test -> test communication between components
  3. functional tests (system validation & verification)
  4. acceptance tests (with customer)
- CI -> test cov
    ```
    coverage run Rational.py
    coverage report -m
    ```
- TDD -> interfaces from UML component diagram

### Qt intro
- Qt :
  - IHM multiplatform
  - owner : Trolltech -> Nokia -> Digia -> The Qt Company
  - version based on C++ version
  - Qt6 is last version, based on C++ ISO 2017
- 2 main bindings between Python & Qt : PyQt & PySide
  - PyQt original binding
  - PySide maintened by The Qt Company
- PySide6 is modern and official binding

### Qt Hello world
- See [HelloWorld.py](qt/QtHelloWorld.py)
- Styling with [CSS file](qt/styles.css)  
  `python HelloWorld.py -stylesheet styles.css`
- See [QAppWithToolbars.py](qt/QAppWithToolbars.py)


# Day 3

