import os


class Corpus(object):

    def __init__(self):
        current_directory = os.path.dirname(__file__)
        self.data_directory = os.path.join(current_directory, 'data')

    def get_file_path(self, dotted_path):
        """
        Reads a dotted file path and returns the file path.
        """
        parts = dotted_path.split(".")
        if parts[0] == 'chatterbot':
            parts.pop(0)
            parts[0] = self.data_directory

        corpus_path = os.path.join(*parts)

        if os.path.exists(corpus_path + '.json'):
            corpus_path += '.json'

        return corpus_path

    def read_corpus(self, file_name):
        """
        Read and return the data from a corpus json file.
        """
        import json
        import io

        with io.open(file_name, encoding='utf-8') as data_file:
            data = json.load(data_file)
        return data

    def list_corpus_files(self, dotted_path):
        """

        """
        corpus_path = self.get_file_path(dotted_path)
        paths = []

        if os.path.isdir(corpus_path):
            for dirname, dirnames, filenames in os.walk(corpus_path):
                for datafile in filenames:
                    if datafile.endswith('.json'):
                        paths.append(os.path.join(dirname, datafile))
        else:
            paths.append(corpus_path)

        paths.sort()
        return paths

    def load_corpus(self, dotted_path):
        """
        Return the data contained within a specified corpus.
        """
        data_file_paths = self.list_corpus_files(dotted_path)

        corpora = []

        for file_path in data_file_paths:
            corpus = self.read_corpus(file_path)

            for key in list(corpus.keys()):
                corpora.append(corpus[key])

        return corpora
