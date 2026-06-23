NAME = grafana
SPEC = $(NAME).spec

# Define a safe, colon-free path for NVM
NVM_DIR = /tmp/grafana-nvm-build

default: clean verify-deps install-nvm tar

verify-deps:
	@which yarn >/dev/null 2>&1 || ( echo "yarn not found; run \`sudo npm install -g yarn\`" && false )

install-nvm:
	@echo "Installing NVM locally into $(NVM_DIR)..."
	@set -e; \
	mkdir -p "$(NVM_DIR)"; \
	export NVM_DIR="$(NVM_DIR)"; \
	curl -f -sS -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash

clean:
	rm -f $(NAME)-*.tar $(NAME)-*.tar.gz ui-*.tar.gz
	rm -rf "$(NVM_DIR)"

tar:
	@set -e; \
	export NVM_DIR="$(NVM_DIR)"; \
	. "$$NVM_DIR/nvm.sh"; \
	osc service manualrun; \
	version=$$( awk '/^Version:/ {print $$2}' $(SPEC) ); \
	echo "Package version is $$version"; \
	basename=$(NAME)-$$version; \
	tar=$$basename.tar; \
	webassets_tarball=ui-$$version.tar.gz; \
	tmpdir=$$(mktemp -d -p .); \
	cd $$tmpdir; \
	tar xzf ../$$tar.gz; \
	cd $$basename; \
	# Patches for the JS frontend go after here \
	patch --no-backup-if-mismatch -p1 -i ../../0001-Add-source-code-reference.patch; \
	# End patches section \
	# Patches for Go modules go after here \
	patch --no-backup-if-mismatch -p1 -i ../../0005-Bump-edwards25519.patch; \
	# End of Go modules patches section \
	go mod download; \
	go mod verify; \
	go work vendor; \
	tar --format=posix -cf ../../vendor.tar vendor; \
	# avoid ".git can't be found" \
	git init; \
	# avoid "FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory" \
	export NODE_OPTIONS=--max_old_space_size=8192; \
	nvm install; \
	yarn install --immutable; \
	yarn run build; \
	echo "Updating $$basename/public in tarball..."; \
	tar czf ../../$$webassets_tarball public; \
	cd ../..; \
	gzip -f vendor.tar; \
	rm -rf $$tmpdir
