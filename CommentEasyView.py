#-*- coding: UTF-8 -*-
import sublime, sublime_plugin

class ViCommentCommand(sublime_plugin.TextCommand):
	MOJO = {
		'A':['   ███    ',
				 '  ██ ██   ',
				 ' ██   ██  ',
				 '██     ██ ',
				 '█████████ ',
				 '██     ██ ',
				 '██     ██ ',
				 '          '],
		'B':['████████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '████████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '████████  ',
				 '          '],
		'C':[' ███████  ',
				 '██     ██ ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'D':['███████   ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '███████   ',
				 '          '],
		'E':['█████████ ',
				 '██        ',
				 '██        ',
				 '███████   ',
				 '██        ',
				 '██        ',
				 '█████████ ',
				 '          '],
		'F':['█████████ ',
				 '██        ',
				 '██        ',
				 '███████   ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '          '],
		'G':[' ███████  ',
				 '██     ██ ',
				 '██        ',
				 '██  █████ ',
				 '██     ██ ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'H':['██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '█████████ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '          '],
		'I':[' ███████  ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 ' ███████  ',
				 '          '],
		'J':['       ██ ',
				 '       ██ ',
				 '       ██ ',
				 '       ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'K':['██     ██ ',
				 '██   ██   ',
				 '██ ██     ',
				 '██        ',
				 '██ ██     ',
				 '██   ██   ',
				 '██     ██ ',
				 '          '],
		'L':['██        ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '█████████ ',
				 '          '],
		'M':['██     ██ ',
				 '███   ███ ',
				 '████ ████ ',
				 '██ ███ ██ ',
				 '██  █  ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '          '],
		'N':['██     ██ ',
				 '██    ███ ',
				 '██   ████ ',
				 '██  ██ ██ ',
				 '██ ██  ██ ',
				 '████   ██ ',
				 '███    ██ ',
				 '          '],
		'O':[' ███████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'P':['████████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '████████  ',
				 '██        ',
				 '██        ',
				 '██        ',
				 '          '],
		'Q':[' ███████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '██  █  ██ ',
				 '██  ██ ██ ',
				 '██   ███  ',
				 ' █████ ██ ',
				 '          '],
		'R':['████████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '████████  ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '          '],
		'S':[' ███████  ',
				 '██     ██ ',
				 '██        ',
				 ' ███████  ',
				 '       ██ ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'T':['█████████ ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '          '],
		'U':['██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 ' ███████  ',
				 '          '],
		'V':['██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 '██     ██ ',
				 ' ██   ██  ',
				 '  ██ ██   ',
				 '   ███    ',
				 '          '],
		'W':['██     ██ ',
				 '██     ██ ',
				 '██  █  ██ ',
				 '██ ███ ██ ',
				 '████ ████ ',
				 '███   ███ ',
				 '██     ██ ',
				 '          '],
		'X':['██     ██ ',
				 ' ██   ██  ',
				 '  ██ ██   ',
				 '   ███    ',
				 '  ██ ██   ',
				 ' ██   ██  ',
				 '██     ██ ',
				 '          '],
		'Y':['██     ██ ',
				 '██     ██ ',
				 ' ██   ██  ',
				 '  ██ ██   ',
				 '   ███    ',
				 '   ███    ',
				 '   ███    ',
				 '          '],
		'Z':['█████████ ',
				 '      ██  ',
				 '     ██   ',
				 '   ███    ',
				 '  ██      ',
				 ' ██       ',
				 '█████████ ',
				 '          ']
		}

	def run(self, edit):
		shuus = []

		for shuu in self.view.sel():
			shuus.insert(0, shuu)
			# 找到區域

		for shuu in shuus:
			if shuu.empty():
				zeroshuu = 0
				# 如果沒有區域
				shuu = self.view.line(shuu)
				# 取得當下行前後
			else:
				zeroshuu = 1
				# 如果有區域

			yosts = self.view.substr(shuu).strip().split("\n")
			# 有來前後整個拿下來
			self.view.erase(edit, shuu)
			point = shuu.begin()

			if zeroshuu == 1:
				point += self.view.insert(edit, point, "\n")

			# yosts = yosts.reverse()
			for yost in reversed(yosts):
				if yost == '':
					continue
				decodes = self.matrix(yost)

				for decode in  reversed(decodes):
					self.view.insert(edit, point,decode + "\n")
					self.view.sel().clear()
					self.view.sel().add(sublime.Region(point, point))
					self.view.run_command('toggle_comment')

	def matrix(self, origin):
		afters = ['','','','','','','','']
		origin = origin.upper()
		for x in range(0,len(origin)):
			if str(origin[x]) in self.MOJO:
				afters[0] += self.MOJO[origin[x]][0]
				afters[1] += self.MOJO[origin[x]][1]
				afters[2] += self.MOJO[origin[x]][2]
				afters[3] += self.MOJO[origin[x]][3]
				afters[4] += self.MOJO[origin[x]][4]
				afters[5] += self.MOJO[origin[x]][5]
				afters[6] += self.MOJO[origin[x]][6]
				afters[7] += self.MOJO[origin[x]][7]
		return afters



