#
# spec file for package wcslib
#
# Copyright (c) 2023 SUSE LLC
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


%define libver  8
Name:           wcslib
Version:        8.2.2
Release:        0
Summary:        An implementation of the FITS WCS standard
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/
Source0:        ftp://ftp.atnf.csiro.au/pub/software/wcslib/%{name}-%{version}.tar.bz2
BuildRequires:  cfitsio-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig

%description
WCSLIB is a C library, supplied with a full set of Fortran wrappers, that
implements the "World Coordinate System" (WCS) standard in FITS (Flexible Image
Transport System).

%package -n libwcs%{libver}
Summary:        An implementation of the FITS WCS standard
Group:          System/Libraries

%description -n libwcs%{libver}
WCSLIB is a C library, supplied with a full set of Fortran wrappers, that
implements the "World Coordinate System" (WCS) standard in FITS (Flexible Image
Transport System).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       cfitsio-devel
Requires:       libwcs%{libver} = %{version}
Recommends:     %{name}-doc
# libwcs-devel was last used in version 5.15
Provides:       libwcs-devel = %{version}
Obsoletes:      libwcs-devel <= 5.15

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary:        Documentation for %{name} library
# libwcs-doc was last used in version 5.15
Group:          Documentation/Other
Provides:       libwcs-doc = %{version}
Obsoletes:      libwcs-doc <= 5.15
BuildArch:      noarch

%description doc
This package contains documentation and help files for %{name} library.

%package tools
Summary:        Tools for %{name}
Group:          Productivity/Scientific/Other
Requires:       libwcs%{libver} = %{version}
# libwcs-tools was last used in version 5.15
Provides:       libwcs-tools = %{version}
Obsoletes:      libwcs-tools <= 5.15

%description tools
This package contains tools for working with files created or
opened with %{name}.

%prep
%autosetup -p1

%build
# Additional FLAGS from %%configure macro makes tests ("make check") fail in i586. So don't use them for now.
%ifarch %ix86
./configure --prefix=%{_prefix} -docdir=%{_docdir}/%{name} --without-pgplot
%else
%configure --docdir=%{_docdir}/%{name} --without-pgplot
%endif
%make_build

%install
%make_install

# Remove static libraries
rm -rf %{buildroot}%{_libdir}/*.a

%fdupes %{buildroot}%{_docdir}/%{name}/html
# recursive symlink
rm %{buildroot}%{_docdir}/%{name}/wcslib
# avoid rpmlint install-file-in-docs, not needed in rpm package
rm %{buildroot}%{_docdir}/%{name}/INSTALL

%check
make check

%post -n libwcs%{libver} -p /sbin/ldconfig
%postun -n libwcs%{libver} -p /sbin/ldconfig

%files -n libwcs%{libver}
%doc CHANGES
%license COPYING COPYING.LESSER
%{_libdir}/libwcs.so.%{libver}*

%files tools
%{_bindir}/HPXcvt
%{_bindir}/fitshdr
%{_bindir}/sundazel
%{_bindir}/tofits
%{_bindir}/wcsware
%{_mandir}/man1/HPXcvt.1%{?ext_man}
%{_mandir}/man1/fitshdr.1%{?ext_man}
%{_mandir}/man1/sundazel.1%{?ext_man}
%{_mandir}/man1/tofits.1%{?ext_man}
%{_mandir}/man1/wcsware.1%{?ext_man}

%files doc
%doc %{_docdir}/%{name}/

%files devel
%{_includedir}/wcslib
%{_includedir}/wcslib-%{version}/
%{_libdir}/libwcs.so
%{_libdir}/pkgconfig/wcslib.pc

%changelog
