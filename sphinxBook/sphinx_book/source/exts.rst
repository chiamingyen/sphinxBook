擴展程式
============

為了讓最終的作品格式更美觀和規範，我們提供了一些Sphinx插件程式和範本，本章對這些插件和範本進行介紹。為了讓Sphinx能找到插件和範本，需要編輯書籍專案的配置檔“conf.py”中的路徑設置。在此文件開頭添加：

::

    _exts = "../../exts"
    sys.path.append(os.path.abspath(_exts))

並修改HTML範本相關的配置：

::
    
    html_theme = 'book'
    html_theme_path = [_exts +"./theme"]

LaTeX的編號
++++++++++++++

.. tcode::

    number_ref.py
    
    為LaTeX檔添加帶編號的章節和插圖參照，適合製作印刷版的PDF文檔
    
需要進行編號的插圖使用以“fig”開頭的標籤，例如：

.. code-block:: none
    
    \ :ref:`fig-leo`\ 是Leo 4.9的介面截圖。
    
    .. _fig-leo:
    
    .. figure:: images/leo.png
        :width: 12.0cm
    
        Leo的介面截圖

.. ttip::

    在Leo編輯器中，可以輸入“fig>leo”並按CTRL+1，快速生成上面的代碼。
    
需要進行引用的章節可以用以“sec”開頭的標籤，例如：

.. code-block:: none

    章節名
    ======
    
    .. _sec-test:
    
    這是一個章節。

    這是一個引用：\ :ref:`sec-test`\ 。
    
例如：關於書籍目錄的相關說明請閱讀\ :ref:`sec-book-folder`\ 。
    
.. ttip::

    為了讓章節標籤包含在章節內部，本插件對以“sec”開頭的標籤進行特殊處理，因此可以在章節名之下定義標籤。

代碼說明標籤
++++++++++++++++++

.. tcode::

    number_label.py
    
    為代碼添加如“❶❷”的說明標籤
    
為了對代碼中的重要語句進行說明，本插件對代碼中的“#❶”等進行處理。例如：

::

    import os
    print os.getcwd() #❶
    print os.environ  #❷

❶輸出當前路徑，❷輸出環境變數。   

.. ttip::

    在Leo編輯器中，可以通過輸入數位並按CTRL+1，快速輸入“❶❷”等符號。如果通過“literalinclude”命令從外部檔載入代碼段，則可以在代碼中使用“#{1}”、“#{2}”等標籤，它們會自動被轉換為對應的數位記號。
    
.. twarning::

    目前此功能只支援Python語言。

帶圖示的塊
+++++++++++++++

.. tcode::

    block.py
    
    可以在文章中間插入帶圖的塊
    
本擴展程式提供了5種圖片塊，例如：

.. code-block:: none

    .. ttip:: 
    
        這個一個小提示。
        
生成：

.. ttip:: 

    這個一個小提示。
    
.. code-block:: none
    
    .. tcode:: 
    
        example.py
        
        這是一個例副程式
  
生成：

.. tcode:: 

    example.py

    這是一個例副程式  

.. code-block:: none

            
    .. twarning:: 
    
        警告，如果你看到這個警告，那麼請無視它。
        
生成：

.. twarning:: 

    警告，如果你看到這個警告，那麼請無視它。
    
.. code-block:: none
        
    .. tlink:: 
    
        http://hyry.dip.jp
        
        歡迎訪問我們的主頁
        
生成：

.. tlink:: 

    http://hyry.dip.jp
    
    歡迎訪問我們的主頁
    
.. code-block:: none

    .. tanim::

        demo.avi
        
        這是一個動畫演示檔
        
生成：

.. tanim::

    demo.avi
    
    這是一個動畫演示檔  
    
為了添加新的圖示塊命令“tnews”，需要準備兩個圖示檔：“news.png”和“news.pdf”，將它們分別放到下面兩個目錄中：   

.. code-block:: none

    exts\latexstyle\news.pdf 
    exts\theme\book\static\news.png
    
並編輯“block.py”檔，在其中的setup()中添加：

::

    app.add_directive('tnews', MakeFileDirective("tnews"))

HTML的中文分詞
+++++++++++++++++++

.. tcode::

    chinese_search.py
    
    增加HTML的中文搜索功能
    
本擴展程式使用\ `SmallSeg <http://code.google.com/p/smallseg/>`_\ 對中文進行分詞。

插入代碼片段
++++++++++++++++++

.. tcode::

    literal_include.py
    
    修改literalinclude命令，為其添加section選項，可從根源程式中載入檔中的部分源代碼
    
    
例如程式“example.py”的內容如下：

.. literalinclude:: codes/example.py

使用下面的命令可以載入其中以“###1###”包圍的部分。

.. code-block:: none

    .. literalinclude:: codes/example.py
        :section: 1
        
結果為：

.. literalinclude:: codes/example.py
    :section: 1

自動選擇圖片
++++++++++++++++++

.. tcode::

    image.py
    
    根據輸出格式自動選擇圖像

當figure命令的圖像名參數以“.*”結尾時，Sphinx將根據輸出格式選擇合適的圖像。例如輸出HTML時優先選擇PNG圖像，而輸出PDF時優先選擇PDF圖像。本擴展程式在此基礎上，添加了通過檔案名選擇圖像的功能。具體的使用方法請參考\ :ref:`sec-tips-figure`\ 。

