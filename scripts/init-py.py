import os
import sys
import logging

def setup_logger() -> logging.Logger:
    logger = logging.getLogger(name="")
    logger.setLevel(logging.DEBUG)

    # Logs to stdout so we can at least see logs in GHA.
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

LOGGER: logging.Logger = setup_logger() 

def turn_dir_into_py_package(dir_path: str):
    assert os.path.exists(dir_path)
    init_path = os.path.join(dir_path, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, 'w+') as fh:
            fh.write(f"# {dir_path}")
        LOGGER.info(f"converted directory {dir_path} to package")
    else:
        LOGGER.info(f"skipped directory {dir_path}")

def main():
    for (dir, dirs_inside, files_inside) in os.walk("nibiru_proto"):
        if not ("__init__.py" in files_inside):
            turn_dir_into_py_package(dir)            
    LOGGER.info("Success!")

if __name__ == '__main__':
    main()