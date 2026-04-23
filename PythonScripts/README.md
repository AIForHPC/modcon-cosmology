# Power Spectrum Plotting Utilities

### `PowerSpectrum_CLASS`
Computes the power spectrum from the transfer function data from the `tk.dat` file in CLASS and compares it with the power spectrum data from the `pk/dat` file in CLASS for reference and comparison. This verifies that transfer functions can be converted correctly into power spectra. 

### `PowerSpectrum_CosmicIC`
Computes the power spectra from the transfer functions output by the CosmicIC code (`trasnfer\_function.txt` file) for cold, warm, and fuzzy dark matter. The warm and fuzzy dark matter transfer functions are obtained by modification of the cold dark matter function by the CosmicIC code (`Cosmology.cpp` file).

### `PowerSpectrum_CosmicIC_Gimlet_Nyx`
Plots and compares power spectra across CosmicIC, Gimlet, and Nyx spectra outputs.

### `TransferFunction`
Plots transfer function data for cold, warm, and fuzzy dark matter and compare.
