NAME = skupper

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))
export GOPATH := $(mkfile_dir)/tmpdir/

# make sure ./ is in the path,
# otherwise mockery is not found...
export PATH := :$(mkfile_dir)/tmpdir/bin:$(PATH)

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio vendor.tar.gz generated.tar.gz ./tmpdir

tar:
	osc service manualrun
	mkdir -p ./tmpdir/src/ && \
	rm -rf ./tmpdir/src/  && \
	echo "Copy files to ./tmpdir/src/" && \
	cp -r ./skupper/ ./tmpdir/src && \
	cd ./tmpdir/src/ && \
	echo "Starting go generate" && \
	./scripts/update-codegen.sh && \
	./scripts/libpod-generate.sh && \
	go mod download && \
	go mod vendor && \
	echo "Creating tarball vendor.tar.gz" && \
	tar czf ../../vendor.tar.gz ./vendor && \
	ls -lh ../../vendor.tar.gz && \
	echo "Creating tarball generated.tar.gz" && \
	tar czf ../../generated.tar.gz ./client/generated/ && \
	ls -lh ../../generated.tar.gz && \
	echo "Cleaning up" && \
	go clean -modcache && \
	cd ../../ && \
	rm -rf ./tmpdir && \
	echo "Finished"
