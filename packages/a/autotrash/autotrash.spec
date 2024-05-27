#
# spec file for package autotrash
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python3

Name:           autotrash
Version:        0.4.6
Release:        0
Summary:        Tool to automatically purge old trashed files
License:        GPL-3.0-or-later
URL:            https://github.com/bneijt/autotrash
Source:         https://files.pythonhosted.org/packages/source/a/autotrash/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildArch:      noarch

%description
Autotrash is a small python script to automatically remove (permanently delete)
trashed files. It relies on the FreeDesktop.org Trash files for it's deletion
information.

%prep
%autosetup
## Cleanup source for env and permissions
sed -i '/^#!/s/env \(.*\)$/\1/' src/autotrash/app.py
chmod 0755 src/autotrash/app.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/autotrash
%{python_sitelib}/autotrash
%{python_sitelib}/autotrash-%{version}.dist-info

%changelog
