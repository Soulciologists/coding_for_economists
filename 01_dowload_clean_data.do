copy "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv" "data/raw/european_commission/ted-sample.csv", replace
copy "https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/country-codes.csv" "data/raw/european_commission/country-codes.csv", replace

import delimited "data/raw/european_commission/ted-sample.csv", clear

*only keep relevant variables
keep iso_country_code win_country_code award_value_euro

*summarize award_value_euro
summarize award_value_euro, detail
display "Numver of observarions: `r(N)'"
display "Mean: `r(mean)'"

* Let's generate an indicator: 1 (above mean), 0 otherwise
gen above_mean = 1
replace above_mean = 0 if award_value_euro < `r(mean)'

*Drop if outliers
drop if `r(p95)'

* plot the distribution of award_value_euro
hist award_value_euro

* Let's generate an indicator:1 above median , 0 otherwise
gen above_median = (award_value_euro > `r(p50)')

* looping in stata

* forvalues loop
forvalues i = 0/9 {
	display `i'
}

* foreach loop
foreach vegetable in paprika aubergine carrot {
	display "`vegetable'"
}

foreach var of varlist iso_country_code win_country_code {
	count if strlen(`var') > 2
}