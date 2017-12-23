# python\_textbook\_practice

- CH2 資料型別、變數與運算子
	* Python 資料型別
	* 變數
	* 運算子
	* 字串
- CH3 Python 的資料儲存容器
	* tuple
	* list(串列)
	* dict(字典)
	* set(集合)
- CH4 選擇結構
	* if
	* if-else
	* if-elif-else
	* in
- CH5 迴圈與生成式
	* for
	* while
	* 巢狀迴圈
	* break、continue、else
	* for item in tuple/list/dict
	* comprehension(生成式)
		- `[]` 表示產生**串列**
			* e.g. `[ x for x in range(1,6) ]`
			* e.g. `[ x for x in range(1,11) if x%2 == 1 ]`
		- `{}` 表示產生**字典**
			* e.g. 
			```python
			word = 'elephant'
			{ letter : word.count(letter) for letter in set(word) }
			```
		- `{}` 表示產生**集合**
			* e.g. 
			```python
			word = 'elephant'
			{ letter for letter in word }
			``` 
	* generator(產生器)
		- 使用`(...)`作為產生器
			* 這**不是** tuple 產生器
		- 產生器只能執行一次，執行第二次不會產生任何值
		- e.g. `( x for x in range(1,10) if (x%2) == 1 )`
- CH6 函式與遞迴
	* 函式的說明文件
	* 函式視為物件
	* 函式lambda
		- e.g. `sort_num = sorted( num_dic, key = lambda x: x[3], reverse = True )`
	* 內部函式
	* closure 函式
		- 在函式內部動態建立一個函式，回傳該函式
		- 好處：內部函式能夠存取外部函式的參數
	* Decorator (裝飾器)
		- e.g. `@decorator`
	* 遞迴
		- 呼叫自己
		- 需要有終止條件
			* 否則會變成無窮迴圈 QAQ
- CH7 模組、套件與獨立程式：	
	* 模組 module ： 一個 .py 的 python 檔案
		- 內容：1 至 多個 函式 (def 所定義的)
		- 使用方法：
			* `from 模組 import 函式名稱`：只匯入模組中的其中一個函式
			* `import 模組名稱`：匯入整個模組				
	* 套件 package：一個 資料夾
		- 內容：多個模組、`__init__.py` 檔(內容可以是空的)
		- 使用方法：
			```python
			from 套件名稱 import 模組名稱
			模組名稱.函式名稱()
			```
	* 腳本程式 Script：??看不懂

- CH8 類別與例外
	* 8-1 類別
		1. 實作類別
		2. 繼承
			- 定義繼承關係：`class 衍伸類別-子類別 (基礎類別-雙親類別)`
			- 呼叫基礎類別的函式：`super().基礎類別的函式`
		3. 覆寫函式
			- Do：在衍伸類別內，重新修改基礎類別的函式
			- For：衍伸類別與基礎類別的**相同函式有不同的功能**
		4. 新增參數的覆寫函式
			- Do：覆寫函式時，新增參數
		5. 新增函式
			- Do：在衍伸類別內，**新增基礎類別沒有的函式**
		6. 多型(polymorphism)
			- 多個類別可以定義**相同的**函式名稱
			- 而相同的函式名稱在不同類別可以定義**各自特有的功能**
				* call：物件的函式名稱
				* output：不同的物件都定義此 相同函式名稱 而產生的**不同功能**
			- python 中，類別不一定要有繼承關係		7. 類別內**無法**直接存取的變數
			- 目的：資料保護
			- 用法：變數名稱前加上 `__`
				- e.g.`__變數名稱`
			- 作用：其他物件 無法直接使用 `類別物件.__變數名稱` 來存取
			- 解法：需要在類別內定義函式，回傳 `self.__變數名稱` 才能讓 其他物件 存取到該變數
		8. 特殊函式(special method)
			- 運算子('=='、'!='...)或內建函式
			可以與[特殊函式](https://docs.python.org/3/reference/datamodel.html#special-method-names)
			(`__eq__`、`__ne__`)自動對應
			- 詳見表格
		9. 組合(composition)
			- 類別與類別間不全然是繼承關係
			- 也可能 類別A 是 類別B 的一部分
				- ex. 腳是動物的一部分，但腳不是動物，腳無法繼承動物
				- 因此在 動物類別 初始化時，將 腳 當成參數傳入，讓 腳 為 動物 的一部分
		10. 類別方法(class method)
			- 作用對象：類別(class)
			- 影響：整個類別、類別所產生的物件
			- 類別方法：
				* 第一個參數：通常取名為`cls`
				* 需在類別中，函式的前一行使用裝飾器`@classmethod`
			- 實例方法(instance method):
				* 第一個參數都是 `self`
		11. 靜態方法(static method)
			- 讓類別不需要建立物件，就可以直接使用該類別的靜態方法
			- 需在類別中，函式的前一行使用裝飾器`@staticmethod`
				
|                     |特殊函式                    |對應的運算子         |
|---------------------|----------------------------|---------------------|
|比較運算             |\__eq\__(self, other)       |self == other        |
|                     |\__ne\__(self, other)       |self != other        |
|                     |\__gt\__(self, other)       |self > other         |
|                     |\__ge\__(self, other)       |self >= other        |
|                     |\__lt\__(self, other)       |self < other         |
|                     |\__le\__(self, other)       |self <= other        |
|邏輯運算             |\__add\__(self, other)      |self + other         |
|                     |\__sub\__(self, other)      |self - other         |
|                     |\__mul\__(self, other)      |self * other         |
|                     |\__truediv\__(self, other)  |self / other         |
|                     |\__floordiv\__(self, other) |self // other        |
|                     |\__mod\__(self, other)      |self % other         |
|算術與邏輯運算       |\__pow\__(self, other)      |self ** other        |
|                     |\__lshift\__(self, other)   |self << other        |
|                     |\__rshift\__(self, other)   |self >> other        |
|                     |\__and\__(self, other)      |self & other         |
|                     |\__or\__(self, other)       |self  l  other        |
|                     |\__xor\__(self, other)      |self ^ other         |
|                     |\__len\__(self)             |len(self)            |
|                     |\__str\__(self)             |str(self)            |
|                     |\__[repr](https://www.pythoncentral.io/what-is-the-difference-between-__str__-and-__repr__-in-python/) \__(self) |repr(self) |
		
- CH9
- CH10
- CH11
- CH12