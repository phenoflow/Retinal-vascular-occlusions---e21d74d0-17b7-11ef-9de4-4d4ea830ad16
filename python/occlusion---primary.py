# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F423.00","system":"readv2"},{"code":"8149.0","system":"readv2"},{"code":"5258.0","system":"readv2"},{"code":"5223.0","system":"readv2"},{"code":"21669.0","system":"readv2"},{"code":"39989.0","system":"readv2"},{"code":"4102.0","system":"readv2"},{"code":"53818.0","system":"readv2"},{"code":"21794.0","system":"readv2"},{"code":"7720.0","system":"readv2"},{"code":"5343.0","system":"readv2"},{"code":"57909.0","system":"readv2"},{"code":"861.0","system":"readv2"},{"code":"7647.0","system":"readv2"},{"code":"50242.0","system":"readv2"},{"code":"95341.0","system":"readv2"},{"code":"3602.0","system":"readv2"},{"code":"32480.0","system":"readv2"},{"code":"11928.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('retinal-vascular-occlusions-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["occlusion---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["occlusion---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["occlusion---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
