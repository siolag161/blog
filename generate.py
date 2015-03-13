#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os, sys
import locale

    
sys.path.append(os.path.join(os.path.dirname(__file__)))



from settings import dev_settings as conf


def locale_time(t, show_seconds=False):
    format = getattr(conf, "DATE_FORMAT", "%H:%M %a %d %b %Y")
    return t.strftime(format)

def get_local_time():
    import pytz
    import datetime
    return datetime.datetime.now().replace(
				    tzinfo=pytz.timezone(conf.TIMEZONE))
def get_default_time():     
    local_time= get_local_time()
    return locale_time(local_time)

def get_slug(title):
    from slugify import slugify
    # t = get_local_time().strftime("%Y/%m/%d")
    slug = slugify(title)
    return slug

def filter_empty_lines(original):
    #import re
    #return filter(lambda x: not re.match(r'^\s*$', x), original)
    filtered = [line.strip() for line in original.split('\n') if line.strip() != '']
    return "\n".join(filtered)
#########
if __name__=='__main__':
    default_author = conf.AUTHOR
    title = raw_input("Enter the title of your post: ") or "My fancy title"
    author = raw_input("Enter author[%s]: "%default_author) or default_author
    date = get_default_time()
    tags = raw_input("Enter tags, seperated by a ',': ")
    category = raw_input("Enter category: ") or "dev"
    summary = raw_input("Enter the summary here: ") 
    # locale.setlocale(locale.LC_ALL, conf.LOCALE)    
    # print get_default_time()

    
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('content'))
    template = env.get_template('_md_base_post')
    output_from_parsed_template = template.render(title=title, author=author,tags=tags,
						  date=date,category=category,summary=summary)

    output_from_parsed_template = filter_empty_lines(output_from_parsed_template)
    outfile = get_slug(title)
    with open("./content/%s.md"%outfile, "wb") as fh:
	fh.write(output_from_parsed_template)
