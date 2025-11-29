# main.py
import sys
import os

# Ajouter les modules au path Python
sys.path.extend([
    os.path.join(os.path.dirname(__file__), 'module-snmp'),
    os.path.join(os.path.dirname(__file__), 'module-negios'),
    os.path.join(os.path.dirname(__file__), 'module-wireshark'),
    os.path.join(os.path.dirname(__file__), 'interface-python')
])

from interface_python.main_app import main

if __name__ == "__main__":
    main()