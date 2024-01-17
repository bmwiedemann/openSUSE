#
# spec file for package autotrash
#
# Copyright (c) 2021 SUSE LLC
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


Name:           autotrash
Version:        0.4.4
Release:        0
Summary:        Tool to automatically purge old trashed files
License:        GPL-3.0-or-later
URL:            http://www.logfish.net/pr/autotrash/
Source:         https://files.pythonhosted.org/packages/source/a/autotrash/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3
BuildRequires:  python3-setuptools

%description
Autotrash is a small python script to automatically remove (permanently delete)
trashed files. It relies on the FreeDesktop.org Trash files for it's deletion
information.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/autotrash
%{python3_sitelib}/*

%changelog
