from Model.IV_Measurement import Experiment

exp = Experiment()
exp.load_config('Config/experiment.yml')
exp.load_daq()
exp.do_scan()
exp.save_data('data.dat')
exp.save_metadata('metadata.yml')