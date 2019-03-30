#
#   File creation and upload
#


def local(infile,outfile):
    """
    Creates file output file from given input.
    """
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def s3(client,infile,bucket,name):
    """
    Uploads file to s3 bucket from given input.
    """
    client.upload_fileobj(infile, bucket, name)