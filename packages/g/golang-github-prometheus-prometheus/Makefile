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

.SILENT: package_lock_json
package_lock_json:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/create_package-lock_json.sh $(SPEC) nodejs24

.SILENT: node_modules
node_modules:
	osc service manualrun node_modules
	rm -f *tgz
