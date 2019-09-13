#
# spec file for package hamlib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   2
Name:           hamlib
Version:        3.3
Release:        0
Summary:        Run-time library to control radio transcievers and receivers
License:        LGPL-2.1-only
Group:          Productivity/Hamradio/Other
URL:            http://hamlib.sourceforge.net
#Git-Clone:     https://git.code.sf.net/p/hamlib/code
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE hamlib-3.0-perl_install.patch -- patch from Fedora
Patch0:         hamlib-3.0-perl_install.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(tcl)
Requires(post): info
Requires(preun): info

%description
The Ham Radio Control Libraries (Hamlib) provide a programming
interface for controlling radios and other shack hardware.
It is a software layer, not a complete user application.

%package devel
Summary:        Development files for hamlib, a set of radio control libraries
Group:          Development/Libraries/Other
Requires:       libhamlib%{sover} = %{version}
Requires:       libhamlib++%{sover} = %{version}

%description devel
Hamlib provide a programming interface for controlling radios and
other shack hardware.

%package -n libhamlib++%{sover}
Summary:        C++ interface of the Ham Radio Control Libraries
Group:          System/Libraries

%description -n libhamlib++%{sover}
Hamlib provides a programming interface for controlling radios and
other shack hardware. It is a software layer, not a complete user
application.

%package -n libhamlib%{sover}
Summary:        C interface of the Ham Radio Control Libraries
Group:          System/Libraries

%description -n libhamlib%{sover}
Hamlib provides a programming interface for controlling radios and
other shack hardware. It is a software layer, not a complete user
application.

%package -n lua-Hamliblua
Summary:        LUA bindings for Hamlib
Group:          Development/Libraries/Other

%description -n lua-Hamliblua
Hamlib provide a programming interface for controlling radios and
other shack hardware.

%package -n python-Hamlib
Summary:        Python bindings for Hamlib
Group:          Development/Libraries/Python

%description -n python-Hamlib
Hamlib provide a programming interface for controlling radios and
other shack hardware.

%package -n tcl-Hamlib
Summary:        Tcl bindings for Hamlib
Group:          Development/Languages/Tcl
%requires_eq    tcl

%description -n tcl-Hamlib
Hamlib provide a programming interface for controlling radios and
other shack hardware.

%package -n perl-Hamlib
Summary:        Perl bindings for Hamlib
Group:          Development/Languages/Perl

%description -n perl-Hamlib
Hamlib provide a programming interface for controlling radios and
other shack hardware.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure \
  --with-perl-binding \
  --with-tcl-binding \
  --with-lua-binding \
  --with-python-binding \
  --with-xml-support
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print

rm %{buildroot}%{perl_vendorarch}/auto/Hamlib/.packlist

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}%{_docdir}

%fdupes %{buildroot}%{python_sitearch}

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post -n libhamlib++%{sover} -p /sbin/ldconfig
%post -n libhamlib%{sover} -p /sbin/ldconfig
%postun -n libhamlib++%{sover} -p /sbin/ldconfig
%postun -n libhamlib%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS NEWS
%{_bindir}/rigctl
%{_bindir}/rigctld
%{_bindir}/rigmem
%{_bindir}/rigsmtr
%{_bindir}/rigswr
%{_bindir}/rotctl
%{_bindir}/rotctld
%{_mandir}/man1/rigctl.1%{?ext_man}
%{_mandir}/man1/rigctld.1%{?ext_man}
%{_mandir}/man1/rigmem.1%{?ext_man}
%{_mandir}/man1/rigsmtr.1%{?ext_man}
%{_mandir}/man1/rigswr.1%{?ext_man}
%{_mandir}/man1/rotctl.1%{?ext_man}
%{_mandir}/man1/rotctld.1%{?ext_man}
%{_mandir}/man7/hamlib-primer.7%{?ext_man}
%{_mandir}/man7/hamlib-utilities.7%{?ext_man}
%{_mandir}/man7/hamlib.7%{?ext_man}
%{_infodir}/hamlib.info%{?ext_info}
%{_docdir}/hamlib

%files devel
%dir %{_includedir}/hamlib
%{_includedir}/hamlib/*.h
%{_datadir}/aclocal/hamlib.m4
%{_libdir}/pkgconfig/hamlib.pc
%{_libdir}/libhamlib.so
%{_libdir}/libhamlib++.so

%files -n libhamlib%{sover}
%license COPYING COPYING.LIB
%{_libdir}/libhamlib.so.%{sover}*

%files -n libhamlib++%{sover}
%license COPYING COPYING.LIB
%{_libdir}/libhamlib++.so.%{sover}*

%files -n lua-Hamliblua
%{_libdir}/lua

%files -n python-Hamlib
%{python_sitearch}/Hamlib.*
%{python_sitearch}/_Hamlib.*

%files -n tcl-Hamlib
%dir %{_libdir}/tcl*/
%dir %{_libdir}/tcl*/Hamlib
%{_libdir}/tcl*/Hamlib/*

%files -n perl-Hamlib
%{perl_vendorarch}/*

%changelog
