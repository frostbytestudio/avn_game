"""
Enhanced logging system for the core package.
Extends Ren'Py's logging capabilities with additional features.
"""

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

    def _write(self, level, category, message):
        try:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            formatted = f"[{timestamp}] [{level}] [{category}] [{message}]"

            if level == "DEBUG" and not self.debug_mode:
                return
            
            if level == "INFO" and not self.debug_mode:
                self._write("DEBUG", "CoreLogger", f"INFO message suppressed: {message}")
                return

            if self.log_file and not self.log_file.closed:
                self.log_file.write(formatted + '\n')
                self.log_file.flush()

            if self.console_output:
                print(formatted)
        except Exception as e:
            print(f"Logging Error: {str(e)}")

    def info(self, category, message):
        if not self.debug_mode:
            self._write("DEBUG", "CoreLogger", f"INFO message suppressed: {message}")
        if self.debug_mode:
            self._write("INFO", category, str(message))

    def warning(self, category, message):
        if self.log_level <= self.WARNING:
            self._write("WARNING", category, str(message))

    def error(self, category, message):
        self._write("ERROR", category, str(message))

    def set_level(self, level):
        if level in [self.ERROR, self.WARNING, self.INFO]:
            self.log_level = level
            self.info("CoreLogger", f"Log Level Set To {level}")

    def set_debug_mode(self, enabled):
        self.debug_mode = enabled
        renpy.config.developer = enabled

        self.info("CoreLogger", f"DEBUG MODE {'enabled' if enabled else 'disabled'}")

    def __del__(self):
        if self.log_file and not self.log_file.closed:
            self.log_file.close()


core_logger = CoreLogger()