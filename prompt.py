import os
import argparse

def collect_yaml_files(root_dir, output_file):
    # Extensions to look for
    yaml_extensions = ('.yaml', '.yml')
    
    # Directories to ignore (to save tokens and avoid noise)
    ignore_dirs = {'.git', 'node_modules', '__pycache__', 'venv', 'env', '.idea', '.vscode'}

    count = 0
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            
            # Walk through directory
            for root, dirs, files in os.walk(root_dir):
                # Modify dirs in-place to skip ignored directories
                dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith('.')]
                
                for file in files:
                    if file.lower().endswith(yaml_extensions):
                        file_path = os.path.join(root, file)
                        
                        # Calculate relative path for cleaner LLM context
                        relative_path = os.path.relpath(file_path, root_dir)
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                                
                                # Write clearly formatted block for the LLM
                                outfile.write(f"================================================================\n")
                                outfile.write(f"FILE: {relative_path}\n")
                                outfile.write(f"================================================================\n")
                                outfile.write(content)
                                outfile.write(f"\n\n") # Extra spacing between files
                                
                                print(f"Added: {relative_path}")
                                count += 1
                                
                        except Exception as e:
                            print(f"Error reading {file_path}: {e}")

        print(f"\nSuccess! Concatenated {count} YAML files into '{output_file}'.")

    except IOError as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine all YAML files in a directory into a single text file for LLM prompting.")
    
    # Argument for root directory (default is current dir)
    parser.add_argument("directory", nargs='?', default=".", help="The root directory to search (default: current directory)")
    
    # Argument for output file
    parser.add_argument("-o", "--output", default="combined_yaml_context.txt", help="The output filename (default: combined_yaml_context.txt)")

    args = parser.parse_args()
    
    collect_yaml_files(args.directory, args.output)
