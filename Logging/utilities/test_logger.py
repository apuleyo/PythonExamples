import pytest
# Agregar el directorio del proyecto al sys.path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

def test_logger():
    log = Logger(R'C:\Folders\GitHub\PythonExamples\Logging\custom.log', level='warning', fmt='%(asctime)s - %(levelname)s - %(message)s', when='S')
    log.logger.debug("This is a debug message - won't be logged")
    log.logger.warning("This is a warning message - will be logged")