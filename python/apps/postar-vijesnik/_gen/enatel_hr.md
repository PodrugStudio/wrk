# enatel.hr
```
info:info:ent123=)(:0:1:512000
duje.peric:Duje Perić:cde3$RFV:0:1:316000
tanja.kadic:Tanja Kadić:hrvatska:0:1:2048000
test:test:12345Test09876:1:0
```

---

#info
```sh
/usr/bin/imapsync \
  --host1 178.63.74.244 --user1 info.enatel.hr --password1 '"ent123=)("' \
  --host2 localhost --user2 info.enatel.hr --password2 '"ent123=)("'
```

#duje.peric
```sh
/usr/bin/imapsync \
  --host1 178.63.74.244 --user1 duje.peric.enatel.hr --password1 '"cde3$RFV"' \
  --host2 localhost --user2 duje.peric.enatel.hr --password2 '"cde3$RFV"'
```

#tanja.kadic
```sh
/usr/bin/imapsync \
  --host1 178.63.74.244 --user1 tanja.kadic.enatel.hr --password1 '"hrvatska"' \
  --host2 localhost --user2 tanja.kadic.enatel.hr --password2 '"hrvatska"'
```

#test
```sh
/usr/bin/imapsync \
  --host1 178.63.74.244 --user1 test.enatel.hr --password1 '"12345Test09876"' \
  --host2 localhost --user2 test@enatel.hr --password2 '"12345Test09876"'
```

