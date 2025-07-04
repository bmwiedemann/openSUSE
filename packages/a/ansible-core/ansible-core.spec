#
# spec file for package ansible-core
#
# Copyright (c) 2025 SUSE LLC
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


%define ansible_core_major_minor_version 2.18

%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1550
# Leap15, SLES15
%if %pythons == "python310"
%define ansible_python python310
%define ansible_python_version 3.10
%define ansible_python_executable python3.10
%define ansible_python_sitelib %python310_sitelib
%endif
%if %pythons == "python311"
%define ansible_python python311
%define ansible_python_version 3.11
%define ansible_python_executable python3.11
%define ansible_python_sitelib %python311_sitelib
%endif
%else
# Tumbleweed
%define pythons python3
%define ansible_python python3
%define ansible_python_version %python3_version
%define ansible_python_executable python3
%define ansible_python_sitelib %python3_sitelib
%endif

Name:           ansible-core
Version:        2.18.6
Release:        0
Summary:        Radically simple IT automation
License:        GPL-3.0-or-later
URL:            https://ansible.com/
Source0:        https://files.pythonhosted.org/packages/source/a/ansible-core/ansible_core-%{version}.tar.gz#/ansible_core-%{version}.tar.gz
Source1:        ansible_core-%{version}.tar.gz.sha256
# PATCH-FIX-UPSTREAM fix resolvelib dependency
Patch1:         https://github.com/ansible/ansible/commit/771f7ad29ca4d259761eaa88673c2e32f6412bbe.patch
# PATCH-FIX-UPSTREAM unarchive-test-fix.patch -- Clamp zip timestamps on 32-bit time_t
# Upstream commit: d500354798beb9bf8341eb8e84e1e2046bbfd21b
# Reference: https://github.com/ansible/ansible/commit/d500354798beb9bf8341eb8e84e1e2046bbfd21b
Patch2:         unarchive-test-fix.patch
# Patch to fix distribution.py to identify the correct distribution for server-sap and micro
# Upstream pr https://github.com/ansible/ansible/pull/85152
Patch3:         suse-distribution-fix.patch
BuildArch:      noarch

# cannot be installed with ansible < 3 or ansible-base
Conflicts:      ansible < 3
Conflicts:      ansible-base

# cannot be installed with a lower or higher 2.X version
Conflicts:      ansible-core < %{ansible_core_major_minor_version}
Conflicts:      ansible-core > %{ansible_core_major_minor_version}

# https://github.com/ansible/ansible/blob/stable-2.18/pyproject.toml#L6
BuildRequires:  %{ansible_python}-base >= 3.11
BuildRequires:  %{ansible_python}-pip
BuildRequires:  %{ansible_python}-setuptools
BuildRequires:  %{ansible_python}-wheel
# https://github.com/ansible/ansible/blob/stable-2.18/requirements.txt
BuildRequires:  %{ansible_python}-Jinja2 >= 3.0.0
BuildRequires:  %{ansible_python}-PyYAML >= 5.1
BuildRequires:  %{ansible_python}-cryptography
BuildRequires:  %{ansible_python}-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  (%{ansible_python}-resolvelib >= 0.5.3 with %{ansible_python}-resolvelib < 2.0.0)
# SECTION test requirements
BuildRequires:  %{ansible_python}-botocore
BuildRequires:  %{ansible_python}-curses
BuildRequires:  %{ansible_python}-passlib
BuildRequires:  %{ansible_python}-pytest
BuildRequires:  %{ansible_python}-pytest-mock
BuildRequires:  %{ansible_python}-pytest-xdist
BuildRequires:  %{ansible_python}-pytz
BuildRequires:  git-core
BuildRequires:  openssh
# /SECTION
# SECTION docs
BuildRequires:  %{ansible_python}-docutils
# /SECTION
Requires:       %{ansible_python}-Jinja2 >= 3.0.0
Requires:       %{ansible_python}-PyYAML >= 5.1
Requires:       %{ansible_python}-cryptography
Requires:       %{ansible_python}-packaging
Requires:       %{ansible_python}-rpm
Requires:       (%{ansible_python}-resolvelib >= 0.5.3 with %{ansible_python}-resolvelib < 2.0.0)

# ansible-documentation is a separate package since 2.15.3
Recommends:     ansible-documentation

%description
Ansible is a radically simple IT automation system. It handles configuration
management, application deployment, cloud provisioning, ad-hoc task execution,
network automation, and multi-node orchestration. Ansible makes complex changes
like zero-downtime rolling updates with load balancers easy. More information
on the Ansible website <https://ansible.com/>.

%package -n ansible-test
Summary:        Tool for testing ansible plugin and module code
Requires:       %{name} = %{version}
BuildRequires:  %{ansible_python}-virtualenv
Requires:       %{ansible_python}-virtualenv
# cannot be installed with a lower or higher 2.X version
Conflicts:      ansible-test < %{ansible_core_major_minor_version}
Conflicts:      ansible-test > %{ansible_core_major_minor_version}

%description -n ansible-test
This package installs the ansible-test command for testing modules and plugins
developed for ansible.

Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%prep
%autosetup -p 1 -n ansible_core-%{version}

for file in .git_keep .travis.yml ; do
  find . -name "$file" -delete
done

# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
    sed -i '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} \;

# Replace all #!/usr/bin/python lines to use %{ansible_python_executable} directly.
find ./ -type f -exec \
    sed -i '1s|^#!%{_bindir}/python$|#!%{_bindir}/%{ansible_python_executable}|' {} \;

# fix shebangs in scripts
sed -i "1{/python3/d;}" ./lib/ansible/cli/*.py
sed -i "1{/python3/d;}" ./lib/ansible/cli/scripts/ansible_connection_cli_stub.py
sed -i "1{/python3/d;}" ./lib/ansible/modules/hostname.py

%build
%pyproject_wheel

mkdir man1
%{ansible_python_executable} packaging/cli-doc/build.py man --output-dir ./man1

%install
%pyproject_install
%fdupes %{buildroot}%{ansible_python_sitelib}

mkdir -p %{buildroot}%{_sysconfdir}/ansible/
mkdir -p %{buildroot}/%{_mandir}/man1/
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

mkdir -p %{buildroot}/%{_mandir}/man1/
cp -v ./man1/*.1 %{buildroot}/%{_mandir}/man1/

%check
export PYTHONPATH=%{ansible_python_sitelib}:$PWD
mkdir bin
cd bin
ln -s ../test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py ./ansible-test
cd ..
%{ansible_python_executable} bin/ansible-test units -v --python %{ansible_python_version}

%files
%doc changelogs/CHANGELOG-v%{ansible_core_major_minor_version}.rst changelogs/changelog.yaml
%license COPYING licenses/Apache-License.txt licenses/MIT-license.txt licenses/PSF-license.txt licenses/simplified_bsd.txt
%{_bindir}/ansible
%{_bindir}/ansible-config
%{_bindir}/ansible-console
%{_bindir}/ansible-doc
%{_bindir}/ansible-galaxy
%{_bindir}/ansible-inventory
%{_bindir}/ansible-playbook
%{_bindir}/ansible-pull
%{_bindir}/ansible-vault
%{ansible_python_sitelib}/ansible
%{ansible_python_sitelib}/ansible_core-%{version}*-info

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
%{_datadir}/ansible/

%files -n ansible-test
%{_bindir}/ansible-test
%{ansible_python_sitelib}/ansible_test

%changelog
