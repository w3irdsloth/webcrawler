
#Create list of available models
mod_list = ["textgenrnn"]

#Create list of available functions for each model
textgenrnn = [{"train_from_file": ["source", "epochs"]}, 
              {"generate": ["lines", "temperature", "return_as_list=True"]}]

fun_list = [textgenrnn]    

def activate_module(model):
    if model == "textgenrnn":
        print("running textgenrnn...")
        from textgenrnn import textgenrnn
        constructor = textgenrnn()

    else:
        print("model not found")
