list_of_title = ['Keypoints of Stage 1','Keypoints of Stage 2']
list_of_lession1 = ['1.1: the Basics of the Web and HTML','1.2: Creating a Structured Document','1.3: Adding CSS Style and HTML Structure']
list_of_lession2 = ['2.1: Introduction to Computer Science','2.2: Variables and Strings','2.3: Input & Function & Output','2.4: Control Flow &#38; Debugging','2.5: Structure Data &#38; How to Solve Problems']
list_of_lession = [list_of_lession1,list_of_lession2]
list_of_concepts_title_1_1 = ['Web components','How to write HTML','Inline vs Block Elements']
list_of_concepts_detail_1_1 = ["<ul>   <li>Browsers: A program that runs on the computers to display files found on the web.</li>     <li>Internet: the world's largest computer network.</li>  <li>HTTP: the main ptotocal of the web.</li> <li>Servers: computers that host the files that make up the web.</li>  </ul> Hypertext Markup Language (HTML) is a main type of documents on the web that glues everything together. Any type of documents can be found on the web, such as images, videos, texts, pdfs, and other web pages.",'HTML documents are made of HTML <em><b>elements</b></em>. The basic format of elements is: <br><br><span style="font-weight: bold; display: block; margin: 0px auto; text-align: center;" >&lt;name&gt; content &lt;/name&gt;.</span> <br>This <a href = "http://www.fing.edu.uy/tecnoinf/mvd/cursos/ria/material/teorico/html-tags-chart.pdf">tag chart</a> lists some frequently-used tags.','HTML elements are either <b>inline</b> or <b>block</b>. Block elements form an "invisible box" around the content inside of them.']
list_of_concepts_1_1 = [list_of_concepts_title_1_1,list_of_concepts_detail_1_1]
list_of_concepts_title_1_2 = ['Page Structure','Visual Styling','HTML-CSS-DOM','Boxifying Design']
list_of_concepts_detail_1_2 = ['<ul><li>All emlments are rectangular.</li><li>Tree like structure. </li> <li>HTML controls the "structure" of a web page.</li> </ul>','<ul>        <li>How is the stucture turned into a page? CSS controls the "style" of web page.</li>        <li>Document object model (DOM) is referred to tree-like structure of a page.</li> </ul>', '<ul>        <li>HTML is the web language &#8594; syntax+rules,</li>        <li>Tage is the "basic word" in HTML &#8594; element in tree.</li>        <li>CSS defines the "style". </li>      </ul>' ,'Everything on a web page is a box that can be divided from big to small. <br>  &lt;div&gt; can separate a web page into boxes.  <br>  More info about &lt;div&gt; and &lt;span&gt; can be found at <a href="http://www.w3schools.com/html/html_blocks.asp"> this page </a>.']
list_of_concepts_1_2 = [list_of_concepts_title_1_2,list_of_concepts_detail_1_2]
list_of_concepts_title_1_3 = ['Avoiding repetition','Understand CSS and thinking about inheritance','Set the attributes in CSS for different tags or classes','Web design process']
list_of_concepts_detail_1_3 = ['Avoiding repetition is the essential of programming. Cascading style sheet (CSS) let the coder avoid repetition.        <br>        <b>Avoiding Errors</b>: Without avoiding repetition, the code that do the same thing will often repeat over and over, like copying and pasting certain style attributes into many HTML elements or rewriting the same code (sometimes with minor differences) many times. This can lead to errors when the programmer decides to make a change to something. If they do not diligently make that same change everywhere the repeated code appears, problems will arise.                <br>        <b>Consistency</b>: Consistency is a key to a well-organized and elegant web page. The same style  can be assigned to each div and specified in only one place! It is also easy to make changes on that style.','CSS allows the descendant elements inherit property values from ancestor elements. Properties that can be inherited are color, font, letter-spacing, line-height, list-style, text-align, text-indent, text-transform, visibility, white-space and word-spacing. Properties that cannot be inherited are background, border, display, float and clear, height and width, margin, min- and max-height and -width, outline, overflow, padding, position, text-decoration, vertical-align and z-index. This <a href="http://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance">wiki-page</a> details inheritance of CSS.','The style of each element can be set by assigning attributes to tags or classes. ','<ul>        <li> Look for natural boxes</li>        <li> Look for repeated styles and semantic elements</li>        <li> Write the HTML </li>        <li> Apply style (from biggest to smallest)</li>        <li> Fix details</li>      </ul>']
list_of_concepts_1_3 = [list_of_concepts_title_1_3,list_of_concepts_detail_1_3]

list_of_concepts_1 = [list_of_concepts_1_1,list_of_concepts_1_2,list_of_concepts_1_3]

list_of_concepts_title_2_1 = ['Computer science','Web crawler','Programming','Python expression']
list_of_concepts_detail_2_1 = ['Breaking a problem into smaller pieces.  Precisely and mechanically describe a sequence of steps that can be used to solve each piece.','Seed page &#8594;flowing the link to find other pages.','Program tell the computer to act in a precise sequence of steps. There are many languages for programming. Most of them are high level language. For example, the Python interpreter translates  Python code into a low level language to run on computers. Programming language should avoid amiguity and verbosity. ','Python follows some certain grammar.        <br>        Expression &#8594; expression operator exoression</p>']
list_of_concepts_title_2_2 = ['Variables','Assignment statement','Strings']
list_of_concepts_detail_2_2 = ['Variable is the name of value. The existence of variables improves the code readability. ','name = expression','name = expression']

list_of_concepts_title_2_3 = ['What is a function?','What is the difference between making and using a function?','How do functions help programmers avoid repetition?','What happens if a function does not have a <span class="code">return</span> statement?']
list_of_concepts_detail_2_3 = ['A function is a series  of operations on input and then produce output. There is a python function example below:       <br>       <br>       <span class="code">        def restOfString(s):        <br>          &nbsp;&nbsp;return s[1:]       </span>       <br>        <br>          This function returns the rest of a string other than its first letter. ','Making a function is defining the action and parameters inside the function.        <br>        Using a function is, after making the function, calling this function to do some certain task','Functions only need to be defined once and allow use to operate the same action with different input.','<span class="code"> return </span> returns the output after calling the function. Without <span class="code">return</span>, although the function modified the input, but no output from the function and  nothing would happen.']

list_of_concepts_title_2_4 = ['Comparison operators','Debugging']
list_of_concepts_detail_2_4 = ['Comparison operators make decisions in if while and for statements, and can help controlling the function running flow. More details on python operators can be fund in <a href="http://www.tutorialspoint.com/python/python_basic_operators.htm">this page</a>. For more details on if, while, and for statements, visit <a href="https://docs.python.org/2/tutorial/controlflow.html"> this page</a>.','Bugs are inevitable. Do not panic or feel frustrating when bugs occur. Read the error message and trace back the line and function which make the code crashes. Use print statement to separate and observe the code in small sections and debugging. <a href="https://www.udacity.com/course/software-debugging--cs259">Debugging scientific approach for debugging</a> is a debugging course.Make your code more modular can help reducing bugs efficiently <b>Git</b> is a good version control tool.']

list_of_concepts_title_2_5 = ['List','Solving complex problem']
list_of_concepts_detail_2_5 = ['<b>String</b> and <b>list</b> are two kinds of structure data. Strings only contain a sequence of characters while list can be sequences of anything. list can be inside another list. List support mutation which means the value of the list can be changed after created. If both names refer to the same list, any changes affect one value name refers to also affect the values the other one refers to.','Do not panic! Identify the inputs and how they are represented. Then identify the outputs. Understand the relationship between the input and output with some examples. Test your thoughts with a simple mechanical solution. When it works, develop incrementally and test the results.']
list_of_concepts_2_1 = [list_of_concepts_title_2_1,list_of_concepts_detail_2_1]
list_of_concepts_2_2 = [list_of_concepts_title_2_2,list_of_concepts_detail_2_2]
list_of_concepts_2_3 = [list_of_concepts_title_2_3,list_of_concepts_detail_2_3]
list_of_concepts_2_4 = [list_of_concepts_title_2_4,list_of_concepts_detail_2_4]
list_of_concepts_2_5 = [list_of_concepts_title_2_5,list_of_concepts_detail_2_5]

list_of_concepts_2 = [list_of_concepts_2_1,list_of_concepts_2_2,list_of_concepts_2_3,list_of_concepts_2_4,list_of_concepts_2_5]




def make_stage_title(t):
	t = '<div><h1> '+ t + ' </h1></div>'
	return t

def make_lession_title(t):
	t = '<div><h2> '+ t +'</h2></div>'
	return t

def make_concepts_title(t):
	t = '<h3> ' + t + ' </h3>'
	return t

def make_concepts_detail(d):
	d = '''
			<p>
			  '''+ d +'''
			</p>'''
	return d

def make_concepts(title,detail):
	c = ''
	for i in range(0,len(title)):
		c = c + '''
		<div class="concepts">
			''' + make_concepts_title(title[i]) +  make_concepts_detail(detail[i]) + '''
		</div>'''
	return c

def make_lession(title,concepts):
	c = '''
	<div class = "lession">
		''' + make_lession_title(title) + make_concepts(concepts[0],concepts[1]) + '''
	</div>'''
	return c


def head(heading):
	c = '''
<head>
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>'''+ heading + '''</title>
</head>'''
	return c




# print make_stage_title(list_of_title[1])
# print make_lession_title(list_of_lession2[2])
# print make_concepts_title(list_of_concepts_title_1_1[2])
# print make_concepts_detail(list_of_concepts_detail_1_1[2])

#print make_concepts(list_of_concepts_title_1_1,list_of_concepts_detail_1_1)


print '''<!DOCTYPE html>
<html>'''

print head('ClassNote')
print '<body>'
for i in range(0,len(list_of_lession1)):
	print make_lession(list_of_lession1[i],list_of_concepts_1[i])
for i in range(0,len(list_of_lession2)):
	print make_lession(list_of_lession2[i],list_of_concepts_2[i])
print '</body>'
print '</html>'

