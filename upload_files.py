import os
from rmapy.api import Client
from rmapy.document import ZipDocument

def convert_and_upload_file(client, doc_location, folder, new_name=None):
    raw_document = ZipDocument(doc=doc_location)
    if new_name:
        raw_document.metadata["VissibleName"] = new_name
    client.upload(raw_document, folder)
    return True

def find_folder(client, folder_name):
    matches = [ i for i in client.get_meta_items()
               if i.VissibleName == folder_name ]
    if len(matches) >= 1:
        return matches[0]
    return None

def upload_into_folder(doc_location, folder_name, new_name=None):
    rm = Client()
    rm.renew_token()
    folder = find_folder(rm, folder_name)
    if folder is not None:
        result = convert_and_upload_file(rm, doc_location,
                                         folder, new_name=new_name)
        if result == True:
            print("Success!")


if __name__ == "__main__":
    start_path = "/home/katharine/Downloads"
    for fn in os.listdir(path=start_path):
        upload = input("Do you want to upload %s? " % fn)
        if upload in ["y", "Y", "yes"]:
            new_name = input("Enter new name if desired: ")
            folder_name = input("Enter what folder name you want it to upload to: ")
            doc_location = "%s/%s" % (start_path, fn)
            upload_into_folder(doc_location, folder_name, new_name=new_name)
