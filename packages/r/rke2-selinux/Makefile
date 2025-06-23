.ONESHELL:

NAME = rke2-selinux
SPEC = rke2-selinux.spec

default: clean osc_services package_versions

.PHONY: clean
clean:
	rm -rf $(NAME) $(NAME)-*.obscpio

.PHONY: osc_services
osc_services:
	osc service manualrun

.PHONY: package_versions
package_versions:
	selinux_policyver=$$( awk '/^%define selinux_policyver/ {print $$3}' $(NAME)/policy/microos/rke2-selinux.spec )
	echo "selinux_policyver is set to $$selinux_policyver"
	container_policyver=$$( awk '/^%define container_policyver/ {print $$3}' $(NAME)/policy/microos/rke2-selinux.spec )
	echo "container_policyver is set to $$container_policyver"

	echo "Replacing selinux_policyver"
	sed -i "/^%define selinux_policyver/ s/%define selinux_policyver.*/%define selinux_policyver $$selinux_policyver/" $(SPEC)
	echo "Replacing container_policyver"
	sed -i "/^%define container_policyver/ s/%define container_policyver.*/%define container_policyver $$container_policyver/" $(SPEC)
