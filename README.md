# IMDb-Scrapper

Keep track of all our favourite seasons and their latest episodes’air time.This leads to the worst nightmare a series buff can have.This script requires email address and list of favourite TV series for multiple users as input.Store the input data in MySQLdb table(s).A single email is send to the input email address with all the appropriate response for every TV series. The content of the mail could depend on the following use cases:
  1. Exact date is mentioned for next episode.
  2. Only year is mentioned for next season.
  3. All the seasons are finished and no further details are available.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Python36 must be preinstalled
2. Mysql,mysql.connector must be preinstalled.
3. BeautifulSoup,IMDbpy should also be available.
4. Ansible must also be installed (mail is send through ansible)

### Installing

In Rhel 7.5 OS:
1. Install Mysql 




## Running the tests

Download the innovacer_code.py and secret.py.
Edit secret.py by enetering your email-id and password 
After downloading run following command in the same directory where you have downloaded it.
  #python36 innovacer_code.py


### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

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

