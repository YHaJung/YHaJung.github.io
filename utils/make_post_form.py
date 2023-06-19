
def set_post_content(dir, new_filename):
    import os
    f = open(os.path.join(dir, new_filename))
    lines = f.readlines()

    if lines[0][0] == '#':   # set post start
        title = lines[0].rstrip("\n").lstrip("# ")
        if title[0] == '[':
            category = title.split(']')[0][1:]
        else:
            category = ''
        lines[0] = f"--- \ntitle : \"{title}\"\ncategories:\n- {category}\ntags:\n- {category}\n---"
    
    # for line_idx, line in enumerate(lines):
    #     if line[:12] != "![Untitled]":
    #         lines[line_idx] = "![Untitled](../../assets/images/"

    
    
    content = "".join(lines)
    print(content)
    return content



def set_post_filename(filename):
    import re
    from datetime import datetime
    new_filename = str(datetime.today())[:11]+filename.lower()
    new_filename = re.sub(r'[,()]', "", new_filename)
    new_filename = "-".join(new_filename.split(' ')[:-1])+".md"
    print(new_filename)
    # os.rename(
        #     os.path.join(dir, filename),
        #     os.path.join(dir, new_filename)
        # )
    return new_filename

def set_post_form(dir = '_posts'):
    import os
    filelist = os.listdir(dir)
    for filename in filelist:
        if filename[:2] != '20':
            new_filename = set_post_filename(filename)
            set_post_content(dir, new_filename)
            break

    

if __name__=='__main__':
    set_post_form()
    # set_all_post_filename()