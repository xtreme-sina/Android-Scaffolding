#! /usr/bin/python2

from xml.dom import minidom, Node
import os

class ManifestDomHandler:
    
    domTree = None
    xmlFile = ""

    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
   
    def open_xml(self, xmlFile):
        self.domTree = None
        self.domTree = minidom.parse(xmlFile)
        return self.domTree
    
    def save_xml(self, xmlOutFile, outputDom):
        try:
            f = open(xmlOutFile, "w")
            f.write(outputDom.toxml())
            f.close()
        except:
            print "ERROR :: Could not update Android Manifest file."

    def add_activity_node(self, activityName):
        self.open_xml(self.xmlFile)
        appNodeList = self.domTree.getElementsByTagName("application")
        appNode = appNodeList.pop()
        if (appNode):
            newActivityNode = self.domTree.createElement("activity")
            newActivityNode.setAttribute("android:name", activityName)
            newActivityNode.appendChild(self.domTree.createTextNode("\n        "))
            appNode.appendChild(self.domTree.createTextNode("\n        "))
            appNode.appendChild(newActivityNode)
            appNode.appendChild(self.domTree.createTextNode("\n    "))
        self.save_xml(self.xmlFile, self.domTree) 

    def get_package_name(self):
        self.open_xml(self.xmlFile)
        manifestNode = self.domTree.getElementsByTagName("manifest").pop()
        package = ""
        if (manifestNode):
            package = manifestNode.getAttribute("package")
        return package

if __name__ == "__main__":
    if (os.path.exists("AndroidManifest.xml")):
        h = ManifestDomHandler("AndroidManifest.xml")
        h.add_activity_node("test")

