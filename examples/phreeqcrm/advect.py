"""Example 11 - advection."""


from matplotlib import pyplot as plt
from phreeqpy.phreeqcrm.rm_model import PhreeqcRMModel


def advect(model, bc_conc):
    """Shift concentrations by one cell."""
    model.update()
    data = model.concentrations.values_2d
    data[:, 1:] = data[:, :-1]
    data[:, 0] = bc_conc
    model.write_conc_back()


def run_model(file_name):
    """Run advection model."""
    model = PhreeqcRMModel(file_name)
    model.update()
    bc_conc = model._rm.InitialPhreeqc2Concentrations([0])
    nsteps = 100
    molalities = {'Na': [], 'Cl': [], 'K': [], 'Ca': []}
    pore_volumes = []
    for step in range(1, nsteps + 1):
        advect(model, bc_conc)
        for name in molalities:
            molalities[name].append(model.get_molality(name)[-1] * 1000)
        pore_volumes.append((step + 1.5) / model.number_of_cells)
    return molalities, pore_volumes


def plot_molalities(molalities, pore_volumes):
    """Plot the molalities."""
    _, ax = plt.subplots()
    for name, value in molalities.items():
        ax.plot(pore_volumes, value, label=name)
    ax.set_xlabel('Pore volumes')
    ax.set_ylabel('Millimoles per kilogram water')
    ax.legend()
    plt.show()


def main():
    """Run and plot."""
    molalities, pore_volumes = run_model('ex11-advect.yaml')
    plot_molalities(molalities, pore_volumes)


if __name__ == '__main__':
    main()
