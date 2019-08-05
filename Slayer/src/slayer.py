

import sys
from features import PdfFeatures
from classification import Training, Test
import argparse
from clustering import PdfClustering

def start_training(debug):
    '''Starts training the system.'''
    train = Training(debug)
    train.train()

def start_test(debug, folder):
    '''Starts testing the classifier.'''
    test = Test(debug)
    test.test(folder)
    test.print_results(folder)

def start_clustering(debug):
    '''Starts Clustering.'''
    clustering = PdfClustering(debug)
    clustering.perform_clustering("benign", "malicious")
    clustering.merge_occurrences()
    clustering.dump_keywords()


if __name__ == '__main__':
    '''Main of the program. '''
    parser = argparse.ArgumentParser(description = 'Malware Detector',  formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument("action", default = 'test', help = 'specifies which action to take. Choose between:\n' +
                        '1) cluster - performs clustering to get the most frequent keywords\n' + 
                        '(benign and malicious files must be put in benign and malicious folders)\n' + 
                        '2) train - trains the system (training files must be put in benign and malicious folders)\n' +
                        '3) test - tests the system (default folder is "test", to specify a different folder, use -f\n ' + 
                        '4) train_test - performs, in order, actions 2 and 3\n' +
                        '5) all - performs, in order, actions 1, 2 and 3)')
    parser.add_argument('-f', '--folder', dest = 'folder', default = 'default', help = "specifies a different folder to the default one (only for TEST)")
    parser.add_argument('-d', '--debug', dest = 'debug', type = bool, default = False, help = "runs Slayer in DEBUG mode" )
    args = parser.parse_args()
    if (args.action == 'cluster'):
        start_clustering(args.debug)
    elif (args.action == 'train'):
        start_training(args.debug)
    elif (args.action == 'test'):
        start_test(args.debug, args.folder)
    elif (args.action == 'train_test'):
        start_training(args.debug)
        start_test(args.debug, args.folder)
    elif (args.action == 'all'):
        start_clustering(args.debug)
        start_training(args.debug)
        start_test(args.debug, args.folder)
    else:
        parser.print_help()

        