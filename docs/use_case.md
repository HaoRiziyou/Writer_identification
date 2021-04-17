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




# generate example
PYTHONPATH="./" python3 tools/run_generator.py -text_in 'imagine a vast sheet of paper on which straight' -input 'line1.png' -text_out 'Imagine a vast sheet of paper on which straight Lines,
Triangles, Squares, Pentagons, Hexagons, and other
figures, instead of remaining fixed in their places,
move freely about, on or in the surface, but without
the power of rising above or sinking below it,
very much like shadows-only hard with
luminous edges- and you will then have a
pretty correct notion of my country and countrymen.
Alas, a few years ago, I should have said
"my universe:" but now my mind has been
opened to higher views of things.'	
