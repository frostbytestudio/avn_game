import os
import datetime
import renpy

class CoreLogger:

    # Log Level Constraints
    ERROR = 0
    WARNING = 1
    INFO = 2

    def __init__(self):
        self.log_level = self.WARNING   # Default to WARNING Level
        self.log_file = None
        self.console_output = True
        self.debug_mode = False         # Debug flag for INFO messages

    def initalize(self):
        try:
            # Get Ren'Py Game Directory
            log_directory = os.path.join(renpy.config.gamedir, "logs")

            # Create a logs directory if it doesn't exist
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            # Clear any exisiting log file
            log_path = os.path.join(log_directory, "core.log")
            if os.path.exists(log_path):
                os.remove(log_path)

            # Create a new log file for this game session
            self.log_file = open(log_path, "w", encoding='utf-8')

            # Log game session start
            session_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._write("INFO", 'CoreLogger', f"New Logging Session Started At {session_start}")
            return True
        except Exception as e:
            self._write(f"Failed to initialize logging system: {str(e)}")
            return False