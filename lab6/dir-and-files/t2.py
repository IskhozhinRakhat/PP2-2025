import os
print('Exist:', os.access("C:\Users\Рахат\Desktop\PP2-2025", os.F_OK))
print('Readable:', os.access("C:\Users\Рахат\Desktop\PP2-2025", os.R_OK))
print('Writable:', os.access("C:\Users\Рахат\Desktop\PP2-2025", os.W_OK))
print('Executable:', os.access("C:\Users\Рахат\Desktop\PP2-2025", os.X_OK))