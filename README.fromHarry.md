# I - Requirements:

1/ Run the docker-compose.mino.yml file to start Minio. Additional instructions can be found here: https://min.io/docs/minio/kubernetes/upstream/ (Alternatively, you can use a different method to start Minio).

2/ After successfully starting Minio, navigate inside and create a bucket named "data". Then, generate access and secret keys for yourself.

3/ Code should be written in the two pre-configured files: download.ipynb, transform.ipynb.

4/ Write code: Use Selenium to download the file from the following link (the code should be written in the download.ipynb file): https://drive.google.com/drive/folders/1EImvKyUQ_iJCfd2h-Dxjn_sqPyDV5tFC?usp=sharing

Note: We prefer not to download and store chromedriver within our source code. Therefore, please find a suitable library to achieve this.

5/ Write code: Unzip the .zip file. Then, upload all files to the "data-raw" folder on Minio that you just created.

6/ Write code: Use Spark to connect to Minio to read the data. (I'll provide you with some hints in file transform.ipynb).

7/ Write code: Use Spark to merge the files data.json, data2.json, data3.json into a single file named result.json => Then, upload it to the "data-result" folder on Minio.

8/ Write code: Then, use Spark to read the result.json file => Display the data => You might have some duplicate data, please remove them => Display the data again after processing (Please retain the key steps you used to derive the final result).

9/ Check your results. Before eliminating duplicates it will be 19 and after duplicates will it be equal to 18? The final result is the csv file uploaded to minio or not and can the csv file be read or not.


# II. Evaluation Criteria:

1/ Ability to comprehend requirements.
2/ Self-learning capability.
3/ Accuracy of code functionality.
4/ Conformity of results to our expectations.
5/ Readability of the code and presence of comments explaining its functionalities.

# III - Suggestions
Maybe you will need to install this to using spark:

sudo apt-get install default-jdk python3-venv s3fs