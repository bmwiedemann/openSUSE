#
# spec file for package yum-metadata-parser
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           yum-metadata-parser
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  sqlite-devel
Summary:        A fast metadata parser for yum
License:        GPL-2.0+
Group:          Development/Libraries/Python
Version:        1.1.2
Release:        0
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-1.0-quiet.patch
# PATCH-FIX-UPSTREAM yum-metadata-parser [bnc#802576]
Patch1:         %{name}-1.1.2-handle_2GB_sized_rpms.patch
# PATCH-FIX-UPSTREAM yum-metadata-parser
Patch2:         %{name}-1.1.2-weakdeps.patch
Url:            http://devel.linux.duke.edu/cgi-bin/viewcvs.cgi/yum-metadata-parser/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{suse_version} <= 1010
Requires:       python-sqlite
%endif
%py_requires

%description
Fast metadata parser for yum implemented in C.



Authors:
--------
    Tambet Ingo  <tambet@ximian.com>

%prep
%setup -q
%patch0
%patch1 -p1
%patch2

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install -O1 --prefix="%{_prefix}" --root="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog
%{py_sitedir}/*

%changelog
