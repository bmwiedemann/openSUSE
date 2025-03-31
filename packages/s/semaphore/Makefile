NAME = semaphore
SPEC = semaphore.spec

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio $(NAME)-*.tar $(NAME)-*.tar.gz web-*.tar.gz vendor.tar.gz

tar:
	osc service manualrun
	@version=$$( awk '/^Version:/ {print $$2;exit;}' $(SPEC) ) && \
	echo "Package version is $$version" && \
	basename=$(NAME)-$$version && \
	tar=$$basename.tar && \
	web=web-$$version.tar.gz && \
	wd=$$(pwd) && \
	tmpdir=$$(mktemp -d -p /tmp) && \
	cd $$tmpdir && \
	cp -vr $$wd/$(NAME) ./$(NAME) && \
	cd $(NAME)/web/ && \
        mkdir -p dist/ && \
        npm install && \
        npm run build && \
        cd .. && \
	echo "Creating web assets tarball" && \
	tar -czf $$wd/$$web web/ api/ && \
	cd $$wd && \
	rm -rf $$tmpdir
