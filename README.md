# inception_script.py
This script will  generates bolierplate for basescript based scripts.

### Parameters
- `-c or class_name` Class used in script file
- `f or --filename` Filename for the script file. Don't pass file extension. If this argument is not given script will create filename based on **class_name** as file name
- `-args or --arguments` this arguments takes the arguments list you want to add in your generated script. This argument takes special formatted string as a arugment. You can pass colon sperated data for arugment for e.g.  `name:extendedname:type:required:help`. If you have more than one arguments in your script concat the list with `#` symbol for e.g. `name:extendedname:type:required:help#test:test_extended:type:required:help`. Here ervery argument is required except for help if don't what to send `help` argument you can simply pass `_` for help parameter for e.g. `name:extendedname:type:required:_#test:test_extended:type:required:userhelp` 

### Usage
`python inception_script.py run -c Foo -f foo -args name:full_name:str:false:help
- output
```python3
from basescript import BaseScript

class Foo(BaseScript):
    def define_args(self, parser):
        parser.add_argument('-name', '--full_name', type=str, required=False, help='help')
        

    def run(self):
        pass

if __name__ == '__main__':
    Foo().start()(inception) 
```

### Change template
If you want to change the structure of the output  file you can modify `template/script_template.txt`.  The script_template uses `jinja2` templating langauge
