.ONESHELL:

NAME = opencloud-server
DIRECTORY_NAME = opencloud
SPEC = opencloud-server.spec

default: clean osc_services web_assets_version idp_tarball

clean:
	rm -rf $(DIRECTORY_NAME) $(NAME)-*.obscpio web-*.tar.gz third-party-licenses-*.tar.gz vendor.tar.gz

.SILENT: osc_services
osc_services:
	osc service manualrun

.SILENT: web_assets_version
web_assets_version:
	web_assets_version="$$(awk -F ' = ' '/^WEB_ASSETS_VERSION/ {print $$2}' $(DIRECTORY_NAME)/services/web/Makefile)"
	sed -i "/^%define/ s/web_assets_version.*/web_assets_version $$web_assets_version/g" $(SPEC)

.SILENT: idp_tarball
idp_tarball:
	echo "Preparing idp tarball"
	version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) )
	echo "define basename"
	basename=$(NAME)-$$version
	echo "define obscpio"
	obscpio=$$basename.obscpio
	echo "define idp_tarball_name"
	idp_tarball_name=idp_$$version.tar.gz
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
