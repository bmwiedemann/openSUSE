#
# spec file for package ansible
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

Name:           ansible
Version:        6.6.0
Release:        0
Summary:        Radically simple IT automation
License:        GPL-3.0+
URL:            https://ansible.com/
Source:         https://files.pythonhosted.org/packages/source/a/ansible/ansible-%{version}.tar.gz
Source99:       ansible-rpmlintrc
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  fdupes

# required to fix the azure collection line endings
BuildRequires:  dos2unix

# SECTION test requirements
BuildRequires:  ansible-core >= 2.13.6
# /SECTION

Requires:       ansible-core >= 2.13.6
BuildArch:      noarch

%description
Ansible is a radically simple model-driven configuration management, multi-node
deployment, and remote task execution system. Ansible works over SSH and does
not require any software or daemons to be installed on remote nodes. Extension
modules can be written in any language and are transferred to managed machines
automatically.

%prep
%setup -q -n ansible-%{version}

for file in .git_keep .travis.yml ; do
  find . -name "$file" -delete
done

# fix for wrong shebang:
sed -i 's|/Users/kbreit/Documents/Programming/ansible_collections/cisco/meraki/venv/bin/python|%{_bindir}/python3|g' ansible_collections/cisco/meraki/scripts/sublime-build/build.py.generic

# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
    sed -i '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} \;

find ./ -type f -exec \
    sed -i '1s|python$|python3|' {} \;

# remove .keep and .gitignore files
find ./ansible_collections/ -iname .gitignore -delete
find ./ansible_collections/ -iname .keep -delete

# azure collection has wrong file endings
find ./ansible_collections/azure -type f -exec dos2unix {} \;

# ./ansible_collections/lowlydba/sqlserver/ throws errors in rpmlint
# and is powershell only
rm -rf ./ansible_collections/lowlydba/sqlserver/

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}/%{python_sitelib}/ansible_collections/

%files
%doc CHANGELOG-v6.rst README.rst
%license COPYING
%{_bindir}/ansible-community
%{python_sitelib}/*

%changelog
