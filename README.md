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
Install libraries by running shell script install.sh


## Running the tests

Download the innovacer_code.py and secret.py.
Edit secret.py by enetering your email-id and password (senders) also your mysql connector password.

After downloading run following command in the same directory where you have downloaded it.
  #python36 innovacer_code.py

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
1. A database is maintained of all the input email-id and corresponding tv_series


## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

