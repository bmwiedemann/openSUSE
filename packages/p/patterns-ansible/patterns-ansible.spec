#
# spec file for package patterns-ansible
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           patterns-ansible
Version:        1.0.0
Release:        0
Summary:        Patterns for Ansible automation
License:        MIT
Group:          Metapackages
URL:            https://www.suse.com/
BuildArch:      noarch

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

##############################
# ansible_automation
##############################

%package automation
Summary:        Ansible automation engine and Linux system roles
Group:          Metapackages
Provides:       pattern() = ansible_automation
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3100
Provides:       pattern-category() = Systems%20Management
Provides:       pattern-visible()
Requires:       ansible
Requires:       ansible-core
Requires:       ansible-linux-system-roles

%description automation
Ansible automation engine with SUSE Linux system roles for configuration
management of SUSE Linux Enterprise systems. Includes roles for network,
timesync, firewall, ssh, selinux, podman, cockpit, and more.

Install this pattern to manage your SLES fleet with Ansible.

##############################
# ansible_devtools (SLE 16+ / Tumbleweed only)
##############################

%if 0%{?suse_version} >= 1600
%package devtools
Summary:        Ansible development and testing tools
Group:          Metapackages
Provides:       pattern() = ansible_devtools
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 3110
Provides:       pattern-category() = Development
Provides:       pattern-visible()
Requires:       pattern() = ansible_automation
Requires:       ansible-lint
Requires:       molecule
Requires:       molecule-plugins
Requires:       ansible-navigator
Requires:       ansible-builder
Requires:       ansible-runner
Requires:       ansible-creator

%description devtools
Development and testing tools for Ansible content creation. Includes
ansible-lint for playbook linting, molecule for role testing,
ansible-navigator TUI, ansible-builder for execution environments,
ansible-runner for programmatic execution, and ansible-creator for
scaffolding new content.
%endif

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-ansible/
echo "This file marks the pattern automation to be installed." \
    > %{buildroot}%{_docdir}/patterns-ansible/automation.txt
%if 0%{?suse_version} >= 1600
echo "This file marks the pattern devtools to be installed." \
    > %{buildroot}%{_docdir}/patterns-ansible/devtools.txt
%endif

%files automation
%dir %{_docdir}/patterns-ansible
%{_docdir}/patterns-ansible/automation.txt

%if 0%{?suse_version} >= 1600
%files devtools
%dir %{_docdir}/patterns-ansible
%{_docdir}/patterns-ansible/devtools.txt
%endif

%changelog
