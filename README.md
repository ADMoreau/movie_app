# Project Movie App [![Build Status](https://travis-ci.com/ADMoreau/movie_app.svg?branch=master)](https://travis-ci.com/ADMoreau/movie_app) [![codecov](https://codecov.io/gh/ADMoreau/movie_app/branch/master/graph/badge.svg)](https://codecov.io/gh/ADMoreau/movie_app)

This is a demo app designed to run in a web browser. It is based on a python 3.6 flask architecture and uses the IMDb python API to retrieve JSON formatted information about a movie or tv show. It was designed to be deployed on an AWS elasticbeanstalk environment.

The home index page is a simple search interface.
/search?query=${some title} will retrieve the top 20 IMDb listings based on similarity to the query.
/show/${id} will get the most similar entry to the title of a tv show. 
/movie/${id} will perform similar actions for a movie. 