.ONESHELL:

NAME = opencloud-server
DIRECTORY_NAME = opencloud
SPEC = opencloud-server.spec

default: clean obs_scm obs_go_modules web_assets_version obs_download_files idp_tarball

clean:
	rm -rf $(DIRECTORY_NAME) $(NAME)-*.obscpio idp-*.tar.gz web-*.tar.gz third-party-licenses-*.tar.gz vendor.tar.gz

.SILENT: obs_scm
obs_scm:
	osc service manualrun obs_scm
	osc service manualrun set_version

.SILENT: obs_go_modules
obs_go_modules:
	osc service manualrun go_modules

.SILENT: web_assets_version
web_assets_version:
	web_assets_version="$$(awk -F ' = ' '/^WEB_ASSETS_VERSION/ {print $$2}' $(DIRECTORY_NAME)/services/web/Makefile)"
	sed -i "/^%define/ s/web_assets_version.*/web_assets_version $$web_assets_version/g" $(SPEC)

.SILENT: obs_download_files
obs_download_files:
	osc service manualrun download_files

.SILENT: idp_tarball
idp_tarball:
	echo "Preparing idp tarball"
	version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) )
	echo "define basename"
	basename=$(NAME)-$$version
	echo "define obscpio"
	obscpio=$$basename.obscpio
	echo "define idp_tarball_name"
	idp_tarball_name=idp-$$version.tar.gz
	working_directory=$$(pwd)
	tmpdir=$$(mktemp -d -p /tmp)
	echo "Changing into tmpdir"
	cd $$tmpdir
	echo "Extracting obscpio archive"
	cpio -id < $$working_directory/$$obscpio
	echo "Changing into services"
	cd $$basename/services/idp/
	echo "Starting pnpm install"
	pnpm install --frozen-lockfile
	echo "Starting tarball creation"
	tar -czf $$working_directory/$$idp_tarball_name ./node_modules/
	echo "Tarball creation finished, cleaning up"
	cd $$working_directory/
	rm -rf $$tmpdir
	echo "Finished"
