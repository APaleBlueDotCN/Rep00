
import ROOT

file1 = ROOT.TFile("test.root", "recreate")
h1 = ROOT.TH1D("hist","the first histogram", 10, 0, 10)
for i in range(1,11):
  h1.SetBinContent(i, i)
h1.Write()
file1.Close()
