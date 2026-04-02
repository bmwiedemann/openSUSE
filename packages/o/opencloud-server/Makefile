.ONESHELL:
.SILENT: obs_scm obs_scm obs_go_modules web_assets_version obs_download_files idp_tarball
.PHONY: obs_scm obs_scm obs_go_modules web_assets_version obs_download_files idp_tarball

NAME = opencloud-server
DIRECTORY_NAME = opencloud
SPEC = opencloud-server.spec

default: clean obs_scm obs_go_modules web_assets_version obs_download_files idp_tarball

clean:
	rm -rf $(DIRECTORY_NAME) $(NAME)-*.obscpio idp-*.tar.gz web-*.tar.gz third-party-licenses-*.tar.gz vendor.tar.gz

obs_scm:
	osc service manualrun obs_scm
	osc service manualrun set_version

obs_go_modules:
	osc service manualrun go_modules

web_assets_version:
	web_assets_version="$$(awk -F ' = ' '/^WEB_ASSETS_VERSION/ {print $$2}' $(DIRECTORY_NAME)/services/web/Makefile)"
	sed -i "/^%define/ s/web_assets_version.*/web_assets_version $$web_assets_version/g" $(SPEC)

obs_download_files:
	osc service manualrun download_files

idp_tarball:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/prepare_webassets.sh $(NAME) pnpm
