import time, os, sublime, sublime_plugin

class VersionedCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#save the file in case if there is any modifications before start versioning it.
		sublime.active_window().run_command("save")
		os.system("cd " + self.currentDir())
		gitStatus = os.popen('git status').read()
		if("Not a git repository" not in gitStatus):
			os.system("cd " + self.currentDir() + " & git init . & git add . & git commit -m 'modified'")
		else:
			os.system("cd " + self.currentDir() + " & git add . & git commit -m 'modified'")
	def currentDir(self):
		file_name=self.view.file_name()
		path=file_name.split("\\")
		current_driver=path[0]
		path.pop()
		current_directory="\\".join(path)		
		return current_directory
