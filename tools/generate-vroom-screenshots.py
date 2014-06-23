#!/usr/bin/env python
#
# NAME: generate-vroom-screenshots
#
# USAGE: generate-vroom-screenshots
#
# DESCRIPTION:
#   This script parses source files for the vroom documentation website and 
#   generates screenshots for the examples. 
#
# OUTPUT:
#   For each example found in the source files a PNG screenshot will be 
#   generated and stored in the website image directory.


import os
import subprocess

# Setup global variables

WEBSITE_ROOT = '/home/jvan/Development/Web/vroom'
SOURCE_DIR   = os.path.join(WEBSITE_ROOT, 'source')
ASSETS_DIR   = os.path.join(SOURCE_DIR, 'assets')
IMAGE_DIR    = os.path.join(ASSETS_DIR, 'img', 'examples')
DOCUMENT_DIR = os.path.join(SOURCE_DIR, 'documentation')

#EXAMPLE_SOURCE_DIR = '/home/jvan/Development/Web/vroom/etc'
EXAMPLE_SOURCE_DIR = './examples'

SUBMODULES = [ 'rendering', 'core', 'utils' ]

SCREENSHOT_GRABBER = './vroom-screenshot.sh'

class NoImageTagFound(BaseException): pass

def get_markdown_files(module_name):
   directory = os.path.join(DOCUMENT_DIR, module_name)
   return filter(lambda f: '.md' in f and not f.startswith('.'), os.listdir(directory))

def generate_example_code(module, filename, title, block):
   
   basename = filename.replace('.html.md', '')
   basename = filename.split('.')[0]
   source_dir = os.path.join(EXAMPLE_SOURCE_DIR, module, basename)

   if not os.path.exists(source_dir):
      print('!! creating directory {} !!'.format(source_dir))
      os.makedirs(source_dir)

   vroom_file = title.replace(' ', '-').strip() + '.vroom'
   print('  (generating example code: vroom_file={})'.format(vroom_file))

   source_file = os.path.join(source_dir, vroom_file) 

   #if not os.path.exists(source_file):
   output = open(source_file, 'w')
   output.write('#!/usr/bin/env vroom-wrapper\n')
   output.write('from vroom import *\n')
   #output.write(block.replace('draw(', 'display('))
   output.write(block)
   output.close()
   #else:
      #print('!! WARNING: source file {} exists. Skipping. !!'.format(source_file))

   return source_file

def parse_markdown(module, filename):
   print('(parsing markdown: filename={})'.format(filename))

   path = os.path.join(DOCUMENT_DIR, module, filename)
   
   lines = open(path).readlines()

   while True:
      try:
         line = lines.pop(0)
      except IndexError:
         return

      if line.startswith('### examples'):
         break

   index = { }

   index['headers']    = [i for i,line in enumerate(lines) if line.startswith('####')]
   index['code-begin'] = [i for i,line in enumerate(lines) if line.startswith("~~~ python")]
   index['code-end']   = [i for i,line in enumerate(lines) if line.startswith("~~~") and i not in index['code-begin']]

   get_title      = lambda i: lines[i].strip().split('#### ')[1]
   get_code_block = lambda a,b: ''.join(lines[a+1:b])

   block_has_image_tag = lambda a,b: len([line for line in lines[a:b] if "vroom_example_image" in line])

   examples = zip(index['headers'], index['code-begin'], index['code-end'])

   #for header, begin, end in examples:
      #generate_example_code(module, filename, get_title(header), get_code_block(begin, end))
   
   return [[get_title(header), get_code_block(begin, end)] 
               for (header, begin, end) in examples
                  if block_has_image_tag(header, end)]


def take_screenshot(module, markdown, source):
   print('(take_screenshot: module={}, markdown={}, source={})'.format(module, markdown, source))    
   #image_dir = os.path.join(IMAGE_DIR, module, markdown.replace('.html.md', ''))
   image_dir = os.path.join(IMAGE_DIR, module, markdown.split('.')[0])

   if not os.path.exists(image_dir):
      print('!! creating directory {} !!'.format(image_dir))
      os.makedirs(image_dir)

   filename = os.path.join(image_dir, os.path.basename(source).replace('.vroom', '.png'))

   if os.path.exists(filename):
      print('!! WARNING: screenshot file {} already exists. Skipping.'.format(filename))
      return

   subprocess.call([SCREENSHOT_GRABBER, source, filename])
   

if __name__ == '__main__':
   
   for module in SUBMODULES:
      markdown_files = get_markdown_files(module)
      for markdown in markdown_files:
         examples = parse_markdown(module, markdown)
         if not examples:
            continue
         for title, code_block in examples:
            try:
               source = generate_example_code(module, markdown, title, code_block)
               take_screenshot(module, markdown, source)
            except NoImageTagFound:
               pass
