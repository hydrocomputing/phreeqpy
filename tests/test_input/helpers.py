import textwrap

def cut_code(code_text):
    """Dedent and strip extra white space of code text."""
    return textwrap.dedent(code_text).strip()

def show_code(desired, generated, whitespace_fill=None):
    """Print desired and generated PHREEQC code.
    """
    generated = str(generated)
    if whitespace_fill:
        generated = generated.replace(' ', whitespace_fill)
        desired= desired.replace(' ', whitespace_fill)
    print '\ndesired:\n'
    print desired
    print '\ngenerated:\n'
    print generated
