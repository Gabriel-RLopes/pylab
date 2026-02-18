import subprocess
import platform
import shlex


class CompilerExecutor:

    def __init__(self, command, working_dir=None, timeout=None):
        self.command = command
        self.working_dir = working_dir
        self.timeout = timeout

    def run(self):
        if isinstance(self.command, str):
            cmd = shlex.split(self.command)
        else:
            cmd = self.command
        
        try:
            process = subprocess.run(
                cmd,
                cwd=self.working_dir,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            return{
                'returncode': process.returncode,
                'stdout': process.stdout,
                'stderr': process.stderr
            }
        except subprocess.TimeoutExpired:
            return {
                'returncode': -1,
                'stdout': '',
                'stderr': 'timeout during compilation'
            }
