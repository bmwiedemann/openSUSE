#
# Makefile to install DocBook 4.x
#
# Author:
#   Thomas Schraitle <toms@opensuse.org>
#

ifndef PREFIX
  PREFIX := /usr
endif

# ifdef DESTDIR
#  DESTDIR := $(dir $(patsubst %/,%,$(dir $(DESTDIR))))
# endif

SHELL         := /bin/bash
PACKAGE       := docbook_4
VERSION       := 4.5
CDIR          := $(shell pwd)
#
DATADIR       := $(DESTDIR)$(PREFIX)/share
#
SGML_DIR      := $(DATADIR)/sgml
XML_DIR       := $(DATADIR)/xml

# Catalog stuff
DB_CATALOG_SRC   := $(PACKAGE).xml
XML_CATALOG_DIR  := $(DESTDIR)/etc/xml/catalog.d
XML_CATALOG      := $(XML_CATALOG_DIR)/$(DB_CATALOG_SRC)
SGML_CATALOGS    := $(wildcard CATALOG*)
SGML_CATALOG_DIR := $(SGML_DIR)
#
SGML_CONFIG_DIR  := $(DESTDIR)/var/lib/sgml
SGML_CATALOG_FILES := $(addprefix $(SGML_CONFIG_DIR)/,$(SGML_CATALOGS))
#
DB_XML_DIR       := $(XML_DIR)/docbook
DB_SGML_DIR      := $(SGML_DIR)/docbook
XML_SCHEMA_DIR   := $(DB_XML_DIR)/schema
#
DTD_SGML_DIR     := $(DB_SGML_DIR)/dtd
#
DB_VERSIONS      := 4.2 4.3 4.4 4.5
DB_XML_VERSIONS  := 4.1.2 $(DB_VERSIONS)
DB_SGML_VERSIONS := 4.1 $(DB_VERSIONS)

SGML_DB_PATHS    := $(foreach p,$(DB_SGML_VERSIONS),$(DTD_SGML_DIR)/$(p))
XML_IN_SGML_DIRS := $(addsuffix xml,$(foreach p,$(DB_XML_VERSIONS),$(DTD_SGML_DIR)/$(p)))

## All DTD paths and files (restricted to docbookx.dtd)
DTD_DEST_DIRS    := $(sort docbook-xml-4.1.2 $(wildcard docbook-xml-4.?))
DTD_DEST_DIRS    := $(subst -,/,$(patsubst docbook-%, %,$(DTD_DEST_DIRS)))
DTD_DEST_DIRS    := $(subst xml,dtd,$(DTD_DEST_DIRS))
DTD_DEST_DIRS    := $(addprefix $(XML_SCHEMA_DIR)/,$(DTD_DEST_DIRS))

DTD_DEST_FILES   := $(addsuffix /docbookx.dtd,$(DTD_DEST_DIRS))

# Add the DocBook SGML files too (HINT: SGML has docbook.dtd, without "x"!)
DTD_DEST_FILES   += $(addsuffix /docbook.dtd,$(SGML_DB_PATHS))

## All RNG paths and files (restricted to docbook.rng)
RNG_DEST_DIRS    := $(sort $(wildcard docbook-rng-4.?))
RNG_DEST_DIRS    := $(subst -,/,$(patsubst docbook-%, %,$(RNG_DEST_DIRS)))
RNG_DEST_DIRS    := $(addprefix $(XML_SCHEMA_DIR)/,$(RNG_DEST_DIRS))

RNG_DEST_FILES   := $(addsuffix /docbook.rng,$(RNG_DEST_DIRS))

## All XSD paths and files (restricted to docbook.xsd)
XSD_DEST_DIRS    := $(sort $(wildcard docbook-xsd-4.?))
XSD_DEST_DIRS    := $(subst -,/,$(patsubst docbook-%, %,$(XSD_DEST_DIRS)))
XSD_DEST_DIRS    := $(addprefix $(XML_SCHEMA_DIR)/,$(XSD_DEST_DIRS))

XSD_DEST_FILES   := $(addsuffix /docbook.xsd,$(XSD_DEST_DIRS))

# All destination files to be unpacked
ALL_DEST_FILES   := $(DTD_DEST_FILES) $(RNG_DEST_FILES) $(XSD_DEST_FILES)
XML_DB_PATHS     := $(DTD_DEST_DIRS) $(RNG_DEST_DIRS) $(XSD_DEST_DIRS)

# All installation directories that needs to be created before
INST_DIRECTORIES := $(XML_DB_PATHS) $(SGML_DB_PATHS) $(SGML_CONFIG_DIR) \
		    $(XML_CATALOG_DIR) $(SGML_CATALOG_DIR)


#-----------------------------
.PHONY: install
install: $(XML_CATALOG) $(SGML_CATALOG_FILES) $(ALL_DEST_FILES)
install: | $(XML_IN_SGML_DIRS)
	@echo "# Installed in $(DESTDIR)$(PREFIX)..."
#	@echo "DTD_DEST_DIRS=$(DTD_DEST_DIRS)"
#	@echo "SGML_CATALOGS=$(SGML_CATALOGS)"
#	@echo "SGML_CATALOG_FILES=$(SGML_CATALOG_FILES)"
	@echo "INST_DIRECTORIES=$(INST_DIRECTORIES)"
	@echo "DESTDIR=$(DESTDIR)"
	@echo "Finished."

$(SGML_CONFIG_DIR)/CATALOG.%: CATALOG.% | $(SGML_CONFIG_DIR) $(SGML_CATALOG_DIR)
	@echo "# Installing SGML catalog $<..."
# No longer wanted in /var hierarchy; see bsc#1093345
#	cp $< $(dir $@)
	cp $< $(SGML_CATALOG_DIR)

$(XML_IN_SGML_DIRS): | $(INST_DIRECTORIES)
	@echo "Creating link $@..."
	ln -s ../../../xml/docbook/schema/dtd/$(patsubst %xml,%,$(subst $(DTD_SGML_DIR)/,,$@)) $@

$(DTD_SGML_DIR)/%/docbook.dtd: docbook-sgml-%
	@echo "# Copying $<"
	@cp -a $</* $(dir $@)

$(XML_SCHEMA_DIR)/dtd/%/docbookx.dtd: docbook-xml-%
	@echo "# Copying $<"
	@cp -a $</* $(dir $@)

$(XML_SCHEMA_DIR)/rng/%/docbook.rng: docbook-rng-%
	@echo "# Copying $<"
	@cp -a $</* $(dir $@)

$(XML_SCHEMA_DIR)/xsd/%/docbook.xsd: docbook-xsd-%
	@echo "# Copying $<"
	@cp -a $</* $(dir $@)

$(XML_CATALOG): $(DB_CATALOG_SRC) | $(XML_CATALOG_DIR)
	@echo "# Installing XML Catalog..."
	install -m644 $< $@

# create needed directories
#
$(INST_DIRECTORIES):
	@mkdir -p $@

#-----------------------------
.PHONY: check
check:
	@echo "Checking DocBook4 Catalogs..."

	@for v in $(DB_XML_VERSIONS); do \
		echo "*** Checking version $$v..."; \
		xmlcatalog $(XML_CATALOG) "-//OASIS//DTD DocBook XML V$$v//EN" \
			"http://www.oasis-open.org/docbook/xml/$$v/docbookx.dtd" \
			"http://www.docbook.org/xml/$$v/docbookx.dtd" \
			"-//OASIS//DTD DocBook CALS Table Model V$$v//EN" \
			"-//OASIS//ELEMENTS DocBook Information Pool V$$v//EN" \
			"-//OASIS//ELEMENTS DocBook Document Hierarchy V$$v//EN" \
			"-//OASIS//ENTITIES DocBook Additional General Entities V$$v//EN" \
			"-//OASIS//ENTITIES DocBook Notations V$$v//EN" \
			"-//OASIS//ENTITIES DocBook Character Entities V$$v//EN" \
			"-//OASIS//ENTITIES DocBook Additional General Entities V$$v//EN" \
			; \
	done
