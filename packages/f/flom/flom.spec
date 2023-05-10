#
# spec file for package flom
#
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           flom
Version:        1.6.0
Release:        0
Summary:        Distributed Lock Manager
License:        GPL-2.0-only
URL:            https://www.tiian.org/flom/
Source:         https://sourceforge.net/projects/flom/files/1.6.x-stable/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(dbus-1) >= 1.2.16
BuildRequires:  pkgconfig(gthread-2.0) >= 2.22
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(python)

%description
FLoM is a distributed lock manager that can be used to
synchronize shell commands, scripts and custom developed software. When used
in a shell environment, FLoM manages process synchronization in the same way
that "nice" manages process prioritization. It supports networking, abstract
resources, offers a library, encryption and peer authentication.

%package -n libflom0
Summary:        Distributed lock manager library

%description -n libflom0
FLoM is a distributed lock manager that can be used to
synchronize shell commands, scripts and custom developed software.

This package contains the shared library.

%package devel
Summary:        Distributed lock manager library
Requires:       libflom0 = %{version}

%description devel
FLoM is a distributed lock manager that can be used to
synchronize shell commands, scripts and custom developed software.

This package contains the files required to build programs with FLoM.

%prep
%autosetup -p1
# No network interface in OBS builds, seem to be only used for docs and tests.
# We would normally patch configure.ac and regenerate the files, but they are
# not portable to our versions.
sed -i -e '/find a valid network interface/,+15d' configure

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	--disable-perl \
	--disable-java \
	--disable-php \
	--disable-python \
	%{nil}
%make_build

%install
%make_install
find %{buildroot}/%{_libdir} -type f -name "*.a" -print -delete
find %{buildroot} -type f -name "*.la" -delete -print
# installed in files sections
rm %{buildroot}%{_docdir}/flom/COPYING
rm %{buildroot}%{_docdir}/flom/TestLog

%ldconfig_scriptlets -n libflom0

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%doc %dir %{_docdir}/flom
%doc %{_docdir}/flom/*.conf
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%license COPYING
%doc %dir %{_docdir}/flom
%doc %{_docdir}/flom/protocol.txt
%doc %{_docdir}/flom/html
%doc %{_docdir}/flom/examples
%{_includedir}/*
%{_libdir}/libflom.so

%files -n libflom0
%license COPYING
%{_libdir}/libflom.so.*

%changelog
