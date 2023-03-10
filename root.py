import ROOT

# Load the shared library containing MyClass.
ROOT.gSystem.Load('libMyLibrary.so')

# Instantiate MyClass.
obj = ROOT.MyClass(42)

# Call the Print() method.
obj.Print()
