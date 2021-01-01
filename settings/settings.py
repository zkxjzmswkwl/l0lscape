import configparser


class Settings:

    def __init__(self, path='../config.ini'):
        self._path = path

        self._config = configparser.ConfigParser()
        self._config.read(path)

    def write(self):
        """Writes current config blob to disk from memory."""

        with open(self._path, 'w') as conf_file:
            self._config.write(conf_file)

    def get(self, section, key, is_list=False):
        """Returns value from config file

        section -- str
        key     -- str
        is_list -- boolean, default = False
        """

        if is_list:
            return self._config[section].get(key).split('-')
        return self._config[section].get(key)


