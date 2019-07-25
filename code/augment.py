# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

from eda import *
from tqdm import tqdm
import pandas as pd
import csv

#arguments to be parsed from command line
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input",
                required=True,
                type=str,
                help="input file of unaugmented data")
ap.add_argument("--output",
                required=False,
                type=str,
                help="output file of unaugmented data")
ap.add_argument("--num_aug",
                required=False,
                type=int,
                help="number of augmented sentences per original sentence")
ap.add_argument("--alpha",
                required=False,
                type=float,
                help="percent of words in each sentence to be changed")
args = ap.parse_args()

#the output file
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#number of augmented sentences to generate per original sentence
num_aug = 9  #default
if args.num_aug:
    num_aug = args.num_aug

#how much to change each sentence
alpha = 0.1  #default
if args.alpha:
    alpha = args.alpha


#generate more data with standard augmentation
def gen_eda(train_orig, output_file, alpha, num_aug=9):

    lines = pd.read_csv(train_orig)
    out = open(output_file,"a",newline="")
    csv_write = csv.writer(out)
    csv_write.writerow(['sentence_a','sentence_b','category'])
    for i, line in tqdm(lines.iterrows()):
        try:
            sentence_a = str(line['sentence_a'])
            sentence_b = str(line['sentence_b'])
            category = str(line['category'])
            aug_sentence_a = eda(sentence_a,
                             alpha_sr=alpha,
                             alpha_ri=alpha,
                             alpha_rs=alpha,
                             p_rd=alpha,
                             num_aug=num_aug)
            aug_sentencd_b = eda(sentence_b,
                               alpha_sr=alpha,
                               alpha_ri=alpha,
                               alpha_rs=alpha,
                               p_rd=alpha,
                               num_aug=num_aug)
            for aug_sentence_a, aug_sentence_b in zip(aug_sentence_a, aug_sentencd_b):
                csv_write.writerow([aug_sentence_a,aug_sentence_b,category])
        except IndexError:
            print("Index Error for sample " + str(i))

    print("generated augmented sentences with eda for " + train_orig + " to " +
          output_file + " with num_aug=" + str(num_aug))

#main function
if __name__ == "__main__":

    #generate augmented sentences and output into a new file
    gen_eda(args.input, output, alpha=alpha, num_aug=num_aug)