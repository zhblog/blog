# -*- coding: utf-8 -*-

# author: onesuper
# under MIT license

import yaml
import markdown
import re
import time
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

# ===========import the configs========
infile = "config.yaml"
outfile = "point.html"
if len(sys.argv) > 2:
    infile = sys.argv[1]
    outfile = sys.argv[2]

f = open(infile)
config = yaml.load(f)
f.close()
filename = config['filename']
theme = config['theme']
title = config['meta']['title']
subtitle = config['meta']['subtitle']
author = config['meta']['author']
email = config['meta']['contact']['email']
sinaweibo = config['meta']['contact']['sinaweibo']
github = config['meta']['contact']['github']
organization = config['meta']['organization']
googlefonts = config['googlefonts']
navi_enable = config['slide']['navi']
ribbon_enable = config['slide']['ribbon']
latex_enable = config['slide']['latex']
gravatar_enable = config['meta']['gravatar']
ga = config['google-analytics']
# =======read the markdown file and convert it to html ========
fmd = codecs.open(filename, mode="r", encoding="utf8")
text = fmd.read()
html = markdown.markdown(text)


# ==================html starts===============
content = '''
<!doctype html>  
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>''' 
content += title
content += '''</title>
    <link rel="stylesheet" href="/blog/weakpoint/core/weakpoint.css">
    <script src="/blog/weakpoint/third/jquery.js" type="text/javascript"></script>
    <script src="/blog/weakpoint/third/jquery.bxSlider.min.js" type="text/javascript"></script>
    <script type="text/javascript">
  $(document).ready(function(){
    bxslide = $('#slider1').bxSlider({
        infiniteLoop: false,
        controls: false,
        mode: 'horizontal',
        speed: 200,
        onBeforeSlide: function(){onSwitch=true},
        onAfterSlide: function(){onSwitch=false}
        });
});
    </script>'''

# ====================latex======================
if latex_enable:
    content += '''
     <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [ ['$','$'], ["\\(","\\)"] ],processEscapes: true}});</script>
    <script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']}});</script>
    <script type="text/x-mathjax-config">MathJax.Hub.Queue(function() {var all = MathJax.Hub.getAllJax(), i;for(i=0; i < all.length; i += 1) {all[i].SourceElement().parentNode.className += ' has-jax';}});</script>
    <script type="text/javascript"src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>'''
# ends

# ===================google fonts==================
if googlefonts:
    content += '''
    <link href='http://fonts.googleapis.com/css?family='''
    content += googlefonts
    content += '''' rel='stylesheet' type='text/css'>'''


# ===================theme=====================
if theme:
    content +='''    
    <link rel="stylesheet" href="/blog/weakpoint/theme/'''
    content += theme
    content += '''.css">\n'''

# ================google-analytics================= 
if ga:
    content += '''    <script type="text/javascript">var _gaq = _gaq || [];_gaq.push(['_setAccount', "'''
    content +=ga
    content += '''"]);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
  </script>
    '''

# ================head ends & body starts ===================
content += '''\n  </head>\n<body>'''


# =======================navi====================
if navi_enable:
    content += '''
    <div class="navi">'''
    # get the headlines ready 
    headlines = re.compile(r'<h1>.+</h1>').findall(html)
    if headlines: 
        for i in range(len(headlines)):
            headlines[i] = headlines[i][4:-5]
        for h in headlines:
            content += ("<span>" + h + "</span>")
    content += '''
    </div>'''

content += '''
    <div id="wrapper">
    <div id="slider1">
    <div class="paper"><div class="paper-container">\n<!-- ====================front page ===============  -->\n''' 

# =====================front page starts===========================

# title
content += '''<div class="title">'''
content += title
content += '''</div>\n'''
    
# subtile
content += '''<div class="subtitle">'''
content += subtitle
content += '''</div>\n'''

# *****************meta starts **********************

content += '''<div class="meta">'''

if gravatar_enable and email:
    import urllib, hashlib
    gravatar_url = "/blog/weakpoint/img/ubuntu-gril.jpg"
    content += '<img style="float:left;margin:15px;" class="avatar"src="' + gravatar_url +'" alt="avatar" width="180" height="140"/>'


content += '''\n<table>\n<tbody>\n''' 
    
# author
content += '''<tr class="author"><td>'''
content += author
content += '''</td></tr>\n'''

# +++++++++++++++social starts ++++++++++++++++++
content +='''<tr class="social"><td><ul>\n'''

# email
if email:
    content += '''  <li class="email"><a href="mailto:'''
    content += email
    content += '''" targe="_blank">Email</a></li>\n'''

#sinaweibo
if sinaweibo:
    content += '''  <li class="sinaweibo"><a href="http://weibo.com/''' 
    content += sinaweibo
    content += '''" target="_blank">@sina</a></li>\n'''

if github:
    content += '''  <li class="github"><a href="http://github.com/'''
    content += github
    content += '''" target="_blank">Github</a></li>\n'''
# ++++++++++++++++++social ends +++++++++++++++++
content += '''</ul></td></tr>\n'''
# organization
if organization:
    content += '''<tr class="organization"><td>'''
    content += organization
    content += '''</td></tr>\n'''
    
# time
content += '''<tr class="date"><td>'''
content += time.strftime("%Y-%m-%d", time.localtime())
content += '''</td></tr>\n'''

# ********************************meta ends ************************************
content += '''</tbody>\n</table>\n</div>\n'''
     
# ======================theme========================
content += '''<div class="theme">'''
content += theme
content += ''' theme</div>\n'''

# ============= front page ends=====================
content += ''' <!-- ================front page==============  -->\n<div id="popup" style="margin-top: 60px;width:380px;height:120px;color: #333;display:none;background-color:#ddd;padding: 20px;border-radius: 15px;">j / k PPT翻页<br>F11 全屏</br>试试看!</div></div></div>'''

# ==================trick here=================
html = html.replace('<h2>', '<hr />\n<h2>')
html = html.replace('<h1>', '<hr />\n<h1>')
p = re.compile(r'<hr />')
slides = p.split(html)
slides.remove('')

# ===================slides====================
for one in slides:
    content += '''






    
    
    <div class="paper"><div class="paper-container">
    <!-- =========================SLIDE==========================-->
    '''
    content += one
    content += '''
    <!-- ====================================================== -->
    </div></div>'''

    
# ===================end page & js===================
content += '''
    <div class="paper"><div class="paper-container">
      <div class="thanks">Thanks!</div></div>
    </div>
    </div>
    </div>
    <script type="text/javascript" src="/blog/weakpoint/core/weakpoint.js"></script>
    <script type="text/javascript">var weakpoint = new weakPoint(); weakpoint.init();</script>'''

    

    
# ====================ribbon====================
if ribbon_enable:
    content += '''
    <a href="https://github.com/zhblog"><img style="position: absolute; top: 0; right: 0; border: 0;" src="/blog/img/f.png" alt="Fork me on GitHub"></a>'''

    
# ==================html ends=====================
content += '''
    </body>
</html>'''


# =================write file=====================
fslide = codecs.open(outfile, mode="w", encoding="utf8")
fslide.write(content)
fslide.close()
