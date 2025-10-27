.ONESHELL:

NAME = prometheus
SPEC = golang-github-prometheus-prometheus.spec

default: clean obs_scm go_modules package_lock_json node_modules

clean:
	rm -rf prometheus $(NAME)-*.tar $(NAME)-*.tar.gz $(NAME)-*.obscpio vendor.tar.gz package-lock.json  *[0-9].tgz

.SILENT: obs_scm
obs_scm:
	osc service manualrun obs_scm

.SILENT: go_modules
go_modules:
	osc service manualrun go_modules

.SILENT: node_modules
node_modules:
	osc service manualrun node_modules

.SILENT: package_lock_json
package_lock_json:
	echo "Preparing webui dependencies"
	version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) )
	echo "Setting basename"
	basename=$(NAME)-$$version
	echo "Setting obscpio"
	obscpio=$$basename.obscpio
	working_directory=$$(pwd)
	tmpdir=$$(mktemp -d -p /tmp)
	echo "Changing into tmpdir"
	cd $$tmpdir
	echo "Extracting obscpio archive"
	cpio -id < $$working_directory/$$obscpio
	echo "Changing into services"
	cd $$basename/web/ui/
	echo "Removing package-lock.json"
	rm -vf package-lock.json
	echo "Starting npm install"
	npm install --package-lock-only
	echo "Copy package-lock.json"
	cp -vf package-lock.json $$working_directory/
	echo "Cleaning up"
	cd $$working_directory/
	rm -rf $$tmpdir
	echo "Finished"
