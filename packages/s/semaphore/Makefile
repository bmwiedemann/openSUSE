.ONESHELL:
.SILENT: obsservices tar

NAME = semaphore
SPEC = semaphore.spec

default: clean obsservices tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar $(NAME)-*.tar.gz web-*.tar.gz vendor.tar.gz

obsservices:
	echo "##########"
	echo "Running OBS services"
	osc service manualrun

tar:
	podman run \
		-ti \
		--rm \
		--pull=always \
		-v .:/data/ \
		registry.opensuse.org/opensuse/leap:16.0 \
		bash /data/prepare_webassets.sh $(NAME) nodejs24
