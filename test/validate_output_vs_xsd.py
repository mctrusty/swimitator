'''
validate_output_vs_xsd checks to see that the swimitator xml generation functions produce xml that adheres to the 
xsd defined for its output formatting.

v. 0.1 is just a module with a basic main method, but future versions should flesh out more extensive testing using the
xsd (swimparser.appspot.com/xml/SwimXml.xsd) to check output validity
'''

import sys
sys.path.append("..\\swimitator")

import codecs
from lxml import etree
import swimxml
from StringIO import StringIO

def main():
	#Create schema instance
	xsd = '../swimitator/xml/SwimXml.xsd'
	enc = codecs.open(xsd, 'r', 'utf-8-sig')
	p = etree.parse(enc)
	schema = etree.XMLSchema(p)
	#etree.tostring(schema) 

	#generate swim xml and validate it
	s = '100 x 100 fr @1:30'
	xml = etree.parse(StringIO(swimxml.get_xml(s)))
	schema.assertValid(xml)	
  
if __name__ == "__main__":
	main()