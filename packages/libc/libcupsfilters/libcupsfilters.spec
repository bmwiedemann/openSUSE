#
# spec file for package libcupsfilters
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


Summary:        OpenPrinting libcupsfilters provides CUPS filters as library functions
License:        Apache-2.0
Group:          Hardware/Printing
URL:            https://github.com/OpenPrinting/libcupsfilters
Name:           libcupsfilters
Version:        2.1.1
Release:        0
# To get Source0 go to https://github.com/OpenPrinting/libcupsfilters/releases and use e.g.
# wget https://github.com/OpenPrinting/libcupsfilters/releases/download/2.1.1/libcupsfilters-2.1.1.tar.gz
Source0:        libcupsfilters-%{version}.tar.gz
BuildRequires:  cups-devel >= 2.2.2
BuildRequires:  ghostscript-devel >= 10.0.0
BuildRequires:  qpdf-devel >= 10.3.2
BuildRequires:  poppler-tools
BuildRequires:  pkgconfig(poppler-cpp) >= 0.19
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libexif-devel
BuildRequires:  fontconfig-devel
BuildRequires:  liblcms2-devel
BuildRequires:  dejavu-fonts
# Conflict with the old 'cups-filters' version 1.x RPM, see
# https://build.opensuse.org/request/show/1280274#comment-2149316
# which shows (excerpt)
#   found conflict of cups-filters-1.28.17-... with libcupsfilters-2.1.1-...
#     /usr/share/cups/banners/classified
#     ...
#     /usr/share/cups/data/unclassified.pdf
Conflicts:      cups-filters < 2.0.0

%description
This package provides the libcupsfilters library,
which in its 2.x version contains all the code
of the filters of the former cups-filters package
as library functions, the so-called filter functions.

%package -n libcupsfilters2
Summary:        The actual libcupsfilters 2.x version library
Group:          System/Libraries

%description -n libcupsfilters2
This package provides the libcupsfilters 2.x version library.

%package devel
Summary:        Development files for libcupsfilters
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libcupsfilters2 = %{version}
# Conflict with the old 'cups-filters-devel' version 1.x RPM, see
# https://build.opensuse.org/request/show/1280274#comment-2149316
# which shows (excerpt)
#   found conflict of cups-filters-devel-1.28.17-... with libcupsfilters-devel-2.1.1-...
#     /usr/lib64/libcupsfilters.so
#     ...
#     /usr/lib64/pkgconfig/libcupsfilters.pc
Conflicts:      cups-filters-devel < 2.0.0

%description devel
This package contains the development files for libcupsfilters.

%prep
%autosetup -p1

%build
# No need to set our preferred architecture-specific flags for the compiler and linker
# via export CFLAGS="$RPM_OPT_FLAGS" and export CXXFLAGS="$RPM_OPT_FLAGS"
# because the RPM macro configure does that.
# --disable-mutool : disable filters using mutool because we use ghostcript
# --enable-year2038 : support timestamps after 2038
%configure --disable-static \
           --enable-shared \
           --disable-silent-rules \
           --disable-mutool \
           --enable-year2038 \
           --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
# Do not ship libtool *.la files
rm -f %{buildroot}%{_libdir}/lib*.la

%post   -n libcupsfilters2 -p /sbin/ldconfig
%postun -n libcupsfilters2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %{_datadir}/cups
%dir %{_datadir}/cups/banners
%{_datadir}/cups/banners/*
%dir %{_datadir}/cups/charsets
%{_datadir}/cups/charsets/*
%dir %{_datadir}/cups/data
%{_datadir}/cups/data/*
%doc %{_defaultdocdir}/%{name}

%files -n libcupsfilters2
%defattr(-,root,root)
%{_libdir}/libcupsfilters.so.2*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/cupsfilters
%{_includedir}/cupsfilters/*
%{_libdir}/libcupsfilters.so
%{_libdir}/pkgconfig/libcupsfilters.pc

%changelog

