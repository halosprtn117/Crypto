import sys
from PyQt4 import Qt
 
class HelloApplication(Qt.QApplication):
 
    def __init__(self, args):
        """ In the constructor we're doing everything to get our application
            started, which is basically constructing a basic QApplication by 
            its __init__ method, then adding our widgets and finally starting 
            the exec_loop."""
        Qt.QApplication.__init__(self, args)
        self.encryptedWidget()
        self.exec_()        
 
    def encryptedWidget(self):
        """ In this method, we're adding widgets and connecting signals from 
            these widgets to methods of our class, the so-called "slots" 
        """
        self.encryptedLabel = QtGui.QLabel("Encrypted Text")      
        self.EncryptedText = QtGui.QPlainTextEdit()
        self.EncryptedText.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        
        self.connect(self.EncryptedText, Qt.SIGNAL("textChanged ()"), self.decryptor)
        self.EncryptedText.show()
 
    def decrpyt(self):
        """ This is an example slot, a method that gets called when a signal is 
            emitted """
        print "Hello, World!"
 
# Only actually do something if this script is run standalone, so we can test our 
# application, but we're also able to import this program without actually running
# any code.
if __name__ == "__main__":
    app = HelloApplication(sys.argv)