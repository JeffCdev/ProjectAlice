from terminaltables import DoubleTable

from core.console.Command import Command


#
# ListCommand lists all commands
#
class ListCommand(Command):

	def create(self):
		self.name = 'list'
		self.setDescription('List all commands')
		self.setDefinition()
		self.setHelp('> The %command.name% command lists all commands:\n'
					 '  <fg:magenta>%command.full_name%<fg:reset>')


	def execute(self, inputt):
		commands = self.application.commands
		sortedCommandKeys = sorted(commands)

		self.nl()
		self.write('Options :')
		TABLE_DATA = [['Option', 'Description'], ]
		table_instance = DoubleTable(TABLE_DATA)

		for k, option in self.application.getDefaultInputDefinition().getOptions().items():
			TABLE_DATA.append(['--{} [{}]'.format(option.name, option.getShortcut()), option.getDescription()])

		self.write(table_instance.table)

		self.nl()
		self.write('Commands :')
		TABLE_DATA = [['Command name', 'Description']]
		table_instance = DoubleTable(TABLE_DATA)

		limit = 55

		for name in sortedCommandKeys:
			command = commands[name]

			if len(command.getDescription()) > limit:
				desc = '{}...'.format(command.getDescription()[0:limit])
			else:
				desc = command.getDescription()
			TABLE_DATA.append([name, desc])

		self.write(table_instance.table)
