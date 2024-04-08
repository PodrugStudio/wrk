## List all users (cli)
> https://www.virtualmin.com/documentation/developer/cli/list_users/

Run as root
```sh
virtualmin list-users --domain placa.studenac.hr --email-only > created.txt
```

```sh
virtualmin list-users --all-domains | --domain name | --domain-user username
                     [--multiline | --name-only | --email-only]
                     [--include-owner]
                     [--user name]
                     [--simple-aliases]
```
