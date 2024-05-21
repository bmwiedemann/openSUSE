NAME = alloy
SPEC = alloy.spec

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar.gz ui-*.tar.gz vendor.tar.gz

tar:
	osc service manualrun
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	basename=$(NAME)-$$version && \
	obscpio=$$basename.obscpio && \
	ui=ui-$$version.tar && \
	wd=$$(pwd) && \
	tmpdir=$$(mktemp -d -p /tmp) && \
	cd $$tmpdir && \
	cpio -idv < $$wd/$$obscpio && \
	cd $$basename && \
	cd internal/web/ui/ && \
        yarn --network-timeout=1200000 && \
        yarn run build && \
	cd .. && \
	echo "Creating web assets tarball" && \
	tar -cf $$wd/$$ui ui/ && \
	cd $$wd && \
	gzip -f $$ui && \
	rm -rf $$tmpdir
