from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import Qt
import sys
import keyFinder, decryptor, focusKeyFind

class HelloApplication(Qt.QApplication):
 
    def __init__(self, args):
        """ In the constructor we're doing everything to get our application
            started, which is basically constructing a basic QApplication by 
            its __init__ method, then adding our widgets and finally starting 
            the exec_loop."""
        Qt.QApplication.__init__(self, args)
        self.addWidgets()
        self.exec_()        
 
    def addWidgets(self):
        """ In this method, we're adding widgets and connecting signals from 
            these widgets to methods of our class, the so-called "slots" 
        """
        self.hellobutton = Qt.QPushButton("Say 'Hello world!'",None)
        self.connect(self.hellobutton, Qt.SIGNAL("clicked()"), self.slotSayHello)
        self.hellobutton.show()
 
    def slotSayHello(self):
        """ This is an example slot, a method that gets called when a signal is 
            emitted """
        print ("Hello, World!")
 


class myTextBox(QtGui.QPlainTextEdit):
    
    def __init__(self, parent = None):
        super(myTextBox, self).__init__(parent)
        self.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.connect(self,SIGNAL("textChanged()"),self,SLOT("slotTextChanged()"))


    def _setLabel(self,label): 
        self._label = label

    def _getLabel(self):
        return  self._label

    @pyqtSlot()
    def slotTextChanged(self):
        push(self)
        #print self.toPlainText()
        print
        msg = self.textCursor().blockNumber()
        index = self.textCursor().positionInBlock()
        guess = str(self.textCursor().block().text()[index-1:index])
        
        print msg
        print index
        print guess
        print
        #focusKeyFind.edit(msg,index,guess)
        #pull(self._getLabel(),self)
    
    label = property(_getLabel,_setLabel)


class textComparer(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(textComparer, self).__init__(parent)
        
        
        #encryptedLabel = QtGui.QLabel("Encrypted Text")      
        EncryptedText = myTextBox()
        EncryptedText.label = "Encrypted Text"
                
        KeyText = myTextBox()
        KeyText.label = "Encryption Key"

        DecryptedText = myTextBox()
        DecryptedText.label = "Decrypted Text"

 
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(QtGui.QLabel(EncryptedText._getLabel()))
        mainLayout.addWidget(EncryptedText)
        mainLayout.addWidget(QtGui.QLabel(KeyText._getLabel()))
        mainLayout.addWidget(KeyText)
        mainLayout.addWidget(QtGui.QLabel(DecryptedText._getLabel()))
        mainLayout.addWidget(DecryptedText)

        pull(EncryptedText)
        pull(KeyText)
        pull(DecryptedText)
        
        #DecryptedText.connect(DecryptedText,SIGNAL("textChanged()"),DecryptedText,SLOT("slotTextChanged()"))

        self.setLayout(mainLayout)
        self.setWindowTitle("Decrypter Guess App")

def pull(self):
    textfile = self._getLabel()

    I = open(textfile +".txt", 'r')
    self.setPlainText(I.read())
    I.close()

def push(self):
    textfile = self._getLabel()

    O = open(textfile +".txt", 'w')
    O.write(self.toPlainText())
    O.close()
"""
# Only actually do something if this script is run standalone, so we can test our 
# application, but we're also able to import this program without actually running
# any code.
if __name__ == "__main__":
    app = HelloApplication(sys.argv)        
"""
if __name__ == '__main__':
 
    app = QtGui.QApplication(sys.argv)
 
    helloPythonWidget = textComparer()
    helloPythonWidget.show()
 
    sys.exit(app.exec_())