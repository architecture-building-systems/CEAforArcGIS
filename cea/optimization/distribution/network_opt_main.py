"""
=====================================
Network optimization
=====================================

"""
from __future__ import division
import pandas as pd

__author__ = "Tim Vollrath"
__copyright__ = "Copyright 2015, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Tim Vollrath", "Thuy-An Nguyen", "Jimeno A. Fonseca"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "thomas@arch.ethz.ch"
__status__ = "Production"

class network_opt_main(object):
    """
    This class just sets-ip constants of the linear model of the distribution.
    These results are extracted form the work of Florian at the chair.
    Unfortunately his work only worked for this case study and could not be used else where
    See the paper of Fonseca et al 2015 of the city energy analyst for more info on how that procedure used to work.
    """
    def __init__(self, config, locator):
        self.pipesCosts_DHN = 0     # CHF
        self.pipesCosts_DCN = 0     # CHF
        self.DeltaP_DHN = 0         # Pa
        self.DeltaP_DCN = 0        # Pa
        self.thermallosses_DHN = 0
        self.thermallosses_DCN = 0

        network_names = config.thermal_network.network_names

        if len(network_names) == 0:
            network_names = ['']

        for network_name in network_names:
            pressure_drop_Pa = pd.read_csv(locator.get_optimization_network_layout_pressure_drop_file(config.thermal_network.network_type, network_name))
            print (pressure_drop_Pa['pressure_loss_total_Pa'].sum())
            if config.thermal_network.network_type == 'DH':
                self.DeltaP_DHN = self.DeltaP_DHN + pressure_drop_Pa['pressure_loss_total_Pa'].sum()
            if config.thermal_network.network_type == 'DC':
                self.DeltaP_DCN = self.DeltaP_DCN + pressure_drop_Pa['pressure_loss_total_Pa'].sum()

        for network_name in network_names:
            thermal_loss_sum = 0
            thermal_losses_kW = pd.read_csv(locator.get_optimization_network_layout_qloss_system_file(config.thermal_network.network_type, network_name))
            for column_name in thermal_losses_kW.columns:
                print (thermal_losses_kW[column_name].sum())
                thermal_loss_sum = thermal_loss_sum + (thermal_losses_kW[column_name].sum())*1000
            print (thermal_loss_sum)
            if config.thermal_network.network_type == 'DH':
                self.thermallosses_DHN = self.thermallosses_DHN + thermal_loss_sum
            if config.thermal_network.network_type == 'DC':
                self.thermallosses_DCN = self.thermallosses_DCN + thermal_loss_sum

        for network_name in network_names:
            thermal_loss_sum = 0
            thermal_losses_kW = pd.read_csv(locator.get_optimization_network_layout_qloss_system_file(config.thermal_network.network_type, network_name))
            for column_name in thermal_losses_kW.columns:
                print (thermal_losses_kW[column_name].sum())
                thermal_loss_sum = thermal_loss_sum + (thermal_losses_kW[column_name].sum())*1000
            print (thermal_loss_sum)
            if config.thermal_network.network_type == 'DH':
                self.thermallosses_DHN = self.thermallosses_DHN + thermal_loss_sum
            if config.thermal_network.network_type == 'DC':
                self.thermallosses_DCN = self.thermallosses_DCN + thermal_loss_sum

        print (self.DeltaP_DCN)