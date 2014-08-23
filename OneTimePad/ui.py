from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
from PyQt4 import Qt
import sys
import keyFinder, decryptor, focusKeyFind

class myTextBox(QtGui.QPlainTextEdit):
    
    def __init__(self,label, parent = None):
        super(myTextBox, self).__init__(parent)
        self.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.connect(self,SIGNAL("textChanged()"),self,SLOT("slotTextChanged()"))
        self.label = label
        
        pull(self)


    #def _setLabel(self,label): 
    #    self._label = label

    def getLabel(self):
        return  self.label

    @pyqtSlot()
    def slotTextChanged(self):
        push(self)
        #print self.toPlainText()
        print "This"
        msg = self.textCursor().blockNumber()
        index = self.textCursor().positionInBlock()
        guess = str(self.textCursor().block().text()[index-1:index])
        
        print msg
        print index
        print guess
        print
        focusKeyFind.edit(msg,index,guess)
        #pull(self._getLabel(),self)
    
    #label = property(_getLabel,_setLabel)


class textComparer(QtGui.QWidget):
    
    def __init__(self, parent=None):
        super(textComparer, self).__init__(parent)
        
        
        #encryptedLabel = QtGui.QLabel("Encrypted Text")      
        EncryptedText = myTextBox("Encrypted Text")
        #EncryptedText.label = "Encrypted Text"
                
        KeyText = myTextBox("Encryption Key")
        #KeyText.label = "Encryption Key"

        DecryptedText = myTextBox("Decrypted Text")
        #DecryptedText.label = "Decrypted Text"

 
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(QtGui.QLabel(EncryptedText.getLabel()))
        mainLayout.addWidget(EncryptedText)
        mainLayout.addWidget(QtGui.QLabel(KeyText.getLabel()))
        mainLayout.addWidget(KeyText)
        mainLayout.addWidget(QtGui.QLabel(DecryptedText.getLabel()))
        mainLayout.addWidget(DecryptedText)
        
        #DecryptedText.connect(DecryptedText,SIGNAL("textChanged()"),DecryptedText,SLOT("slotTextChanged()"))

        self.setLayout(mainLayout)
        self.setWindowTitle("Decrypter Guess App")

def pull(self):
    textfile = self.getLabel()

    I = open(textfile +".txt", 'r')
    self.setPlainText(I.read())
    I.close()

def push(self):
    textfile = self.getLabel()

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