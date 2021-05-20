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
Version:        0.2.0
Release:        0
Summary:        Tool to automatically purge old trashed files
License:        GPL-3.0-or-later
URL:            http://www.logfish.net/pr/autotrash/
Source:         https://github.com/bneijt/autotrash/archive/v%{version}.tar.gz
# autotrash has been generated using pandoc -s -t man < doc/autotrash.md > autotrash.1
Source1:        autotrash.1
BuildArch:      noarch
Requires:       python3
BuildRequires:  python3

%description
Autotrash is a small python script to automatically remove (permanently delete)
trashed files. It relies on the FreeDesktop.org Trash files for it's deletion
information.

%prep
%setup -q
# if the pre-built autotrash.1 is outdated, the build will fail
cp %{SOURCE1} doc

%build
python3 setup.py build

cd doc
make

%install
python3 setup.py install --skip-build --root %{buildroot}

mkdir -p %{buildroot}%{_mandir}/man1
cp -a doc/%{name}.1* %{buildroot}%{_mandir}/man1

%files
%doc COPYING README.md TODO
%{_mandir}/man1/autotrash.1*
%{_bindir}/autotrash
%{python3_sitelib}/*

%changelog
