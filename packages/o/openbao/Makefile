NAME = openbao
SPEC = openbao.spec

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio ui-*.tar.gz vendor.tar.gz

tar:
	osc service manualrun
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	ui=ui-$$version.tar && \
	wd=$$(pwd) && \
	tmpdir=$$(mktemp -d -p /tmp) && \
	cd $$tmpdir && \
	echo $$tmpdir && \
	cp -r $$wd/$(NAME) . && \
	cd $$tmpdir/$(NAME) && \
	ls -lh && \
        make install-ui-dependencies ember-dist && \
	tar -cf $$wd/$$ui ui http/ && \
	cd $$wd && \
	gzip -f $$ui && \
        rm -rf $$tmpdir
