import ROOT as rt
import numpy as np

newfile = rt.TFile("test00.root", "recreate")
np.random.seed(42)
data = np.random.normal(5, 2, 1000)			
hist_1 = rt.TH1F("hist1", "Histogram_1", 75, 0, 10)
for value in data:
	hist_1.Fill(value)			
hist_1.Write()						
newfile.Close
