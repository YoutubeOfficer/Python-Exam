import os
import re
import win32com.client

hwp = win32com.client.gencache.EnsureDispatch('HWPFrame.HwpObject')
hwp.RegisterModule('FilePathCheckDLL', 'SecurityModule')

TDPath = "D:\\자격증"
RPath = "C:\\Users\\kimak\\Desktop\\공부"

#HWP to PDF
files = [f for f in os.listdir(TDPath) if re.match('.*[.]hwp', f)]
for file in files:
    # HWP 파일을 PDF로 바꾸는 로직
    hwp.Open(os.path.join(TDPath, file))
    pre, ext = os.path.splitext(file)
    hwp.HAction.GetDefault("FileSaveAs_S", hwp.HParameterSet.HFileOpenSave.HSet)
    hwp.HParameterSet.HFileOpenSave.filename = os.path.join(RPath, pre + ".pdf")
    hwp.HParameterSet.HFileOpenSave.Format = "PDF"
    hwp.HAction.Execute("FileSaveAs_S", hwp.HParameterSet.HFileOpenSave.HSet);

hwp.Quit()