NAME = terragrunt

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))
export GOPATH := $(mkfile_dir)/tmpdir/

# make sure ./ is in the path,
# otherwise mockery is not found...
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
	echo "Installing mockery" && \
	go install github.com/vektra/mockery/v2@v2.43.0 && \
	echo "Starting go generate" && \
	go generate ./... && \
	go mod download && \
	go mod vendor && \
	echo "Creating tarball vendor.tar.gz" && \
	tar czf ../../vendor.tar.gz ./vendor && \
	ls -lh ../../vendor.tar.gz && \
	echo "Cleaning up" && \
	go clean -modcache && \
	cd ../../ && \
	rm -rf ./tmpdir && \
	echo "Finished"
