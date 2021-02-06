import exifread
import pprint
import pickle
from exifread.tags import FIELD_TYPES


filename = 'Street Photos 0226 - 2766'


def scrapeData(file_path):
    f = open(file_path, 'rb')
    image_metadata = exifread.process_file(f)

    return image_metadata


def trim_metadata(image_metadata):
    for tag in image_metadata.keys():
        pprint.pprint(image_metadata[tag])
        #print(image_metadata[tag].printable)


def pickle_exif_data(metadata):
    outfile = open(filename, 'wb')
    pickle.dump(metadata, outfile)
    outfile.close()


def unpickle_exif_data(file):
    infile = open(filename, 'rb')
    loaded_metadata = pickle.load(infile)
    infile.close()
    return loaded_metadata


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
    exif = scrapeData('Street Photos 0226 - 2766.jpg')
    pickle_exif_data(exif)
    unpickled = unpickle_exif_data(filename)
    print_metadata(unpickled)





'''
ExposureTime
FNumber
ISOSpeedRatings
FocalLength
'''
