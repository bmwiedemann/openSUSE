#!/usr/bin/env python3
#
#

from lxml import etree
from lxml.builder import ElementMaker

import os.path

CATATALOG_NS="urn:oasis:names:tc:entity:xmlns:xml:catalog"
CATALOG="file:///usr/share/xml/docbook/schema/dtd/{ver}/catalog.xml"

DB_VERSIONS=["4.1.2", "4.2", "4.3", "4.4", "4.5"]

DTD="-//OASIS//DTD DocBook XML V{ver}//EN"
CALS="-//OASIS//DTD DocBook CALS Table Model V{ver}//EN"
POOL="-//OASIS//ELEMENTS DocBook Information Pool V{ver}//EN"
HIER="-//OASIS//ELEMENTS DocBook Document Hierarchy V{ver}//EN"
GEN_ENT="-//OASIS//ENTITIES DocBook Additional General Entities V{ver}//EN"
NOTA="-//OASIS//ENTITIES DocBook Notations V{ver}//EN"
CHAR_ENT="-//OASIS//ENTITIES DocBook Character Entities V{ver}//EN"
ADD_CHAR_ENT="-//OASIS//ENTITIES DocBook Additional General Entities V{ver}//EN"
HTML="-//OASIS//ELEMENTS DocBook XML grep HTML Tables V{ver}//EN"


SYSTEM_IDENTIFIERS=[
    "http://www.oasis-open.org/docbook/xml/{ver}",
    "http://www.docbook.org/xml/{ver}",
    ]

MISC_IDENTIFIERS=[
    "-//OASIS//DTD XML Exchange Table Model 19990315//EN",
    ]

XML_ENTITIES=[
    ("ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamsa.ent",),

    ("ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamsb.ent",),

    ("ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamsc.ent",),

    ("ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamsn.ent",),

    ("ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamso.ent",),

    ("ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isoamsr.ent",),

    ("ISO 8879:1986//ENTITIES Box and Line Drawing//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isobox.ent",),

    ("ISO 8879:1986//ENTITIES Russian Cyrillic//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isocyr1.ent",),

    ("ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isocyr2.ent",),

    ("ISO 8879:1986//ENTITIES Diacritical Marks//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isodia.ent",),

    ("ISO 8879:1986//ENTITIES Greek Letters//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isogrk1.ent",),

    ("ISO 8879:1986//ENTITIES Monotoniko Greek//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isogrk2.ent",),

    ("ISO 8879:1986//ENTITIES Greek Symbols//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isogrk3.ent",),

    ("ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isogrk4.ent",),

    ("ISO 8879:1986//ENTITIES Added Latin 1//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isolat1.ent",),

    ("ISO 8879:1986//ENTITIES Added Latin 2//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isolat2.ent",),

    ("ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isonum.ent",),

    ("ISO 8879:1986//ENTITIES Publishing//EN//XML",
    "http://www.w3.org/200osc 3/entities/iso8879/isopub.ent",),

    ("ISO 8879:1986//ENTITIES General Technical//EN//XML",
    "http://www.w3.org/2003/entities/iso8879/isotech.ent",),
    ]

DOCBOOK_IDENTIFIERS={
    "4.1.2": [DTD, CALS, POOL, HIER, GEN_ENT, NOTA, CHAR_ENT, ADD_CHAR_ENT],
    "4.2":   [DTD, CALS, POOL, HIER, GEN_ENT, NOTA, CHAR_ENT, ADD_CHAR_ENT],
    "4.3":   [DTD, CALS, POOL, HIER, HTML, GEN_ENT, NOTA, CHAR_ENT, ADD_CHAR_ENT],
    "4.4":   [DTD, CALS, POOL, HIER, HTML, GEN_ENT, NOTA, CHAR_ENT, ADD_CHAR_ENT],
    "4.5":   [DTD, CALS, POOL, HIER, HTML, GEN_ENT, NOTA, CHAR_ENT, ADD_CHAR_ENT],
    }

E = ElementMaker(namespace=CATATALOG_NS, nsmap={None : CATATALOG_NS})

catalog = E.catalog
group = E.group
public = E.public
system = E.system
delpub = E.delegatePublic
delsys = E.delegateSystem
deluri = E.delegateURI
rewsys = E.rewriteSystem

def create_db_catalog():
    c = catalog()
    g = group({'id': 'docbook_4'})
    for version in DB_VERSIONS:
        g.append(etree.Comment(' === Version {ver} === '.format(ver=version)))
        for ident in DOCBOOK_IDENTIFIERS[version]:
            g.append(delpub({'publicIdStartString': ident.format(ver=version),
                             'catalog': CATALOG.format(ver=version)}))
        for sysid in SYSTEM_IDENTIFIERS:
            #g.append(delsys({'systemIdStartString': sysid.format(ver=version),
            #                 'catalog': CATALOG.format(ver=version)}))
            g.append(rewsys({'systemIdStartString': sysid.format(ver=version),
                             'rewritePrefix': os.path.dirname(CATALOG.format(ver=version))
                             }
                            ))

    # We use the latest DocBook version for our misc part:
    g.append(etree.Comment(' === Miscellenous === '))
    for misc in MISC_IDENTIFIERS:
        g.append(delpub(publicIdStartString=misc,
                        catalog=CATALOG.format(ver='4.5')))
    c.append(g)
    c.append(etree.Comment(' === XML Entities === '))
    c.append(create_entities_catalog())
    return c


def create_entities_catalog():
    g = group({'id': 'docbook_4_xmlentities'})
    entfile = "file:///usr/share/xml/docbook/schema/dtd/4.5/ent/{}"
    for pub, sys in XML_ENTITIES:
        e = sys.rsplit("/", 1)[-1]
        entity = entfile.format(e)
        g.append(public(publicId=pub,
                        uri=entity))
        g.append(system(systemId=sys,
                        uri=entity))
    return g


if __name__=="__main__":
    catalog = create_db_catalog()
    print(etree.tostring(catalog, encoding="unicode", pretty_print=True))
