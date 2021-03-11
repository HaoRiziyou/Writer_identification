#use case

#make the lbpfeatures to install the dependency

see thirdparty/wi_19/srslbp/bilde



#extract features

./thirdparty/wi_19/srslbp/bilde/src/lbpFeatures2  -T otsu -r 1 2 3 4 5 6 7 8 9 10 11 12 -s bilinear -i ./data/#where the origin data saved  >the binary features saved file

#srslbp 
./thirdparty/wi_19/srslbp/srs_lbp.py -validation_csv=data/#where the feature data -output=#submission.csv 

or

./tools/full_pipeline_wi.py -validation_csv=#data.csv -output=#submission.csv


# evaluate

./tools/wi19evaluate -submission_csv=dm.csv -gt_csv=gt.csv
	
