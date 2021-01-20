# Writer_identification
Fork from https://github.com/M4rt1nM4yr/spatio-temporal_handwriting_imitation.git
          https://github.com/anguelos/wi19_evaluate.git
          
          
          
./bin/src/lbpFeatures2 -T otsu -r 1 2 3 4 5 6 7 8 9 10 11 12 -s bilinear -i ./wi_comp_19_validation/*.jpg > /tmp/features.csv

./srslbp/srs_lbp.py -validation_csv=/tmp/features.csv -output=/tmp/submission.csv


./bin/wi19evaluate -submission_csv=dm.csv -gt_csv=gt.csv 
./cvl_test/0001-1-cropped.tif ./cvl_test/0002-1-cropped.tif ./cvl_test/0001-2-cropped.tif ./cvl_test/0002-2-cropped.tif  >features.csv


merge srslbp.py and bin evaluate to the tools
