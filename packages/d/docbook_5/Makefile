#
# Makefile to install DocBook 5.x
#
# Author:
#   Thomas Schraitle <toms@opensuse.org>
#

ifndef PREFIX
  PREFIX := /usr
endif

SHELL         := /bin/bash
PACKAGE       := docbook_5
VERSION       := 5.2CR3
DB_VERSIONS   := 5.0 5.1 5.2CR3
LAST_VER      := $(lastword $(DB_VERSIONS))
CDIR          := $(shell pwd)
#
DATADIR       := $(DESTDIR)$(PREFIX)/share
#
BINDIR        := $(DESTDIR)$(PREFIX)/bin
# Catalog stuff
DB_CATALOG_SRC  := $(PACKAGE).xml
XML_CATALOG_DIR := $(DESTDIR)/etc/xml/catalog.d
DB_CATALOG      := $(XML_CATALOG_DIR)/$(DB_CATALOG_SRC)
#
DB_XML_PATH   := $(DATADIR)/xml/docbook
SCHEMA_PATH   := $(DB_XML_PATH)/schema
#
XSLT_PATH     := $(DB_XML_PATH)/stylesheet/upgrade
#
DTD_PATH      := $(SCHEMA_PATH)/dtd
XSD_PATH      := $(SCHEMA_PATH)/xsd
RNG_PATH      := $(SCHEMA_PATH)/rng
SCH_PATH      := $(SCHEMA_PATH)/sch
NVDL_PATH     := $(SCHEMA_PATH)/nvdl
#
DB_DTD_PATHS  := $(DTD_PATH)/5.0
DB_XSD_PATHS  := $(XSD_PATH)/5.0
DB_RNG_PATHS  := $(foreach v,$(DB_VERSIONS),$(RNG_PATH)/$(v))
DB_SCH_PATHS  := $(foreach v,$(DB_VERSIONS),$(SCH_PATH)/$(v))
DB_NVDL_PATHS := $(foreach v,$(DB_VERSIONS),$(NVDL_PATH)/$(v))


INST_DIRECTORIES := $(XML_CATALOG_DIR) $(BINDIR) $(XSLT_PATH) \
		    $(DB_DTD_PATHS) $(DB_XSD_PATHS) $(DB_RNG_PATHS) $(DB_SCH_PATHS) $(DB_NVDL_PATHS)

DTD_SCHEMAS   := $(wildcard docbook-5.0/dtd/*.dtd)
DTD_SCHEMAS   := $(patsubst docbook-5.0/dtd/%,%,$(DTD_SCHEMAS))
DTD_SCHEMAS   := $(addprefix $(DB_DTD_PATHS)/,$(DTD_SCHEMAS))
#
XSD_SCHEMAS   := $(wildcard docbook-5.0/xsd/*.xsd)
XSD_SCHEMAS   := $(patsubst docbook-5.0/xsd/%,%,$(XSD_SCHEMAS))
XSD_SCHEMAS   := $(addprefix $(DB_XSD_PATHS)/,$(XSD_SCHEMAS))
#
NVDL_SCHEMAS  := $(wildcard $(foreach v,$(DB_VERSIONS),docbook-$(v)/*.nvdl))
NVDL_SCHEMAS  := $(subst docbook-,,$(NVDL_SCHEMAS))
NVDL_SCHEMAS  := $(addprefix $(NVDL_PATH)/,$(NVDL_SCHEMAS))
#
SCH_SCHEMAS   := $(wildcard $(foreach p,$(DB_VERSIONS),docbook-$(p)/sch/*))
SCH_SCHEMAS   := $(patsubst docbook-%,%,$(SCH_SCHEMAS))
SCH_SCHEMAS   := $(subst sch/,,$(SCH_SCHEMAS))
SCH_SCHEMAS   := $(addprefix $(SCH_PATH)/,$(SCH_SCHEMAS))
#
RNG_SCHEMAS    := $(wildcard $(foreach p,$(DB_VERSIONS),docbook-$(p)/rng/*.rn?))
RNG_SCHEMAS    := $(patsubst docbook-%,%,$(RNG_SCHEMAS))
RNG_SCHEMAS    := $(subst rng/,,$(RNG_SCHEMAS))
RNG_SCHEMAS    := $(addprefix $(RNG_PATH)/,$(RNG_SCHEMAS))
#
LINKS          := $(foreach v,$(DB_VERSIONS),$(NVDL_PATH)/$(v)/docbook.rng \
                    $(NVDL_PATH)/$(v)/docbook.sch)
COMPAT_LINKS   := $(NVDL_PATH)/5.2  $(RNG_PATH)/5.2  $(SCH_PATH)/5.2
ALL_DB_SCHEMAS :=  $(DTD_SCHEMAS) $(XSD_SCHEMAS) \
		   $(RNG_SCHEMAS) $(SCH_SCHEMAS) $(NVDL_SCHEMAS) \
		   $(LINKS)

#-----------------------------
# Make relative path 
define relpath =
  $(shell realpath --relative-to $(dir $(2)) $(dir $(1)))
endef

#-----------------------------
.PHONY: install
install: $(DB_CATALOG)
install: $(BINDIR)/db4-entities.pl
install: $(XSLT_PATH)/db4-upgrade.xsl
install: $(ALL_DB_SCHEMAS)
install: $(COMPAT_LINKS)
install: | $(INST_DIRECTORIES)
	@echo "Ready."

$(DTD_PATH)/5.0/%: docbook-5.0/dtd/% | $(DB_DTD_PATHS)
	@echo "### Installing DTD $<"
	install -m644 $< $@
$(XSD_PATH)/5.0/%: docbook-5.0/xsd/% | $(DB_XSD_PATHS)
	@echo "### Installing XSD $<"
	install -m644 $< $@

$(RNG_PATH)/5.0/%: docbook-5.0/rng/% | $(DB_RNG_PATHS)
	@echo "### Installing RNG 5.0 $<"
	install -m644 $< $@
$(RNG_PATH)/5.1/%: docbook-5.1/rng/% | $(DB_RNG_PATHS)
	@echo "### Installing RNG 5.1 $<"
	install -m644 $< $@
	
$(RNG_PATH)/$(LAST_VER)/%: docbook-$(LAST_VER)/rng/% | $(DB_RNG_PATHS)
	@echo "### Installing RNG $(LAST_VER) $<"
	install -m644 $< $@

$(SCH_PATH)/5.0/%: docbook-5.0/sch/% | $(DB_SCH_PATHS)
	@echo "### Installing Schematron 5.0 $<"
	install -m644 $< $@
$(SCH_PATH)/5.1/%: docbook-5.1/sch/% | $(DB_SCH_PATHS)
	@echo "### Installing Schematron 5.1 $<"
	install -m644 $< $@
	
$(SCH_PATH)/$(LAST_VER)/%: docbook-$(LAST_VER)/sch/%| $(DB_SCH_PATHS)
	@echo "### Installing Schematron $(LAST_VER) $<"
	install -m644 $< $@	

$(NVDL_PATH)/5.0/%: docbook-5.0/% | $(DB_NVDL_PATHS)
	@echo "### Installing NVDL 5.0 $<"
	install -m644 $< $@
$(NVDL_PATH)/5.1/%: docbook-5.1/% | $(DB_NVDL_PATHS)
	@echo "### Installing NVDL 5.1 $<"
	install -m644 $< $@
	
$(NVDL_PATH)/$(LAST_VER)/%: docbook-$(LAST_VER)/% | $(DB_NVDL_PATHS)
	@echo "### Installing NVDL $(LAST_VER) $<"
	install -m644 $< $@	

define NVDL_LINK_tmpl =
$(NVDL_PATH)/$(1)/docbook.$(3): $(2)/$(1)/docbook.$(3)
	@echo $$< $$@
	ln -s $$(call relpath,$$<,$$@)/$$(notdir $$<) $$@
endef
$(foreach v,$(DB_VERSIONS),$(eval $(call NVDL_LINK_tmpl,$(v),$(RNG_PATH),rng)))
$(foreach v,$(DB_VERSIONS),$(eval $(call NVDL_LINK_tmpl,$(v),$(SCH_PATH),sch)))


$(DB_CATALOG): $(DB_CATALOG_SRC) | $(XML_CATALOG_DIR)
	@echo "### Installing XML Catalog..."
	install -m644 $< $@

$(BINDIR)/db4-entities.pl: docbook-5.1/tools/db4-entities.pl | $(BINDIR)
	@echo "### Installing script db4-entities.pl"
	install -m755 $< $@
	
$(XSLT_PATH)/db4-upgrade.xsl: docbook-5.1/tools/db4-upgrade.xsl | $(XSLT_PATH)
	@echo "### Installing upgrade stylesheet..."
	install -m644 $< $@

$(NVDL_PATH)/5.2: $(NVDL_PATH)/$(LAST_VER) | $(DB_NVDL_PATHS)
	@echo "### Creating a link to $(NVDL_PATH)/5.2"
	ln -sv --relative $< $@

$(RNG_PATH)/5.2: $(RNG_PATH)/$(LAST_VER) | $(DB_RNG_PATHS)
	@echo "### Creating a link to $(RNG_PATH)/5.2"
	ln -sv --relative $< $@

$(SCH_PATH)/5.2: $(SCH_PATH)/$(LAST_VER) | $(DB_SCH_PATHS)
	@echo "### Creating a link to $(SCH_PATH)/5.2"
	ln -sv --relative $< $@

	
# create needed directories
#
$(INST_DIRECTORIES):
	@mkdir -p $@
