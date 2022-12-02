#
# spec file for package ansible-core
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550
# Leap15, SLES15
%define pythons python310
%define ansible_python python310
%define ansible_python_sitelib %python310_sitelib
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_sitelib %python3_sitelib
%endif

Name:           ansible-core
Version:        2.14.0
Release:        0
Summary:        Radically simple IT automation
License:        GPL-3.0-or-later
URL:            https://ansible.com/
Source:         https://files.pythonhosted.org/packages/source/a/ansible-core/ansible-core-%{version}.tar.gz
BuildArch:      noarch

# cannot be installed with ansible < 3 or ansible-base
Conflicts:      ansible < 3
Conflicts:      ansible-base
Conflicts:      ansible-test

BuildRequires:  %{ansible_python}-base >= 3.8
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{ansible_python}-botocore
BuildRequires:  %{ansible_python}-Jinja2 >= 3.0.0
BuildRequires:  %{ansible_python}-PyYAML >= 5.1
BuildRequires:  %{ansible_python}-cryptography
BuildRequires:  %{ansible_python}-curses
BuildRequires:  %{ansible_python}-packaging
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytz
BuildRequires:  (%{ansible_python}-resolvelib >= 0.5.3 and %{ansible_python}-resolvelib < 0.9.0)
# /SECTION
Requires:       %{ansible_python}-Jinja2 >= 3.0.0
Requires:       %{ansible_python}-PyYAML >= 5.1
Requires:       %{ansible_python}-cryptography
Requires:       %{ansible_python}-packaging
Requires:       %{ansible_python}-resolvelib < 0.9.0
Requires:       (%{ansible_python}-resolvelib >= 0.5.3 and %{ansible_python}-resolvelib < 0.9.0)

%description
Ansible is a radically simple IT automation system. It handles
configuration management, application deployment, cloud provisioning,
ad-hoc task execution, network automation, and multi-node orchestration. Ansible makes complex
changes like zero-downtime rolling updates with load balancers easy. More information on the Ansible `website <https://ansible.com/>`_.

%prep
%setup -q -n ansible-core-%{version}

for file in .git_keep .travis.yml ; do
  find . -name "$file" -delete
done

# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
    sed -i '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} \;

%build
%python_build

%install
%python_install
%fdupes %{buildroot}%{ansible_python_sitelib}

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/
mkdir -p %{buildroot}/%{_datadir}/ansible

# Create system directories that Ansible defines as default locations in
# ansible/config/base.yml
DATADIR_LOCATIONS='%{_datadir}/ansible/collections
%{_datadir}/ansible/plugins/doc_fragments
%{_datadir}/ansible/plugins/action
%{_datadir}/ansible/plugins/become
%{_datadir}/ansible/plugins/cache
%{_datadir}/ansible/plugins/callback
%{_datadir}/ansible/plugins/cliconf
%{_datadir}/ansible/plugins/connection
%{_datadir}/ansible/plugins/filter
%{_datadir}/ansible/plugins/httpapi
%{_datadir}/ansible/plugins/inventory
%{_datadir}/ansible/plugins/lookup
%{_datadir}/ansible/plugins/modules
%{_datadir}/ansible/plugins/module_utils
%{_datadir}/ansible/plugins/netconf
%{_datadir}/ansible/roles
%{_datadir}/ansible/plugins/strategy
%{_datadir}/ansible/plugins/terminal
%{_datadir}/ansible/plugins/test
%{_datadir}/ansible/plugins/vars'

UPSTREAM_DATADIR_LOCATIONS=$(grep -ri default lib/ansible/config/base.yml| tr ':' '\n' | grep '%{_datadir}/ansible')

if [ "$SYSTEM_LOCATIONS" != "$UPSTREAM_SYSTEM_LOCATIONS" ] ; then
    echo "The upstream Ansible datadir locations have changed.  Spec file needs to be updated"
    exit 1
fi

mkdir -p %{buildroot}%{_datadir}/ansible/plugins/
for location in $DATADIR_LOCATIONS ; do
    mkdir %{buildroot}"$location"
done
mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}%{_sysconfdir}/ansible/roles/
# fix for https://github.com/ansible/ansible/pull/24381
# resp. https://bugzilla.opensuse.org/show_bug.cgi?id=1137479
mkdir -p %{buildroot}%{ansible_python_sitelib}/ansible/galaxy/data/default/role/{files,templates}

cp examples/hosts %{buildroot}%{_sysconfdir}/ansible/
cp examples/ansible.cfg %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v docs/man/man1/*.1 %{buildroot}/%{_mandir}/man1/

cp -pr docs/docsite/rst .

%check
# NEVER ship untested pure python packages. Enable this before the final submit.
#python3 bin/ansible-test units -v --python %%{python3_version}

%files
%doc README.rst changelogs/CHANGELOG-v2.14.rst changelogs/CHANGELOG.rst changelogs/changelog.yaml
%license COPYING licenses/Apache-License.txt licenses/MIT-license.txt licenses/PSF-license.txt licenses/simplified_bsd.txt
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-connection
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-test
%{_bindir}/ansible-vault
%{ansible_python_sitelib}/ansible
%{ansible_python_sitelib}/ansible_core-%{version}*-info

%exclude %{ansible_python_sitelib}/ansible_test

%{_mandir}/man1/ansible.1%{?ext_man}*
%{_mandir}/man1/ansible-config.1%{?ext_man}*
%{_mandir}/man1/ansible-console.1%{?ext_man}*
%{_mandir}/man1/ansible-doc.1%{?ext_man}*
%{_mandir}/man1/ansible-galaxy.1%{?ext_man}*
%{_mandir}/man1/ansible-inventory.1%{?ext_man}*
%{_mandir}/man1/ansible-playbook.1%{?ext_man}*
%{_mandir}/man1/ansible-pull.1%{?ext_man}*
%{_mandir}/man1/ansible-vault.1%{?ext_man}*
%dir %{_sysconfdir}/ansible
%config(noreplace) %{_sysconfdir}/ansible/ansible.cfg
%config(noreplace) %{_sysconfdir}/ansible/hosts
%{_datadir}/ansible/

%changelog
