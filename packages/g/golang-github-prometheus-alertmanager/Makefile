.ONESHELL:
SHELL := /bin/bash

NAME = alertmanager
SPEC = golang-github-prometheus-alertmanager.spec

.SILENT: clean obs_download_files web_assets obs_go_modules
default: clean obs_download_files web_assets obs_go_modules

clean:
	rm -rf $(NAME) $(NAME)-*.tar.gz ui-*.tar.gz vendor.tar.gz

obs_download_files:
	osc service manualrun download_files

web_assets:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/tumbleweed:latest \
		bash /data/prepare_webassets.sh

obs_go_modules:
	osc service manualrun go_modules
