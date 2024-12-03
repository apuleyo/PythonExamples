from Logging.utilities.Logger import Logger

log = Logger(R'C:\Folders\GitHub\PythonExamples\Logging\custom.log', level='warning', fmt='%(asctime)s - %(levelname)s - %(message)s', when='S')
log.logger.debug("This is a debug message - won't be logged")
log.logger.warning("This is a warning message - will be logged")