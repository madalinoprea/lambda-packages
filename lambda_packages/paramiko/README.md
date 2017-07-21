## Build

`./build.sh paramiko 2.1.2`

```bash
docker run --paramiko -v "$PWD":/var/task lambci/lambda:build-python2.7 ls -al
```
