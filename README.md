# decidim-pilot-connector

[![Build Status](https://travis-ci.com/DECODEproject/decidim-pilot-connector.svg?branch=master)](https://travis-ci.com/DECODEproject/decidim-pilot-connector)
[![codecov](https://codecov.io/gh/DECODEproject/decidim-pilot-connector/branch/master/graph/badge.svg)](https://codecov.io/gh/DECODEproject/decidim-pilot-connector)



## run

    docker build -t decidim-pilot-connector .
    docker run --rm -it -p 80:80 decidim-pilot-connector
    
## docs

After you run the docker file on your docker ip (`docker inspect`) just point to `http://127.0.0.1/docs`
