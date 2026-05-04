.ONESHELL:
.SILENT: obsservices webassets

NAME = woodpecker
SPEC = woodpecker.spec

default: clean obsservices webassets

clean:
	rm -rf $(NAME) $(NAME)-*.tar $(NAME)-*.tar.gz $(NAME)-*.obscpio web-*.tar.gz vendor.tar.gz

obsservices:
	echo "##########"
	echo "Running OBS services"
	osc service manualrun

webassets:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/prepare_webassets.sh $(NAME) nodejs24
