解決方案
============

本章列出一些在寫書過程中經常會遇到的問題。

表格
++++++

.. csv-table:: Python中的常用類型
   :header: 類型,描述,例子
   :widths: 15, 30, 30
   :quote: $ 
   :delim: |

    str|一個由字元組成的不可更改的有串列。在Python 3.x裏，字串由Unicode字元組成。|'Wikipedia', "Wikipedia"
    bytes|一個由位元組組成的不可更改的有串列。|b'Some ASCII', b"Some ASCII"
    list|可以包含多種類型的可改變的有串列|[4.0, 'string', True]
    tuple|可以包含多種類型的不可改變的有串列|(4.0, 'string', True)
    set, frozenset|與數學中集合的概念類似。無序的、每個元素唯一。|{4.0, 'string', True}, frozenset([4.0, 'string', True])
    dict|一個可改變的由鍵值對組成的無串列。|{'key1': 1.0, 3: False}
    int|精度不限的整數|42
    float|浮點數。精度與系統相關。|3.1415927
    complex|複數|3+2.7j
    bool|邏輯值。|只有兩個值：True和False

插圖
++++++

.. _sec-tips-figure:


當圖像檔案名以".*"結尾時，將根據輸出格式自動選擇圖像檔。例如，\ :ref:`fig-fftexamplerectangle`\ 採用的檔案名為“.*”，它對應兩個檔：“fft_example_rectangle.png”和“fft_example_rectangle.pdf”。輸出HTML時將選用PNG檔，而輸出PDF時將選用PDF檔。

.. code-block:: none

    .. figure:: images/fft_example_rectangle.*

.. _fig-fftexamplerectangle:

.. figure:: images/fft_example_rectangle.*
    :width: 14.0cm

    用正弦波合成矩形波
    
\ :ref:`fig-numpyaccess2d`\ 採用的檔案名為“numpy_access2d.*”，對應兩個檔：“numpy_access2d.html.png”和“numpy_access2d.latex.png”。

.. code-block:: none

    .. figure:: images/numpy_access2d.*

.. _fig-numpyaccess2d:

.. figure:: images/numpy_access2d.*
    :width: 12.0cm

    二維NumPy陣列的下標存取

插入代碼
++++++++++++

.. literalinclude:: codes/example.py    
    :linenos:
    :language: python
    :lines: 1, 3-5

.. code-block:: matlab

    %DOCLINK - Provide windows dir HREF text(clipboard)
    
    string_temp_ahead = fullfile('jar:file:///', matlabroot, 'help');
    
    clipboard('copy', href_for_codelib);

