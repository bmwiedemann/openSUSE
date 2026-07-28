.ONESHELL:

NAME = kubeone
SPEC = kubeone.spec

.SILENT: clean osc_service_manualrun kubernetes_version
default: clean osc_service_manualrun kubernetes_version

clean:
	rm -rf $(NAME) *.obscpio *.tar.gz

osc_service_manualrun:
	osc service manualrun

kubernetes_version:
	set -u
	echo "Finding out the kubernetes version"
	KUBERNETES_RELEASE_LINK="$$(cat $(NAME)/hack/stable-kubernetes-url.txt)"
	echo "KUBERNETES_RELEASE_LINK is set to $${KUBERNETES_RELEASE_LINK}"
	KUBERNETES_VERSION="$$(curl -SsL $${KUBERNETES_RELEASE_LINK})"
	echo "KUBERNETES_VERSION is set to $${KUBERNETES_VERSION}"
	sed -i "s/^%define KUBERNETES_STABLE_VERSION .*$$/%define KUBERNETES_STABLE_VERSION $${KUBERNETES_VERSION}/g" kubeone.spec
