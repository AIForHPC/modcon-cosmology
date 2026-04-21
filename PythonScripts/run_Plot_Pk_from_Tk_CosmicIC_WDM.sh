LABEL0='CDM'
LABEL1='$m_{\mathrm{wdm}}=0.85\,\mathrm{keV}$'
LABEL2='$m_{\mathrm{wdm}}=2.1\,\mathrm{keV}$'

python3 Plot_Pk_from_Tk_CosmicIC.py \
  --tk-files \
    /pscratch/sd/n/nataraj2/Nyx/cosmo-suite/modcon-cosmology/NyxRuns/LyA_1024_20Mpcbyh_LCDM/cosmicic/transfer_function_LCDM.txt \
    /pscratch/sd/n/nataraj2/Nyx/cosmo-suite/modcon-cosmology/NyxRuns/LyA_1024_20Mpcbyh_WDM/cosmicic/transfer_function_WDM_p85.txt \
    /pscratch/sd/n/nataraj2/Nyx/cosmo-suite/modcon-cosmology/NyxRuns/LyA_1024_20Mpcbyh_WDM/cosmicic/transfer_function_WDM_2p1.txt \
  --labels "$LABEL0" "$LABEL1" "$LABEL2" \
  --n_s 0.96 \
  --sigma8 0.83 \
  --h 0.675 \
  --output Comparison_Pk_LCDM_WDM.png
