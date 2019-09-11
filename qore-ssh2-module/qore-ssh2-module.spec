#
# spec file for package qore-ssh2-module
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


%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules

Name:           qore-ssh2-module
Version:        0.9.9
Release:        0
Summary:        SSH2 module for Qore
License:        LGPL-2.1+ or GPL-2.0+ or MIT
Group:          Development/Languages
Url:            http://qore.org
Source:         http://prdownloads.sourceforge.net/qore/%{name}-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libssh2-devel >= 1.1
BuildRequires:  openssl-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.5
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SSH2 module for the Qore Programming Language.

%prep
%setup -q

%build
%ifarch x86_64 ppc64 ppc64le x390x
c64=--enable-64bit
%endif
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug $c64
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{module_dir}
mkdir -p %{buildroot}%{_datadir}/doc/qore-ssh2-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s docs

%files
%defattr(-,root,root,-)
%{module_dir}
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES ChangeLog AUTHORS

%package doc
Summary:        SSH2 module for Qore
Group:          Development/Languages

%description doc
SSH2 module for the Qore Programming Language.

This RPM provides API documentation, test and example programs

%files doc
%defattr(-,root,root,-)
%doc docs/ssh2/html test/

%changelog
