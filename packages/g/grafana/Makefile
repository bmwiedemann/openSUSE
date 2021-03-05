NAME = grafana
SPEC = $(NAME).spec

default: verify-deps clean tar

verify-deps:
	@which yarn >/dev/null 2>&1 || ( echo "yarn not found; run \`sudo npm install -g yarn\`" && false )

clean:
	rm -f $(NAME)-*.tar $(NAME)-*.tar.gz

tar:
	osc service disabledrun
	@version=$$( awk '/^Version:/ {print $$2}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	basename=$(NAME)-$$version && \
	tar=$$basename.tar && \
	tmpdir=$$(mktemp -d -p .) && \
	cd $$tmpdir && \
        gunzip ../$$tar.gz && \
	tar -xf ../$$tar && \
	# recreate tarball explicitly in a format that handles long filenames \
	tar --format=posix -cf ../$$tar $$basename && \
	cd $$basename && \
	# Patches for the JS frontend go after here \
	# No patches currently needed \
	# End patches section \
	yarn install --pure-lockfile && \
	yarn run build && \
	cd .. && \
	echo "Updating $$basename/public in tarball..." && \
	tar -rf ../$$tar $$basename/public && \
	cd .. && \
	gzip $$tar && \
	rm -rf $$tmpdir
