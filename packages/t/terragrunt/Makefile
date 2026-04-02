.ONESHELL:

NAME = terragrunt
GOLANG_EXECUTABLE_VERSION = 1.26

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))
export GOPATH := $(mkfile_dir)/tmpdir/

# make sure ./ is in the path,
# otherwise mockgen is not found...
export PATH := :$(mkfile_dir)/tmpdir/bin:$(PATH)

default: clean mockgen osc_service tar

.SILENT: tar

clean:
	# deleting the tmpdir requires root permissions
	sudo rm -rf $(NAME) $(NAME)-*.obscpio vendor.tar.gz ./tmpdir

mockgen:
	echo "Installing mockgen"
	mkdir -p ./tmpdir/
	/usr/lib64/go/1.24/bin/go install go.uber.org/mock/mockgen@v0.5.2
	ls -lh $(mkfile_dir)/tmpdir/bin

osc_service:
	osc service manualrun

tar:
	rm -rf ./tmpdir/src/*
	mkdir -p ./tmpdir/src/
	echo "Copy files to ./tmpdir/src/"
	cp -r ./terragrunt/ ./tmpdir/src/
	cd ./tmpdir/src/$(NAME)/
	ls -lah
	echo "Starting go generate"
	/usr/lib64/go/$(GOLANG_EXECUTABLE_VERSION)/bin/go generate ./...
	/usr/lib64/go/$(GOLANG_EXECUTABLE_VERSION)/bin/go mod download
	/usr/lib64/go/$(GOLANG_EXECUTABLE_VERSION)/bin/go mod vendor
	echo "Creating tarball vendor.tar.gz"
	tar czf ../../../vendor.tar.gz ./vendor
	ls -lh ../../../vendor.tar.gz
	echo "Cleaning up"
	go clean -modcache
	cd ../../../
	# deleting the tmpdir requires root permissions
	sudo rm -rf ./tmpdir
	echo "Finished"
