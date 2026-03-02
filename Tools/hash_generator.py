# This function is used to create a hash file using sha56 algorithm, reading the file safely and in small pieces.
import hashlib  # Hashlib creates hashes


def hash_file(filename, algorithm="sha256"):
    h = hashlib.new(algorithm)  # To create a hashed object using the algorithm

    # rb opens the file in binary mode and with ensures the file is closed safely
    with open(filename, "rb") as file:
        # chunk is a piece of a file, it reads in bytes, 4096 bytes at a time.
        chunk = file.read(4096)

        while chunk:
            # This is used to take the chunk and feed it to the algorithm
            h.update(chunk)
            chunk = file.read(4096)
    return h.hexdigest()
