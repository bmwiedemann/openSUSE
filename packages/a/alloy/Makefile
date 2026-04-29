.ONESHELL:
SHELL := /bin/bash

NAME = alloy
SPEC = alloy.spec

.SILENT: clean obs_download_files web_assets_and_go_modules
default: clean obs_download_files web_assets_and_go_modules

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar.gz ui-*.tar.gz vendor.tar.gz

obs_download_files:
	osc service manualrun download_files

web_assets_and_go_modules:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/prepare_webassets_and_vendor_go_modules.sh $(NAME) go1.26
