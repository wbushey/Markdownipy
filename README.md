# What Is It
Markdownipy is an HTML -> Markdown translator wirtten in Python that uses [lxml](http://lxml.de/installation.html) to parse HTML and a recursive tree traversal to do the translation.

At the moment, Markdownipy is not as complete as other HTML -> Markdown translators, namely [Markdownify](https://github.com/ecenter/markdownify) and [html2text](https://github.com/aaronsw/html2text). But if you need an HTML -> Markdown translator in Python that handles nested lists, you're in the right place.

# Requirements
To use Markdownipy you will need to have [lxml](http://lxml.de/installation.html) installed.

# Usage

The fastest way to see Markdownipy in action is the fire up the Python intepretor and import * from run_md, which will create an instance of Markdownipy named t and provide a couple of helper functions.

    $ python
    >>> from run_md import *
    >>> md = fetchAndProcess('http://www.facebook.com/terms.php', '/html/body/div[3]/div/div/div/div[2]/div/div',t)
    >>> print md
    
The above will fetch Facebook's Terms of Service and run the main content div through Markdownipy. Since the instance created by run_md has verbose = True, you will see the translation tree print during translation. Once translation is finished, print md will display Facebook's ToS in Markdown.

For convience, a small directory of urls and xpath queries is included in sites_dict.py. Using that directory (named 'sites'), we can fetch and translate Facebook's ToS as follows

    $ python
    >>> from run_md import *
    >>> md = fetchAndProcess(sites['Facebook ToS']['url'], sites['Facebook ToS']['xpath'], t)
    >>> print md
    
To use Markdownipy in a script or program, simply copy Markdownipy.py into your working folder, import the Markdownipy class from the Markdownipy module, create an instance, and call the .translate() method

    from Markdownipy import Markdownipy
    t = Markdownipy(True, True)
    md = t.translate('<div>A div with a <a href="#">link</a>!</div>')
    
Arguments to the constructor - Markdownipy(tl, verbose) - control list handling and verbosity

* tl: If True, Markdownipy will translate ul and ol lists into markdown. If false, list markup will be included in the output as its original HTML markup
* verbose: If True, Markdownipy will print debugging messages, including the translation call tree. It will also save the HTML that results from pre-translation cleaning to a file named clean_html.html

# History

Markdownipy started as the HTML to Markdown translator for [FriendlyToS](https://github.com/sethwoodworth/FriendlyToS). Website legalese uses lists a lot, and nests them a lot too; so FriendlyToS needs a translator that can handle lists real well. And since the project is in Python, it makes since to have a translator wirtten in Python. Finally, I just really wanted to write a translator. So, that's how Markdownipy got to this point.

## The Name and Relationship to Markdownify

Anybody familiar with [Markdownify](https://github.com/ecenter/markdownify) will recognize that the name of this module is an homage to Markdownify. Markdownipy is not a Python port of Markdownify - I didn't find Markdownify until I had already written quite a bit of Markdownipy. But they work in basically the same way - recursive translation of a parse tree. So when it came time to name this translator I figured it makes since to name it after a translator that works in a similar way.