class Experiment:
    def load_config(self, filename):
        pass

    def load_daq(self):
        pass

    def do_scan(self):
        pass

    def save_data(self, filename):
        pass

    def save_metadata(self, filename):
        pass

    def finish(self):
        pass


if __name__ == "__main__":
    exp = Experiment()
    exp.load_config('config.txt')