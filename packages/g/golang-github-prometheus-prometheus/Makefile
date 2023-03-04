NAME = prometheus
SPEC = golang-github-prometheus-prometheus.spec

default: clean tar

clean:
	rm -f $(NAME)-*.tar $(NAME)-*.tar.gz

tar:
	osc service disabledrun
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	basename=$(NAME)-$$version && \
	tar=$$basename.tar && \
	web_ui=web-ui-$$version.tar && \
	wd=$$(pwd) && \
	tmpdir=$$(mktemp -d -p /tmp) && \
	cd $$tmpdir && \
	tar -zxf $$wd/$$tar.gz && \
	cd $$basename && \
        make assets npm_licenses assets-compress && \
	tar -cf $$wd/$$web_ui web/ui/static/react && \
        find web/ui/static -type f -name '*.gz' -exec tar -rf $$wd/$$web_ui "{}" \; && \
	tar -rf $$wd/$$web_ui web/ui/embed.go && \
	cd .. && \
	echo "Creating web assets tarball" && \
	mv $$basename/npm_licenses.tar.bz2 $$wd && \
	cd $$wd && \
	gzip -f $$web_ui && \
	rm -rf $$tmpdir
