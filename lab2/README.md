# Results

## Summary Statistics

Summary statistic were obtained from the MPG data for both the current and proposed fleets:

### Current Fleet
* Mean: 20.144578
* Median: 19.000000
* Var: 40.983113
* std: 6.401805
* MAD: 4.000000

### Proposed Fleet
* Mean: 30.481013
* Median: 32.000000
* Var: 36.831918
* std: 6.068931
* MAD: 4.000000

## Scatter Plot and Histograms for Fleet MPG Data

### Scatter Plot

A scatter plot was created from the current and proposed fleet MPG data found in `vehicles.csv'. It visually presents the change in MPG obtained by upgrading the current fleet.

![logo](./scaterplot_vehicles.png?raw=true)

### Histograms

A histogram was created for each of the current and proposed fleets to illustrate the deviation in MPG amongst the vehicles.

![logo](./histogram_vehicles_current_fleet.png?raw=true)
![logo](./histogram_vehicles_proposed_fleet.png?raw=true)

## Standard Deviation Comparison via the Bootstrap

Upper and lower bounds and the mean was calculated for the standard deviation of both the current fleet MPG data and the proposed fleet MPG data using bootstrapping over 100,000 samples.

* Current Fleet
	* STD Mean: 6.383275
	* STD Lower Bound: 5.806590
	* STD Upper Bound: 6.950165
* Proposed Fleet
	* STD Mean: 6.011853
	* STD Lower Bound : 5.143167
	* STD Upper Bound: 6.910813
	
The current fleet shows greater standard deviation but with bounds tending towards higher MPG values.