# import ctypes
# import time
# while 1:
# WindowsError
#     EnumWindows = ctypes.windll.user32.EnumWindows

#     EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

#     GetWindowText = ctypes.windll.user32.GetWindowTextW

#     GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW

#     IsWindowVisible = ctypes.windll.user32.IsWindowVisible
#     titles = []

#     def foreach_window(hwnd, lParam):

#         if IsWindowVisible(hwnd):

#             length = GetWindowTextLength(hwnd)

#             buff = ctypes.create_unicode_buffer(length + 1)

#             GetWindowText(hwnd, buff, length + 1)

#             titles.append(buff.value)

#         return True

#     EnumWindows(EnumWindowsProc(foreach_window), 0)

    

#     for t in titles:
#         print(t)
#     time.sleep(10)
# a=IsWindowVisible("ninja")