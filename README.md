# LocalPacman

![Pytest](https://github.com/cocoazawa/localPacman/actions/workflows/python-app.yml/badge.svg)  

Made by Pete Kou @ Japan  


## Licensing Notes

This project is licensed under the MIT License, and the pygame library (which this project uses) is licensed using the GNU Lesser General Public License version 2.1.  
No license infringements were intended, and the project is meant to respect the LGPL v2.1 license that the pygame library utilizes.  
A copy of the MIT License is attached with the project, and the GNU Lesser General Public License version 2.1 is available at the [Open Source Initiative's licenses website](https://opensource.org/license/lgpl-2-1/) or at the [GNU's license website](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html#SEC1).  


## Code Structure

The code is mainly structured like this (so-far):  

```bash
.
├── main.py  
│   ├── Import CPM (Core Pacman Movement)  
│   ├── Import pygame (pygame, duh)  
│   ├── Rendering the window  
│   ├── Rendering pacman  
│   └── Processing Movements (sends coordinates to CPM)  
└── CPM.py  
    ├── turnDetect (checks if the turn is valid)  
    └── collisionPrevent (sends kill signal if the pacman collides)  
```


### NJunctions Coordinates

```python
"""
junctionsNXUp = [40, 40, 40, 40, 40, 40, 64, 64, 64, 64, 64, 64, 64, 64, 64, 102, 102, 139, 139, 139, 139, 139, 176, 176, 176, 176, 176, 176, 179, 179, 179, 179, 179, 179, 220, 220, 220, 220, 220, 220, 222, 222, 222, 222, 222, 222, 222, 259, 259, 259, 259, 259, 297, 334, 334, 334, 334, 334, 334, 334, 334, 334, 361, 361, 361, 361, 361, 361]
junctionsNXDown = [40, 40, 40, 40, 40, 40, 64, 64, 64, 64, 64, 64, 64, 64, 102, 102, 139, 139, 139, 139, 139, 176, 176, 176, 176, 176, 176, 179, 179, 179, 179, 179, 179, 220, 220, 220, 220, 220, 220, 222, 222, 222, 222, 222, 222, 259, 259, 259, 259, 297, 297, 334, 334, 334, 334, 334, 334, 334, 334, 334, 361, 361, 361, 361, 361, 361]
junctionsNXLeft = [40, 40, 40, 40, 40, 40, 40, 40, 40, 64, 64, 64, 102, 102, 102, 139, 139, 139, 139, 176, 179, 220, 220, 220, 220, 220, 222, 222, 222, 222, 259, 297, 297, 297, 297, 334, 334, 334, 361, 361]
junctionsNXRight = [141, 216, 179, 216, 291, 103, 141, 216, 333, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 333, 179, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216, 16, 66, 103, 141, 216, 253, 291, 333, 366]
junctionsNYUp = [16, 141, 179, 216, 253, 333, 16, 66, 103, 141, 179, 216, 253, 291, 366, 16, 366, 16, 66, 141, 291, 366, 16, 103, 179, 216, 253, 333, 16, 103, 179, 216, 253, 333, 16, 103, 179, 216, 253, 333, 16, 66, 103, 179, 216, 253, 333, 16, 66, 141, 291, 366, 16, 16, 66, 103, 141, 179, 216, 253, 291, 366, 16, 141, 179, 216, 253, 333]
junctionsNYDown = [103, 141, 179, 216, 291, 366, 66, 103, 141, 179, 216, 253, 333, 366, 333, 366, 16, 103, 253, 333, 366, 66, 141, 179, 216, 291, 366, 66, 141, 179, 216, 291, 366, 16, 66, 141, 179, 216, 291, 141, 179, 216, 291, 333, 366, 16, 253, 333, 366, 333, 366, 16, 66, 103, 141, 179, 216, 253, 333, 366, 103, 141, 179, 216, 291, 366]
junctionsNYLeft = [16, 66, 103, 141, 216, 253, 291, 333, 366, 16, 179, 216, 141, 216, 291, 103, 141, 216, 333, 179, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216]
junctionsNYRight = [141, 216, 179, 216, 291, 103, 141, 216, 333, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 333, 179, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216, 16, 66, 103, 141, 216, 253, 291, 333, 366]
"""
```
