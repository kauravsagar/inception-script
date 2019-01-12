import os

from jinja2 import Template

from basescript import BaseScript

class InceptionScript(BaseScript):

    def _parse_define_args(self, args_str):
        if args_str is None:
            return []
        args_list = []
        args = args_str.split('#')
        for arg in args:
            d = arg.split(':')
            args_list.append({
                'name': d[0],
                'extended_name':  d[1],
                'type':  d[2],
                'required':  d[3].capitalize(),
                'help':  d[4] if d[4] != '_' else None
            })
        return args_list
    
    def run(self):
        with open('template/script_template.txt', 'r') as script_template_file:
            script_template = Template(script_template_file.read())
            data = {
                    'class_name': self.args.class_name,
                    'args':  self._parse_define_args(self.args.arguments)
            }

        if self.args.filename is None:
            filename = '{}.py'.format(self.args.class_name.lower())
        else:
            filename = '{}.py'.format(self.args.filename.lower())
        
        self.log.info('generated file name: {}'.format(filename))
        
        # check if file already exists if its print error and end script
        if os.path.isfile(filename):
            self.log.error('File already exists')
            return

        with open(filename, 'w') as test:
            rendered_script = script_template.render(data)
            test.write(rendered_script)

    def define_args(self, parser):
        parser.add_argument('-c','--class_name', type=str, required=True,
            help='Class name for script')
        parser.add_argument('-f', '--filename', type=str,
            help='Script file name don\'t include extension . (By default classname with lowercase)')
        parser.add_argument('-args', '--arguments', type=str,
            help='argument list in script. format name:extendedname:type:required:help#name:extendedname:type:required:help')



if __name__ == "__main__":
    InceptionScript().start()
