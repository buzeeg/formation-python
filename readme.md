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
- See [HelloWorld.py](qt/HelloWorld.py)
- Styling with [CSS file](qt/styles.css)  
  `python HelloWorld.py -stylesheet styles.css`
- See [QAppWithToolbars.py](qt/AppWithToolbars.py)


# Day 3

### Qt Widgets intro, Layouts
- See [QAppWithToolbars.py](qt/AppWithToolbars.py) and [QButtonBlock.py](qt/ButtonBlock.py) : refactor, add central widget, context menu
- See [DBPropertiesDialog.py](qt/DBPropertiesDialog.py) : BoxLayouts, QFormLayout
- See [CalcGridDialog.py](qt/CalcGridDialog.py) : GridLayout
- Signal/Slot (publisher/subscriber), Events (override)
  - Slots historic syntax (C) :
    ``` python
      QObject.connect(self, __button1, SIGNAL('clicked()'), self.slot1)
    ```
  - Slots modern syntax (Python) :
    ``` python
      self.__button1.clicked.connect(self.slot1)
    ```

# Day 4

### Reminders
- Static members & custom signals - see [StaticMembers.py](src/StaticMembers.py), FileWatcher demo (using QThread)

### Qt Widgets & Dialogs
- QRadioButton & QGroupBox, QProgressBar, QSlider
- RGB demo with sliders - see [RGBSelectorDisplay.py](qt/RGBSelectorDialog.py)
- Splitter & Mdi interface (see app)
- Standard Dialogs : QMessageBox, QInputDialog, QFileDialog, QColorDialog, ... (see app)

### Qt Views
- MVC pattern -> QListView, QTableView, QTreeView
  - See [SqlTableModel.py](qt/SqlTableModel.py) & [SqlTableView.py](qt/SqlTableView.py)

# Day 5

### Qt with DB, Models & View
- MariaDB install
- SQL test data : [database.sql](data/database.sql)
- Python SQL interaction :
  - Sql direct orders (base API), including sqlite3 server & driver
  - ORM (cf [Koor.fr/Accès aux données en Python](https://koor.fr/Python/SupportPythonData/slide1.wp))
    - Django Orm
    - Sql Alchemy
- Driver MySQL/Maria : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
- See [DatabaseManager.py](qt/DatabaseManager.py)
- Data display in main app using New Document : see [QAppWithToolbars.py](qt/AppWithToolbars.py)
- Model with multiple Views [Models.py](qt/Models.py)

### Custom widget
- Draw custom widget by overriding paintEvent method and using QPainter object

### Qt Designer
- Qt Creator (C++ & Python) -> IDE
- Qt Designer : see [DBPropDlg.ui](qt/ui/DBPropDlg.ui)
- Python code gen : `pyside6-uic qt\ui\DBPropDlg.ui >qt\ui\DBPropDlg.py`
- Integration in application : using heritage or aggregation (`Ui_Dialog.setupUi`)

### SciPy stack
- SciPy stack : for scientific computing (matlab replace)
  - NumPy : numeric computing
  - SciPy library : algorithmic
  - Matplotlib : data display
  - pandas : statistics
- Not compatible to PySide6 -> PySide2
- Basic graphs : [sinus.py](matplotlib/sinus.py), [Mesh.py](matplotlib/Mesh.py)
- Integration in QApp : [CurveWindow.py](matplotlib/CurveWindow.py)
