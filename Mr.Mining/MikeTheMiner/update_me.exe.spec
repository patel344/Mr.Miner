# -*- mode: python -*-

block_cipher = None


a = Analysis(['Update.py'],
             pathex=['C:\\Users\\igalf\\OneDrive\\Documents\\GitHub\\Mr.Miner\\Mr.Mining\\MikeTheMiner'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='update_me.exe',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='logo_green.ico')
