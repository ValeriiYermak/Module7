def to_indexed(source_file, output_file):

    zapus = 0

    with open (source_file, 'r') as file:
        for line in file:
            with open (output_file, 'w') as output:
                output.write(f"{zapus}: {line}")
                zapus = zapus + 1






    
        
  