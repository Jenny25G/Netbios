└─# rpcclient -U "" 192.168.86.129
Password for [WORKGROUP\]:
rpcclient $> querydomainfo
command not found: querydomainfo
rpcclient $> querydominfo
Domain:         WORKGROUP
Server:         METASPLOITABLE
Comment:        metasploitable server (Samba 3.0.20-Debian)
Total Users:    35
Total Groups:   0
Total Aliases:  0


rpcclient $> enumdomusers
user:[games] rid:[0x3f2]
user:[nobody] rid:[0x1f5]
user:[bind] rid:[0x4ba]
user:[proxy] rid:[0x402]
user:[syslog] rid:[0x4b4]
user:[user] rid:[0xbba]
user:[www-data] rid:[0x42a]
user:[root] rid:[0x3e8]
user:[news] rid:[0x3fa]



rpcclient $> queryuser root
        User Name   :   root
        Full Name   :   root
        Home Drive  :   \\metasploitable\root
        Dir Drive   :
        Profile Path:   \\metasploitable\root\profile
