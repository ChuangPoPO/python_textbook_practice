# python\_textbook\_practice

## CH2 資料型別、變數與運算子

* Python 資料型別
* 變數
* 運算子
* 字串

- - -	
## CH3 Python 的資料儲存容器

* tuple
* list(串列)
* dict(字典)
* set(集合)

- - -	
## CH4 選擇結構

* if
* if-else
* if-elif-else
* in

- - -	
## CH5 迴圈與生成式

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

- - -		
## CH6 函式與遞迴

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

- - -		
## CH7 模組、套件與獨立程式：	

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

- - -
## CH8 類別與例外

### 8-1 類別
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
 - python 中，類別不一定要有繼承關係7. 類別內**無法**直接存取的變數
 - 目的：資料保護
 - 用法：變數名稱前加上 `__`
  - e.g.`__變數名稱`
 - 作用：其他物件 無法直接使用 `類別物件.__變數名稱` 來存取
 - 解法：需要在類別內定義函式，回傳 `self.__變數名稱` 才能讓 其他物件 存取到該變數
8. 特殊函式(special method)
 - 運算子('=='、'!='...)或內建函式
  可以與[特殊函式](https://docs.python.org/3/reference/datamodel.html#special-method-names)
 (`__eq__`、`__ne__`)自動對應
 - ** 詳見下方表格 **
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
 - cf. 實例方法(instance method):
  * 第一個參數都是 `self`
11. 靜態方法(static method)
 - 讓類別**不需要建立物件，就可以直接使用**該類別的靜態方法
 - 需在類別中，函式的前一行使用裝飾器`@staticmethod`	

### 8-2 例外(exception)
 1. try-except
  - 可攔截例外
  - try 區塊：撰寫可能發生錯誤的程式
  - except 區塊：若程式發生錯誤，在這進行後續處理
 2. try-except-else
  - else 區塊：若沒有發生錯誤，跳到這繼續執行
 3. try-except-as-else
  - except ... as ...：將錯誤類別轉換成對應的錯誤類別物件
  - 可以有多個錯誤類別
 4. try-except-as-else 與 自訂例外類別
  - 自訂例外類別需繼承 Exception，該類別就會成為例外類別
   e.g. `class PwdException(Exception)`
  - 可以傳入參數
  - 使用指令 `raise` 發出例外
 5. try-except-as-else-finally 與 自訂例外類別
  - finally 區塊：不管有無發生錯誤，都會執行
	
** 8-1-8 附表 **
	
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
|                     |\__or\__(self, other)       |self  l  other       |
|                     |\__xor\__(self, other)      |self ^ other         |
|                     |\__len\__(self)             |len(self)            |
|                     |\__str\__(self)             |str(self)            |
|                     |\__[repr](https://www.pythoncentral.io/what-is-the-difference-between-__str__-and-__repr__-in-python/) \__(self) |repr(self) |


** 8-2 附表 **	
		
|錯誤類型             |說明                                                |
|---------------------|-----------------------------------------------     |
|KeyboardInterrup     |當使用者輸入中斷(`Ctrl + c`)時，發出此錯誤訊息      |
|ZeroDivisionError    |除以0時，發出此錯誤訊息                             |
|EOFError             |接受到EOF(end of file)訊息時，發出此錯誤            |
|NameError            |區域或全域變數找不到時，發出此錯誤訊息              |
|OSError              |與作業系統有關的錯誤                                |
|FileNotFoundError    |檔案或資料夾找不到的時候，發出此錯誤                |
|ValueError           |傳入資料與程式預期輸入資料之行別不同時，發出此錯誤  |

- - -
## CH9 進階字串處理

1. ASCII 編碼
 - 模組 sting ：`import string`
 - string.ascii_letters / ascii_lowercase / ascii_uppercase / 
  digits / hexdidits / octdigits / punctuation / printable / whitespace
2. Unicode 編碼
 - `import unicodedata`
 - `unicodedata.name('中文字/4個16進位/8個16進位/標準名稱')` --> Unicode 標準名稱
 - `unicodedata.lookup('標準名稱')` --> Unicode 字元
 - 編碼(encode)：將 字串 轉換為 位元組(byte)
 - 解碼(decode)：將 已編碼的位元組(byte) 轉換為 字串
3. 正規表示式(regular expression)
 - 模組 re：`import re`
  - `re.match('開頭字', string)`
  - `re.search('找第一次出現', string)`
  - `re.findall('所有符合格式的字串', string)`：回傳串列

|關鍵字  |用於：意思是                             |e.g.                      |e.g. 的結果會是                 |
|:------:|-----------------------------------------|--------------------------|--------------------------------|
|.       |表示：任何字元(Enter'\n'以外)            |'.'                       |任一個字元                      |
|*       |接在任何字元後：出現0~多次接可           |'.*'                      |所有字元(越長越好)              |
|+       |接在任何字元後：前面字元出現1次以上      |'[abc]+'                  |a或b或c至少出現一次             |
|?       |接在任何字元後：前面字元出現0~1次        |'a?'                      |a出現0或1次                     |
|^       |表示：位置在開頭                         |'^ab'                     |出現在開頭的'ab'                |
|$       |表示：位置在結尾                         |'ab$'                     |出現在句尾的'ab'                |
|[^xy]   |表示篩選：不含x 且 不含y的字             |'[^不但]'                 |篩選出不是'不'也不是'但'的其他字|
|[xy]    |表示篩選：是 x或y                        |'[好可]'                  |篩選出是'好'或'可'的字          |
|(xy)    |表示篩選：是'xy'的字串                   |'(可以){2}'               |篩選出'可以可以'                |
|x{a}    |表示{範圍}：x 連續出現 a 次              |'[可以]{2}'               |篩選出'可以'                    |
|x{a,b}  |表示{範圍}：x 連續出現 a ~ b 次          |'好{3}'                   |篩選出'好好好'                  |
|\b      |字串邊界：「\w」與「\W」的邊界           |`re.findall(r'\b','a_+b')`|字串兩邊的邊界'',''             |
|\B      |字串中 字元間邊界：非「\w」與「\W」的邊界|`re.findall('\B','a_+b')` |字元間的邊界'','',''            |

- - -
## CH10 
## CH11
## CH12