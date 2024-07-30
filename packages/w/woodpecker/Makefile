NAME = woodpecker
SPEC = woodpecker.spec

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.tar $(NAME)-*.tar.gz $(NAME)-*.obscpio vendor.tar.gz web-*.tar.gz

tar:
	osc service manualrun
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	basename=$(NAME)-$$version && \
	obscpio=$$basename.obscpio && \
	wd=$$(pwd) && \
	tmpdir=$$(mktemp -d -p /tmp) && \
	cd $$tmpdir && \
	echo "Extracting obscpio archive" && \
	cpio -id < $$wd/$$obscpio && \
	tar xvf $$wd/vendor.tar.gz && \
	cd $$basename/web/ && \
	rm -rf node_modules && \
	ls -lah && \
	pnpm install --frozen-lockfile && \
	pnpm build && \
	ls -lah && \
	cd .. && \
	tar czf $$wd/web-$$version.tar.gz ./web/ && \
	echo "DONE creating npm dependency offline cache file web-$$version.tar.gz" && \
	rm -rf $$tmpdir
