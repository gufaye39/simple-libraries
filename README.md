# simple-libraries

## nanoGUI

nanoGUI is a simple imperative wrapper for TKinter core widgets published under the GNU General Public License.
Its goal is to provide teachers a tool to teach GUI principles to beginners.
To use nanoGUI in a Python script, download `nanoGUI.py` into your work folder and import the library into your script.
Here is a quick example:

    import nanoGUI as ng
    
    ng.init()
    
    ng.label('Compute a sum')
    ng.begin_horizontal()
    s = ng.slider(0,10)
    e = ng.entry()
    ng.end_horizontal()
    b = ng.button('Compute sum')
    l = ng.label('0')
    
    def btn_action():
      n1 = ng.get_number(s)
      n2 = ng.get_number(e)
      ng.set_text(l, n1 + n2)
    
    ng.set_command(b,btn_action)
    ng.start()
