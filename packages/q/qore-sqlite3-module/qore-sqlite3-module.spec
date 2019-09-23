#
# spec file for package qore-sqlite3-module
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define module_api %(qore --module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules
Name:           qore-sqlite3-module
Version:        1.0.1
Release:        0
Summary:        Sqlite3 DBI module for Qore
License:        LGPL-2.1+
Group:          Development/Languages/Other
Url:            http://www.qore.org
Source:         http://prdownloads.sourceforge.net/qore/%{name}-%{version}.tar.gz
Patch1:         qore_sqlite3_module_add_ppc64le_to_config_guess.patch
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel
BuildRequires:  sqlite3-devel
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
Requires:       sqlite3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Sqlite3 DBI driver module for the Qore Programming Language.

%package doc
Summary:        Documentation and examples for the Qore sqlute3 module
Group:          Development/Languages/Other

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%files doc
%defattr(-,root,root,-)
%doc test docs

%prep
%setup -q
%patch1 -p1
%ifarch x86_64 ppc64 ppc64le x390x
c64=--enable-64bit
%endif
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug $c64
make %{?_smp_mflags}
find test -type f|xargs chmod 644
find docs -type f|xargs chmod 644

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{module_dir}
mkdir -p %{buildroot}%{_datadir}/doc/qore-pgsql-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root,-)
%{module_dir}
%doc COPYING README RELEASE-NOTES ChangeLog AUTHORS

%changelog
