## Build

`./create-build.sh`

## Test

- Deploys a lambda that imports saml and echos saml version

```bash
cd lambda;
virtualenv .env; source .env/bin/activate; pip install -r requirements.txt
zappa deploy test; zappa invoke test 'app.test_import'
```

## Errors

1. Inval
```
/var/task/dm/xmlsec/binding/_xmlsec.so: invalid ELF header
```

 - Adds xmlsec to requirements.txt to allow zappa to load lambda package
