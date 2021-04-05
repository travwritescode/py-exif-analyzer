import exifread
import pprint
import pickle
from pathlib import Path
from os import listdir
from exifread.tags import FIELD_TYPES

PICKLE_STORE_PATH = './pickle_store/'


def scrapeData(file_list):
    """
    Scrape exif data from a list of files

    Parameters
    ----------
    file_list : list
        List of strings representing each file in a directory

    Returns
    ----------
    dict
        Dictionary with file names as the keys and the scraped
        exif metadata as values
    """
    metadata_dict = {}
    for file in file_list:
        f = file.open('rb')
        metadata_list = exifread.process_file(f)
        metadata_dict[file.name] = metadata_list

    return metadata_dict


def pickle_exif_data(store):
    """
    Uses Python built-ni pickle library to serialize dictionaries
    for future storage in a database

    Parameters
    ----------
    store : dict
        Dictionary with file names as the keys and the scraped
        exif metadata as values
    """
    for key in store.keys():
        filename = key
        outfile = open('./pickle_store/' + filename, 'wb')
        pickle.dump(store[key], outfile)
        outfile.close()


def unpickle_exif_data():
    """
    De-serializes all pickled files in a directory

    Returns
    ----------
    loaded_metadata : dict
        Dictionary with file names as the keys and the scraped
        exif metadata as values
    """
    pickles = listdir('./pickle_store/')
    print(pickles)
    for p in pickles:
        infile = open(PICKLE_STORE_PATH + p, 'rb')
        loaded_metadata = pickle.load(infile)
        infile.close()
    return loaded_metadata


def import_files():
    """
    Imports all files of type .PEF from a directory

    Returns
    ----------
    path_list : list
         List of strings representing each file in a directory
    """
    p = Path('E:/2020/0106').resolve()
    path_list = list(p.glob('**/*.PEF'))
    return path_list

def print_metadata(image_metadata):
    #print(type(image_metadata))
    #pprint.pprint(image_metadata)

    for tag in image_metadata.keys():
        if tag.startswith("EXIF") and tag not in ['EXIF MakerNote']: # if the tag contains EXIF data
            #  pprint.pprint("field_type: %s, \nprintable: %s, \nKey: %s" % (image_metadata[tag].field_type, tag, image_metadata[tag].printable))
            pprint.pprint("Printable: " + tag)
            pprint.pprint("Key: " + image_metadata[tag].printable)
            #pprint.pprint(len(tag))
             #pprint.pprint(FIELD_TYPES[image_metadata[tag].field_type])


if __name__ == '__main__':
    files = import_files()
    dict_store = scrapeData(files)
    # exif = scrapeData(dict_store)
    # pickle_exif_data(dict_store)
    unpickled = unpickle_exif_data()
    print_metadata(dict_store)





'''
Image Make
Image Model
Image XResolution
Image YResolution
Image ResolutionUnit
Image GPSInfo
EXIF ExposureTime
EXIF FNumber
EXIF ISOSpeedRatings
EXIF FocalLength
EXIF DateTimeOriginal
EXIF ExposureBiasValue
EXIF ExposureMode
EXIF WhiteBalance
EXIF FocalLengthIn35mmFilm
'''



def trim_metadata(image_metadata):
    for tag in image_metadata.keys():
        pprint.pprint(image_metadata[tag])
        #print(image_metadata[tag].printable)
