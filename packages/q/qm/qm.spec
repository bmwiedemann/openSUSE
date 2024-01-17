#
# spec file for package qm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


Name:           qm
Version:        2.3
Release:        0
Summary:        QMTest--General Purpose Testing Solution
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://www.codesourcery.com/qmtest/
Source:         qm-%{version}.tar.bz2
Patch1:         qm-firefox.patch
Patch2:         qm-doc.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
Requires:       python2-base
Requires:       python2-xml

%description
QMTest is a cost-effective general purpose testing solution that can be
used to implement a robust, easy to use testing process/

%prep
%setup -q
%patch1
%patch2

%build
%python2_build

%install
%python2_install
find %{buildroot}%{_datadir}/qm -type f \( -name "*.gif" -o -name "*.txt" -o -name "*.dtml" -o -name "*.css" \) -print0 | xargs -0 chmod 644
rm -rf %{buildroot}%{_docdir}/qm
%fdupes %{buildroot}

%files
%doc COPYING ChangeLog README
%{_bindir}/qmtest
%{_bindir}/qmtest.py
%{python2_sitearch}/*
%{_datadir}/qm/

%changelog
