


import numpy as np
import argparse
import matplotlib.pyplot as plt
import scipy.integrate as integrate


# Top-hat window in Fourier space
def W_tophat(kR):
    kR = np.where(kR == 0, 1e-10, kR)  # avoid divide by zero
    return 3 * (np.sin(kR) - kR * np.cos(kR)) / kR**3

def sigma_r(k, Pk, R):
    """Compute sigma_R from 1D P(k)"""
    W = W_tophat(k * R)
    integrand = k**2 * Pk * W**2
    return np.sqrt(integrate.simpson(integrand, k) / (2*np.pi**2))

def compute_pk(tk_file, n_s, sigma8_target, h):
    # Read CLASS tk.dat (positive k only)
    data = np.loadtxt(tk_file)
    k_hmpc = data[:, 0]           # k in h/Mpc
    T_tot = np.abs(data[:, 1]*data[0,1])    # total matter transfer function

    T_tot[0] = T_tot[0]/data[0,1]
    

    # Unnormalized P(k)
    Pk_unnorm = T_tot**2 * k_hmpc**n_s

    # Normalize to match sigma8
    s8_current = sigma_r(k_hmpc, Pk_unnorm, R=8.0)
    norm = sigma8_target**2 / s8_current**2
    Pk = norm * Pk_unnorm

    s8_final = sigma_r(k_hmpc, Pk, R=8.0)
    print(f"sigma_8 after normalization: {s8_final:.5f}, target: {sigma8_target}")
    print(f"Normalization factor applied: {norm:.5e}")

    return k_hmpc, Pk

def plot_pk(k, Pk, output_file="Pk_sigma8.png"):
    plt.figure()
    plt.loglog(k, Pk)
    plt.xlabel("k [h/Mpc]")
    plt.ylabel("P(k) [(Mpc/h)^3]")
    plt.title("Matter Power Spectrum normalized to sigma8")
    plt.grid(True, which="both")
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"Saved plot to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--file-cosmicic-tk-lcdm", type=str)
    parser.add_argument("--file-cosmicic-tk-wdm1", type=str)
    parser.add_argument("--file-cosmicic-tk-wdm2", type=str)
    parser.add_argument("--file-cosmicic-tk-fdm1", type=str)
    parser.add_argument("--file-cosmicic-tk-fdm2", type=str)

    parser.add_argument("--n_s", type=float, required=True)
    parser.add_argument("--sigma8", type=float, required=True)
    parser.add_argument("--h", type=float, required=True)
    parser.add_argument("--output", type=str, default="Pk_final.png")

    args = parser.parse_args()

    # Collect all provided files
    file_map = {
        "LCDM": args.file_cosmicic_tk_lcdm,
        "WDM1": args.file_cosmicic_tk_wdm1,
        "WDM2": args.file_cosmicic_tk_wdm2,
        "FDM1": args.file_cosmicic_tk_fdm1,
        "FDM2": args.file_cosmicic_tk_fdm2,
    }

    # Filter out None entries
    file_map = {k: v for k, v in file_map.items() if v is not None}

    # Enforce at least one file
    if len(file_map) == 0:
        parser.error("At least one --file-cosmicic-tk-* must be provided.")

    # Plot everything together
    plt.figure()

    for label, filepath in file_map.items():
        k, Pk = compute_pk(filepath, args.n_s, args.sigma8, args.h)
        plt.loglog(k, Pk, label=label)

    plt.xlabel("k [h/Mpc]")
    plt.ylabel("P(k) [(Mpc/h)^3]")
    plt.title("Matter Power Spectrum normalized to sigma8")
    plt.grid(True, which="both")
    plt.ylim([1e-6, 3e4])
    plt.legend()
    plt.savefig(args.output, dpi=150, bbox_inches='tight')

    print(f"Saved plot to {args.output}")

