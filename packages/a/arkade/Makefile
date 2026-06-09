.ONESHELL:
SHELL := /bin/bash

NAME = arkade
SPEC = arkade.spec

.SILENT: clean obs_services go_modules
default: clean obs_services go_modules

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar.gz fstail fstail.tar.gz gha-bump gha-bump.tar.gz vendor.tar.gz

obs_services:
	osc service manualrun

go_modules:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/vendor_go_modules.sh $(NAME) go1.26
