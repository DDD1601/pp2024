import subprocess
import shlex

def execute_command(command):
    
    args = shlex.split(command)
    
    
    redirect_output = None
    if '>' in args:
        redirect_output = args[args.index('>') + 1]
        args.remove('>')
        args.remove(redirect_output)
    
    
    redirect_input = None
    if '<' in args:
        redirect_input = args[args.index('<') + 1]
        args.remove('<')
        args.remove(redirect_input)
    
    
    try:
        if redirect_input:
            with open(redirect_input, 'r') as f:
                output = subprocess.run(args, input=f.read(), text=True, capture_output=True, check=True)
        else:
            output = subprocess.run(args, text=True, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"
    
    
    if redirect_output:
        with open(redirect_output, 'w') as f:
            f.write(output.stdout)
        return f"Output redirected to {redirect_output}"
    else:
        return output.stdout

def main():
    while True:
        command = input("Enter a command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            break
        result = execute_command(command)
        print(result)

if __name__ == "__main__":
    main()
