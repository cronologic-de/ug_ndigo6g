import pypandoc

def convert_tex_to_rst(tex_file, rst_file):
    try:
        # Convert .tex to RST using pypandoc
        pypandoc.convert_file(tex_file, 'rst', outputfile=rst_file)
        print(f"Successfully converted {tex_file} to {rst_file}")
    except Exception as e:
        print(f"Error converting {tex_file} to RST: {e}")

if __name__ == "__main__":
    # Replace 'example.tex' with the actual path to your LaTeX file
    tex_file_path = 'C:/Users/zeiqbal/PycharmProjects/Ndigov1.1/latex/Ndigo_API.tex'
    rst_output_path = 'C:/Users/zeiqbal/PycharmProjects/Ndigov1.1/docs/Ndigo_API.rst'  # Replace with the desired output RST file name

    convert_tex_to_rst(tex_file_path, rst_output_path)
