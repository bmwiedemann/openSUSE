NAME = terragrunt

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))
export GOPATH := $(mkfile_dir)/tmpdir/

# make sure ./ is in the path,
# otherwise mockgen is not found...
export PATH := :$(mkfile_dir)/tmpdir/bin:$(PATH)

default: clean tar

clean:
	rm -rf $(NAME) $(NAME)-*.obscpio vendor.tar.gz ./tmpdir

tar:
	osc service manualrun
	mkdir -p ./tmpdir/src/ && \
	rm -rf ./tmpdir/src/  && \
	echo "Copy files to ./tmpdir/src/" && \
	cp -r ./terragrunt/ ./tmpdir/src && \
	cd ./tmpdir/src/ && \
	echo "Installing mockgen" && \
	/usr/lib64/go/1.24/bin/go install go.uber.org/mock/mockgen@v0.5.2 && \
	echo "Starting go generate" && \
	/usr/lib64/go/1.24/bin/go generate ./... && \
	/usr/lib64/go/1.24/bin/go mod download && \
	/usr/lib64/go/1.24/bin/go mod vendor && \
	echo "Creating tarball vendor.tar.gz" && \
	tar czf ../../vendor.tar.gz ./vendor && \
	ls -lh ../../vendor.tar.gz && \
	echo "Cleaning up" && \
	go clean -modcache && \
	cd ../../ && \
	rm -rf ./tmpdir && \
	echo "Finished"
