import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://plwgzqtuedvknc:eb781bb1e2867c4d7d56617ea16a3feb04b70e5a14932c874b02c06d777ee0a6@ec2-52-72-125-94.compute-1.amazonaws.com:5432/dvi8f1qtv6s28'
