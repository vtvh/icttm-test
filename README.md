Submission for ICTTM Tests
==========================
## Foreword
- Tested on Ubuntu 22.04 LTS
- I'm running on MacOS so I have to download two more jar files.
But still have problems so I switch to Linux
```
https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar
https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar
```
### Fresh Linux machine install guide
- Run these first
```sh
sudo -i
apt update && apt upgrade
apt install -y default-jdk python3-venv s3fs docker.io docker-compose
```
- Clone and make Python Virtual Environment
```sh
mkdir ~/_workspace && cd ~/_workspace
git clone https://github.com/vtvh/icttm-test
cd icttm-test
python3 -m venv venv && source venv/bin/activate
pip install boto3 gdown pyspark delta-spark python-dotenv
```
- Up minio container
```sh
docker-compose -f docker-compose.mino.yml up
```
- Run app
```
venv/bin/python3 app.py
venv/bin/python3 app1.py
```

## Bottom Line
*Thanks for your time, @quangicttm. Hope to see you soon*.

## My Infos
![name card](namecard.jpg)
