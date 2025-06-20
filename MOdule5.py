import argparse
import os
import zlib # pour la compression et décompression

def compress_file(source_path, destination_path):
    "compresse un fichier"
    try:
        with open(source_path, 'rb') as f_in:
            data = f_in.read()
            compresse_data = zlib.compress(data, zlib.z_BEST_COMPRESSION)
        with open(destination_path, 'wb') as f_out:
                f_out.write(compressed_data)
        original_size = os.path.getsize(source_path)
        compressed_size = os.path.getsize(destination_path)
        compression_rate = (1 - (compressed_size / original_size)) * 100
        print(f"Fichier compressé avec succès de {source_path}vers{destination_path}.")
        print(f"Taille originale: {original_size} octets")  
        print(f"Taux de compression:{compression_rate:2f}%") 
    except FileNotFoundError:
        print(f"erreur: Le fichier source'{source_path} n'a pas été trouvé.")
    except Exception as e:
        print(f"une erreur est survenue lors de la compression:{e}")

def decompress_file(source_path, destination_path):
    """décompresse un fichier."""
    try:
        with open(sourc_path, 'rb') as f_in:
            compressed_data = f_in.read()
            decompressed_data = zlib.decompress(compressed_data)
        with open(destination_path, 'wb') :
             f_out.write(decompressed_data)
        print(f"Fichier décompressé avec succès de{source_path}'vers {destination_path}'.")
    except FileNotFoundError:
        print(f"erreur: Le fichier '{source_path}'n'a pas été trouvé.")
    except zlib.error:
         print(f"Erreur: Le fichier '{source_path} n'est pas un fichier compressé valide ou corrompu.")
    except Exceptionas:
         print(f"une erreur est survenue lors de la déompression:{e}")

def main():
     """fonction pricipale pour gerer les arguments de la ligne de commande."""
     parser = argparse.ArgumentParser(description="outil de compression/decompression de fichiers.")
     parser.add_argument("action", choices=["compresser","decompresser"],
                         help="l'acto=ion a effectuer:  'compresser' ou decompresser'.")
     parser.add_argument("source",
                         help="Le chemindu fichier source.")
     
     args = parser.parser_args()

     if args.action == "compresser":
          compress_file(args.source,args.destination)
     elif args.action == "decompresser":
          decompress_file(args.source, args.destination)
if __name__=="main":
      main
        
