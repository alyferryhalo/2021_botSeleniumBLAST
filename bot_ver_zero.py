import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

def main():
    path = "/home/alyferryhalo/Documents/code/2021/blast_parser/fasta_files/ATP5BprotSeq.fasta"
    driver = webdriver.Firefox()
    driver.get('https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome')
    download_files = driver.find_element_by_name("QUERYFILE")
    download_files.send_keys(path)
    algo_params = driver.find_element_by_id("btnDescrOver")
    algo_params.click()
    select_max_target_seq = Select(driver.find_element_by_id('NUM_SEQ'))
    select_max_target_seq.select_by_value('5000')
    blastbutton = driver.find_element_by_class_name("blastbutton")
    blastbutton.click()
    time.sleep(300)
    btnDwnld = driver.find_element_by_id("btnDwnld")
    btnDwnld.click()
    link_FASTA_aligned = driver.find_element_by_link_text('FASTA (aligned sequences)')
    link_FASTA_aligned.click()
    

if __name__ == '__main__':
    main()
