# IMDb-Scrapper

Keep track of all our favourite seasons and their latest episodes’air time.This leads to the worst nightmare a series buff can have.This script requires email address and list of favourite TV series for multiple users as input.Store the input data in MySQLdb table(s).A single email is send to the input email address with all the appropriate response for every TV series. The content of the mail could depend on the following use cases:
  1. Exact date is mentioned for next episode.
  2. Only year is mentioned for next season.
  3. All the seasons are finished and no further details are available.

### Prerequisites

1. Python36 and pip must be preinstalled
2. Mysql,mysql.connector must be preinstalled.
3. Ansible must also be installed (mail is send through ansible)

### Installing
Install libraries by running shell script install.sh,follow steps:
  1. #chmod +x install.sh
  2. #./install.sh


## Running the tests

  This set of code was tested on Rhel 7.5 OS.
  Download the imdb_code.py and secret.py.
  Edit secret.py by enetering your email-id and password (senders) also your mysql connector password.

  After downloading run following command in the same directory where you have downloaded it.
    #python36 imdb_code.py

## What is Ansible
Ansible is a radically simple IT automation engine that automates cloud provisioning, configuration management, application deployment, intra-service orchestration, and many other IT needs.Designed for multi-tier deployments since day one, Ansible models your IT infrastructure by describing how all of your systems inter-relate, rather than just managing one system at a time.It uses no agents and no additional custom security infrastructure, so it's easy to deploy - and most importantly, it uses a very simple language (YAML, in the form of Ansible Playbooks) that allow you to describe your automation jobs in a way that approaches plain English.


## Use Cases

1. Exact date is mentioned for next episode.
   ```
    Example 'Flash'
    Status:  Next episode airs on <yyyy-mm-dd>
    ```
2. Only year is mentioned for next season.
    ```
    Example 'game of Thrones'
    Status: The next season begins in <yyyy>
    ```
3. All the seasons are finished and no further details are available.
    ```
    Example 'Friends'
    Status: The show has finished streaming all its episodes.
    ```
4. No Information about the next episode's release date is mentioned,so just notify about the latest release date
    ```
    Example 'Suits'
    Status: Latest episode was released on <yyyy-mm-dd>
    ```

## Deployment
1. User input email id and tv series seprated by a comma
![alt text](https://github.com/ayu-gupta/IMDb-Scrapper/blob/master/input%20prompt.jpg)

2. A database is maintained of all the input email-id and corresponding tv_series.
![alt text](https://github.com/ayu-gupta/IMDb-Scrapper/blob/master/input_data%20.jpg)

3. Mail is sent through ansible playbook to each user stating satus of each tv-series.
![alt text](https://github.com/ayu-gupta/IMDb-Scrapper/blob/master/mail%20output.jpg)


