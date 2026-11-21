.ONESHELL:
.SILENT: obsservices webassets

NAME = netbird
SPEC = netbird.spec

default: clean obsservices prepare_webassets

clean:
	rm -rf $(NAME) $(NAME)-*.tar $(NAME)-*.tar.gz $(NAME)-*.obscpio frontend-*.tar.zst vendor.tar.zst

obsservices:
	echo "##########"
	echo "Running OBS services"
	osc service manualrun

prepare_webassets:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/:Z \
		registry.opensuse.org/opensuse/tumbleweed:20261111 \
		bash /data/prepare_webassets.sh $(NAME) nodejs24
