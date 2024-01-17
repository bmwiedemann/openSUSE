#
# spec file for package libctl
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


Name:           libctl
Version:        4.5.1
Release:        0
%define somajor 7
Summary:        A guile Library for Scientific Simulations
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            https://libctl.readthedocs.io/en/latest/
Source0:        https://github.com/NanoComp/libctl/releases/download/v%{version}/libctl-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-fortran
BuildRequires:  guile-devel
BuildRequires:  libtool
BuildRequires:  nlopt-devel
BuildRequires:  pkg-config

%description
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

%package -n     %{name}%{somajor}
Summary:        A guile Library for Scientific Simulations
Group:          System/Libraries
# Missed SOVERSION bump
Conflicts:      libctl5 <= 4.5.0

%description -n %{name}%{somajor}
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

%package        devel
Summary:        Libraries and header files for libctl library
Group:          Development/Libraries/Other
Requires:       %{name}%{somajor} = %{version}
Recommends:     %{name}-doc = %{version}

%description    devel
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

This package contains libraries and header files for developing
applications that use libctl.

%package        doc
Summary:        Documentation for libctl library
Group:          Documentation/HTML

%description    doc
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

This package contains documentation for libctl library.

%prep
%setup -q

%build
autoreconf -fi
%configure --enable-shared --disable-static --disable-rpath F77=gfortran
make

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

install -d %{buildroot}%{_docdir}/%{name}/
install -m 644 {AUTHORS,NEWS.md,README.md} %{buildroot}%{_docdir}/%{name}/
cp -r doc/ %{buildroot}%{_docdir}/%{name}/

%post -n %{name}%{somajor} -p /sbin/ldconfig

%postun -n %{name}%{somajor} -p /sbin/ldconfig

%files -n %{name}%{somajor}
%license COPYING
%{_libdir}/libctl*.so.*

%files devel
%{_bindir}/gen-ctl-io
%{_libdir}/libctl*.so
%{_datadir}/libctl/
%{_includedir}/*
%{_mandir}/man1/gen-ctl-io.1*

%files doc
%{_docdir}/%{name}/

%changelog
