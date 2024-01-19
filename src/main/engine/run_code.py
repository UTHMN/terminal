def run(self, dic, cmd):
        try:
            self.word = dic[f"{cmd}"]
            exec(str(self.word))
        
            return str(self.word)

        except Exception as error:
            return error