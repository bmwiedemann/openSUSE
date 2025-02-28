.ONESHELL:

NAME = zot-registry
SPEC = zot-registry.spec

default: clean zui_version

clean:
	rm -rf vendor.tar.gz $(NAME)-*.obscpio zui.tgz

zui_version:
	osc service manualrun
	@zui_version=$$( awk -F ' ' '/^ZUI_VERSION/ {print $$3}' ./zot/Makefile)
	sed -i "s/%define zui_version.*/%define zui_version $$zui_version/g" $(SPEC)
	osc service manualrun download_files
