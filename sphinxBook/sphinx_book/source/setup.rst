安裝編輯環境
==================



Python和Sphinx
+++++++++++++++

首先到Python的官方網站下載並安裝2.6或2.7系列的Python運行環境。

.. tlink::
    
    http://python.org/getit/
    
    Python的下載地址

Sphinx是一套使用reStructuredText作為標記語言的文檔生成工具。本環境所提供的所有插件均可在Sphinx v1.1.2中正常使用，如果需要單獨升級Sphinx庫，可以在控制臺中輸入如下命令：

.. code-block:: none

    easy_install -U sphinx

如果高版本的Sphinx無法正確運行插件，請使用如下命令安裝1.1.2版本的Sphinx：

.. code-block:: none

    easy_install sphinx==1.1.2

.. topic:: reStructuredText

    restructuredText是一種簡單易用的所見即所得的純文本標記語法。可以通過轉換工具將其轉換為HTML、latex、PDF等多種格式。通常restructuredText的副檔名為"rst"。

Leo
++++

Leo是一個用Python編寫的提綱式程式編輯器，我們用它組織和編輯構成書籍內容的reStructuredText文檔，並管理Sphinx的插件程式、HTML範本以及配置文檔等。

.. tlink::

    http://sourceforge.net/projects/leo/files/Leo/
    
    Leo的下載位址，可以下載根源程式版或打包版，由於系統中已經安裝了Python環境，因此推薦安裝根源程式版

MiKTeX
++++++

.. tlink::

    http://miktex.org/
    
    MiKTex是一個Windows下的Tex編譯環境，我們用它將Sphinx自動生成的LaTex原始檔案編譯成PDF檔
    
安裝完成之後，執行：

.. code-block:: none

    xelatex sample.tex
    
就可以將“sample.tex”編譯成“sample.pdf”。

書籍目錄
++++++++++++

.. _sec-book-folder:


.. tlink::

    http://hyry.dip.jp/files/books.zip
    
    下載本書的編輯環境

編寫書籍專案的目錄結構如下：

.. code-block:: none

    [books]
        master.leo     -- 管理所有內容的leo檔    
        [exts]         -- 插件和範本
        [sphinxbook]   -- 本書的文件夾
        [xxxbook]      -- 其他書籍的文件夾

其中exts檔夾中包含了所有Sphinx插件程式以及LaTex和HTML的範本。而其他文件夾均為Sphinx書籍的文件夾。每本書籍的目錄結構如下：

.. code-block:: none

    [sphinxbook]
        make.bat      -- 編譯書籍的批次處理腳本
        [source]      -- 書籍的原始檔案
            conf.py   -- 書籍配置
            *.rst     -- 各個章節的reStructuredText檔
            [images]  -- 保存所有插圖的檔夾
            [codes]   -- 保存所有代碼的檔夾
        [build]
            [latex]   -- PDF的編譯輸出檔夾
            [html]    -- HTML的編譯輸出檔夾
            
在書籍檔夾下運行“make.bat html”命令將書籍編譯成HTML格式，而運行“make.bat latex”則編譯成LaTex格式。這些命令可以通過Leo的按鈕工具欄(\ :ref:`sec-leo-buttons`\ )運行。 

.. twarning::

    為了保證程式能正常運行，請保證所有路徑中沒有空格或中文。

字體
++++++

使用合適的字體可以使編輯環境用起來更舒適，使書籍更容易閱讀。在“master.leo”中使用“YaHei Mono”字體，它中文字體採用微軟雅黑，英文字體採用等寬的Consolas字體。可以通過如下節點中的QT樣式表修改Leo編輯器所使用的字體：

.. code-block:: none

    @chapters-->@settings-->qtGui plugin-->@data qt-gui-plugin-style-sheet
    
.. tlink::

    yahei_mono.7z
    
    YaHei Mono字體：中文字體採用微軟雅黑，英文字體採用等寬的Consolas字體
    
書籍的HTML版本的字體可以通過書籍範本的樣式表進行修改，而PDF版本的字體通過書籍配置檔“conf.py”中的latex_preamble配置進行修改，例如本書中採用如下字體配置：

.. code-block:: none

    \setCJKsansfont[BoldFont={STXihei},ItalicFont={STXihei}]{STXihei}
    \setCJKromanfont[BoldFont={STXihei},ItalicFont={STXihei}]{STXihei}
    \setCJKmainfont[BoldFont={STXihei},ItalicFont={STXihei}]{STXihei}
    \setCJKmonofont[BoldFont={STXihei},ItalicFont={STXihei}]{STXihei}

STXihei字體的中文名為華文細黑，在網路上可以搜索到它的下載位址。

