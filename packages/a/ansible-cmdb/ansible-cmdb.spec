#
# spec file for package ansible-cmdb
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           ansible-cmdb
Version:        1.30
Release:        0
Summary:        Ansible Configuration Management Database
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/fboender/ansible-cmdb
Source:         https://github.com/fboender/ansible-cmdb/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ansible-cmdb-wrapper.sh
Patch0:         ansible-cmdb-dont-require-ushlex.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
# SECTION test requirements
BuildRequires:  python3-Mako
BuildRequires:  python3-PyYAML
BuildRequires:  python3-jsonxs
# /SECTION
Requires:       python3-Mako
Requires:       python3-PyYAML
Requires:       python3-jsonxs
Recommends:     ansible
BuildArch:      noarch

%description
Ansible-cmdb takes the output of Ansible's fact gathering and converts it into
a static HTML overview page (and other things) containing system configuration
information.
It supports multiple types of output (html, csv, sql, etc) and extending
information gathered by Ansible with custom data. For each host it also shows
the groups, host variables, custom variables and machine-local facts.

%prep
%setup -q
%patch0 -p1
echo %{version} > ./src/ansiblecmdb/data/VERSION
sed -i -e '/^#!\//, 1d' src/ansible-cmdb.py
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' \
  src/ansiblecmdb/data/tpl/html_fancy_split.py \
  src/ansiblecmdb/data/tpl/markdown_split.py
sed -i 's|#!%{_bindir}/python|#!%{_bindir}/python3|g' \
  test/f_inventory/dyninv.py \
  test/f_inventory/mixeddir/dyninv.py

%build
%python3_build

%install
%python3_install
# remove upstream supplied wrapper-script
rm -f %{buildroot}/%{_bindir}/ansible-cmdb
install -D -m0755 %{SOURCE1} %{buildroot}/%{_bindir}/ansible-cmdb
install -D -m0644 contrib/ansible-cmdb.man.1 %{buildroot}%{_mandir}/man1/ansible-cmdb.1
%fdupes %{buildroot}

%check
cd test/ && python3 ./test.py -v

%files
%license LICENSE
%doc README.md
%{_bindir}/ansible-cmdb
%{python3_sitelib}/ansiblecmdb*
%{python3_sitelib}/ansible_cmdb*
%dir %{_prefix}/lib/ansiblecmdb/
%{_prefix}/lib/ansiblecmdb//ansible-cmdb.py
%dir %{_prefix}/lib/ansiblecmdb/data
%{_prefix}/lib/ansiblecmdb/data/*
%{_mandir}/man1/ansible-cmdb.1%{ext_man}


%changelog
