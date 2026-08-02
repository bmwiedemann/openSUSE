.ONESHELL:
.SILENT: obsservices prepare_webassets

NAME = prometheus
SPEC = golang-github-prometheus-prometheus.spec

default: clean obsservices prepare_webassets

clean:
	rm -rf $(NAME) $(NAME)-*.tar $(NAME)-*.tar.gz $(NAME)-*.obscpio web-*.tar.gz vendor.tar.gz

obsservices:
	echo "##########"
	echo "Running OBS services"
	osc service manualrun

prepare_webassets:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/prepare_webassets.sh
