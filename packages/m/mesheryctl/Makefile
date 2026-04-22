.ONESHELL:
.SILENT: clean osc_services cleanup_git_clone

NAME = mesheryctl

default: clean osc_services cleanup_git_clone

clean:
	rm -rf meshery *.obscpio vendor.tar.gz

osc_services:
	osc service manualrun

cleanup_git_clone:
	rm -rf meshery
