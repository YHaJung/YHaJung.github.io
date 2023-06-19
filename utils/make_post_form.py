
def translate_to_english(line):
    import googletrans
    translator = googletrans.Translator()
    again_flag = True
    while again_flag:
        try:
            new_line = translator.translate(line, src='ko', dest='en').text
            again_flag = False
        except:
            again_flag = True
    return new_line

def ask_filename_for_user(origin_filename, new_filename):
    print(origin_filename)
    print(new_filename)
    key = None
    while key not in ['1', '2']:
        key = input("Do you want to change? Pass(1), Change(2) ")

    if key == '1':
        return new_filename
    else:
        new_filename = input("Enter new filename : ")
        return new_filename


def set_post_filename(dir, filename):
    import os, re
    from datetime import datetime
    new_filename = translate_to_english(filename)
    new_filename = str(datetime.today())[:11]+new_filename.lower()
    new_filename = re.sub(r'[,()]', "", new_filename)
    new_filename = "-".join(new_filename.split(' ')[:-1])+".md"
    new_filename = ask_filename_for_user(filename, new_filename)

    os.rename(
            os.path.join(dir, filename),
            os.path.join(dir, new_filename)
        )
    return new_filename

def set_image_path(dir, origin_filename, new_filename):
    import os
    origin_dir = os.path.join(dir, origin_filename)[:-3]
    new_dir = os.path.join(dir, new_filename)[:-3]
    os.makedirs(new_dir, exist_ok=True)

    img_names = os.listdir(origin_dir)
    for img_name in img_names:
        os.rename(
            os.path.join(origin_dir, img_name),
            os.path.join(new_dir, img_name)
        )

    os.rmdir(origin_dir)
    return new_dir


def set_post_content(dir, new_filename):
    import os

    filepath = os.path.join(dir, new_filename)
    with open(filepath, "r") as f:
        lines = f.readlines()
        f.close()

    if lines[0][0] == '#':   # set post start
        title = lines[0].rstrip("\n").lstrip("# ")
        if title[0] == '[':
            category = title.split(']')[0][1:]
        else:
            category = ''
        lines[0] = f"--- \ntitle : \"{title}\"\ncategories:\n- {category}\ntags:\n- {category.lower()}\n---\n"
    
    for line_idx, line in enumerate(lines): # set image path
        if ".png)" in line:
            line_start = lines[line_idx].split('(')[0]
            line_end = lines[line_idx].split('/')[-1]
            lines[line_idx] = f"{line_start}(../../assets/images/{new_filename.rstrip('.md')}/{line_end}"

    
    content = "".join(lines)

    with open(filepath, "w") as f:
        f.write(content)
        f.close()

    return content




def set_post_form(dir = '_posts', img_dir = 'assets/images'):
    import os
    filelist = os.listdir(dir)
    for filename in filelist:
        if filename[:2] != '20':
            new_filename = set_post_filename(dir, filename)
            set_image_path(img_dir, filename, new_filename)
            set_post_content(dir, new_filename)
            print(new_filename)
    

if __name__=='__main__':
    set_post_form()