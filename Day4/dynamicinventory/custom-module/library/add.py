from ansible.module_utils.basic import *

class Adder:

    def add(self, value1, value2):
       return value1 + value2

def main():
   
   module = AnsibleModule (
	argument_spec = dict (
		firstInput = dict( required=True, type='int' ),
		secondInput = dict( required=True, type='int' ),
        )
   )

   firstNumber = module.params['firstInput']
   secondNumber = module.params['secondInput']

   addObj = Adder()
   response = { "Result": str( addObj.add ( firstNumber, secondNumber ) ) }

   module.exit_json ( changed=False, meta=response )
   module.fail_json ( "Fatal error occured" )

main()
