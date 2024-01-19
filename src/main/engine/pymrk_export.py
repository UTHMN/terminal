import json

my_dict = {
	"demo1":"print('hello')"
}

def pymrk_export(self, exp, export_path):
	to_export = export_path + "commands.json"

	with open(to_export, "w") as outfile:
		json.dump(exp, outfile, indent=4)
	outfile.close()

pymrk_export("tmp", my_dict, "./PyMrk/Dict/")