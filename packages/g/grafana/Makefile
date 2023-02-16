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
	patch --no-backup-if-mismatch -p1 -i ../../0001-Add-source-code-reference.patch && \
	patch --no-backup-if-mismatch -p1 -i ../../0002-Update-exporter-toolkit-to-version-0.7.3.patch && \
	# End patches section \
	go mod download && \
	go mod verify && \
	go mod vendor && \
	tar --format=posix -cf ../../vendor.tar vendor && \
	# avoid ".git can't be found" \
	git init && \
	# avoid "FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory" \
	export NODE_OPTIONS=--max_old_space_size=8192 && \
	yarn install --immutable && \
	yarn run build && \
	cd .. && \
	echo "Updating $$basename/public in tarball..." && \
	tar -rf ../$$tar $$basename/public && \
	cd .. && \
	gzip $$tar && \
	gzip -f vendor.tar && \
	rm -rf $$tmpdir
