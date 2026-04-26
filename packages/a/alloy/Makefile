.ONESHELL:
SHELL := /bin/bash

NVM_DIR ?= $(HOME)/.config/nvm

NAME = alloy
SPEC = alloy.spec

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar.gz ui-*.tar.gz vendor.tar.gz

tar:
	osc service manualrun download_files
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) )
	echo "Package version is $$version"
	basename=$(NAME)-$$version
	tar=$$basename.tar
	ui=ui-$$version.tar
	wd=$$(pwd)
	tmpdir=$$(mktemp -d -p /tmp)
	pushd $$tmpdir
	tar zxf $$wd/$$tar.gz
	pushd $$basename/internal/web/ui/
	. $(NVM_DIR)/nvm.sh
	npm install
	npm run build
	popd
	echo "Creating web assets tarball"
	tar zcf $$wd/$$ui.gz $$basename/internal/web/ui/dist/
	pushd $$basename/collector/
	go mod download
	go mod vendor
	go mod verify
	tar zcf $$wd/vendor.tar.gz vendor
	popd
	popd
	rm -rf $$tmpdir
