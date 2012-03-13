from lxml import etree
import types

def render_xml_response_from_dict(context):
    xml = etree.Element('xml')
    for k,v in context.items():
        child = etree.SubElement(xml,k)
        if type(v) == types.DictionaryType:
            for gk,gv in v.items():
                gchild = etree.SubElement(child,gk)
                gchild.text = gv
        else:
            child.text = str(v)
    return xml


def render_xml_response(context):
    xml = etree.Element('xml')
    for k,v in context.items():
        child = etree.SubElement(xml,k)
        if 'models' in type(v):
            for gk,gv in v.__dict__:
                gchild = etree.SubElement(child,gk)
                gchild.text = str(gv)
        else:
            child.text = str(v)
    return xml
