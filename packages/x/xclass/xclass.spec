#
# spec file for package xclass
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


Name:           xclass
%define lname	libxclass-0_9_2
Version:        0.9.2
Release:        0
Summary:        Library for Uniform Presentation of fvwm95 Programs
License:        GPL-2.0+ and LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://xclass.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-configs.patch
Patch1:         %{name}-%{version}-gcc-3.1.patch
Patch2:         %{name}-%{version}-gcc-4.0.patch
Patch3:         %{name}-%{version}-gcc-4.1.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix call of overloaded 'abs(unsigned int)' is ambiguous
Patch4:         %{name}-%{version}-gcc6.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a library for uniform presentation of fvwm95
programs.

%package -n %{lname}
Summary:        Library for Uniform Presentation of fvwm95 Programs
License:        LGPL-2.1+
Group:          System/Libraries
Requires:       %name

%description -n %{lname}
This package contains a library for uniform presentation of fvwm95
programs.

%package devel
Summary:        Development files for xclass
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xpm)

%description devel
This package contains development files for xclass library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%patch3
%patch4 -p1

%build
autoconf
%configure --disable-debug
make %{?_smp_mflags} shared
make %{?_smp_mflags} all

%install
mv lib/libxclass/icons/*.xpm icons/
%make_install
make DESTDIR=%{buildroot} install_shared
install -m 644 include/xclass/XCconfig.h %{buildroot}%{_includedir}/XCconfig.h
rm -rf %{buildroot}%{_docdir}/%{name}/INSTALL
rm -fv %{buildroot}/%{_libdir}/*.a

# kill pointless symlinks (libxclass.so.0)
find %{buildroot}/%{_libdir} -maxdepth 1 -type l -name "*.so.*" -delete
/sbin/ldconfig -N %{buildroot}/%{_libdir}

%fdupes %{buildroot}/%{_prefix}

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/
%config %{_sysconfdir}/xclassrc
%{_datadir}/xclass/

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libxclass.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/xc-config
%{_includedir}/XCconfig.h
%{_includedir}/xclass/
%{_libdir}/libxclass.so

%changelog
