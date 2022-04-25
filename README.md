# PSA_Final_Project_Spring22
Code Repository for INFO 6205 Spring 22 Final Project

Team members:

Shashank Siripragada, Section 8 NUID: 002193773

Mayannk Kumaar, Section 8 NUID: 001537115


### This project requires installation of python 3

Please install python 3


### Testing

Before training, run all the test cases in tests.py using

`python tests.py`


### Training

To train the MENACE algorithm, run

`python game.py --mode train --iterations 1000 --probability 0.9`

- mode : train (for training mode)
- iterations : Number of iterations to train MENACE
	- iterations default : 1000
- probability : probability that the human agent opponent follows the ideal strategy
	- probability default : 0.7 (probability = 1 - epsilon, where epsilon = 0.3) 

### Play against trained MENACE

To play against the trained MENACE, run

`python game.py --mode play`

- mode : play 
	- for playing against MENACE

This will initialize a command line interface enabling user to play against MENACE