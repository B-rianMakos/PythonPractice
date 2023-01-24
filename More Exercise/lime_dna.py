def get_expected_rna_sequence(generated_rna_string, count):

    test = generated_rna_string  
    rna = generated_rna_string.replace(generated_rna_string[count],"U")

    return rna
    

    

def get_first_difference_index(dna_string, generated_rna_string):

    count = 0
    for x in range(len(dna_string)):
        if generated_rna_string[x] == dna_string[x]:
            count = count +1
        else:
            return count
            
    
    


        
def get_first_mutation_index(dna_string, generated_rna_string):
    
    
    count = get_first_difference_index(dna_string, generated_rna_string)

    if generated_rna_string[count] != dna_string[count] and generated_rna_string[count] != "U":
            print("There was an error in the transcription")
            print("The expected rna sequence is")
            rna = get_expected_rna_sequence(generated_rna_string, count)
            print(rna)
            return -1
    else:
        print("the transcription worked perfectly!")
        print(dna_string + " becomes " + generated_rna_string)

        
    
            
