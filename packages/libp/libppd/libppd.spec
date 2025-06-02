#
# spec file for package libppd
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


Summary:        OpenPrinting libppd is a legacy support library for PPD files
License:        Apache-2.0
Group:          Hardware/Printing
URL:            https://github.com/OpenPrinting/libppd
Name:           libppd
Version:        2.1.1
Release:        0
# To get Source0 go to https://github.com/OpenPrinting/libppd/releases and use e.g.
# wget https://github.com/OpenPrinting/libppd/releases/download/2.1.1/libppd-2.1.1.tar.gz
Source0:        libppd-%{version}.tar.gz
BuildRequires:  cups-devel >= 2.2.2
BuildRequires:  libcupsfilters-devel >= 2.1.1
BuildRequires:  ghostscript >= 10.0.0
BuildRequires:  poppler-tools
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel

%description
This package provides the libppd library,
the legacy support library for PPD files, 
which is by 95% code overtaken from CUPS 2.x,
only what is needed to handle PPD files
(and also *.drv PPD generator files)
for retro-fitting legacy printer drivers.
As libppd is only for legacy PPD file support
no new features will be add to it.

%package -n libppd2
Summary:        The actual libppd 2.x version library
Group:          System/Libraries

%description -n libppd2
This package provides the libppd 2.x version library.

%package devel
Summary:        Development files for libppd
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libppd2 = %{version}

%description devel
This package contains the development files for libppd.

%prep
%autosetup -p1

%build
# No need to set our preferred architecture-specific flags for the compiler and linker
# via export CFLAGS="$RPM_OPT_FLAGS" and export CXXFLAGS="$RPM_OPT_FLAGS"
# because the RPM macro configure does that.
# --disable-mutool : disable filters using mutool because we use ghostcript
# --disable-acroread : disable filters using acroread
# --disable-genstrings : disable genstrings, GNU gettext message generator for the libppd PPD Compiler
#   because automated PPD generators are a generic security issue and in particular
#   using (possibly external) gettext translation strings is a known security issue
# --disable-ppdc-utils : disable ppdc utilities, to build PPD files from driver information files (*.drv)
# --enable-testppdfile : enable testppdfile utility, to test correctness and integrity of PPD files
%configure --disable-static \
           --enable-shared \
           --disable-silent-rules \
           --disable-mutool \
           --disable-acroread \
           --disable-ppdc-utils \
           --disable-genstrings \
           --enable-testppdfile \
           --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
# Do not ship libtool *.la files
rm -f %{buildroot}%{_libdir}/lib*.la

%post   -n libppd2 -p /sbin/ldconfig
%postun -n libppd2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/testppdfile
%dir %{_datadir}/ppdc
%{_datadir}/ppdc/*
%doc %{_defaultdocdir}/%{name}

%files -n libppd2
%defattr(-,root,root)
%{_libdir}/libppd.so.2*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/ppd
%{_includedir}/ppd/*
%{_libdir}/libppd.so
%{_libdir}/pkgconfig/libppd.pc

%changelog

