# simple-libraries

## nanoGUI

nanoGUI is a simple imperative wrapper for TKinter core widgets published under the GNU General Public License.
Its goal is to provide teachers a tool to teach GUI principles to beginners.
To use nanoGUI in a Python script, download `nanoGUI.py` into your work folder and import the library into your script.
Here is a quick example:

    from nanoGUI import *
    
    init()
    
    label('Compute a sum')
    begin_horizontal()
    s = slider(0,10)
    e = entry()
    end_horizontal()
    b = button('Compute sum')
    l = label('0')
    
    def btn_action():
      n1 = get_number(s)
      n2 = get_number(e)
      set_text(l, n1 + n2)
    
    set_command(b,btn_action)
    start()
