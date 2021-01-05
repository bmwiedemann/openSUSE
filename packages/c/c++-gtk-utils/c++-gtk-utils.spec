#
# spec file for package c++-gtk-utils
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%global flavor @BUILD_FLAVOR@%{nil}
%global soname 2_2-0

%global srcname c++-gtk-utils

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%define pkgname %{srcname}
%endif

%if "%{flavor}" == "gtk2"
%bcond_without gtk
%define _gtk 2
%define config_script configure-gtk2
%define gtk_dev_pkg pkgconfig(gtk+-2.0)
%define pkgname %{srcname}-gtk%{_gtk}
%endif

%if "%{flavor}" == "gtk3"
%bcond_without gtk
%define _gtk 3
%define config_script configure
%define gtk_dev_pkg pkgconfig(gtk+-3.0)
%define pkgname %{srcname}-gtk%{_gtk}
%endif

%if "%{flavor}" == "gtk4"
%bcond_without gtk
%define _gtk 4
%define config_script configure-gtk4
%define gtk_dev_pkg pkgconfig(gtk4)
%define pkgname %{srcname}-gtk%{_gtk}
%endif

%define libname libcxx-gtk-utils-%{_gtk}-%{soname}
%define devname libcxx-gtk-utils-%{_gtk}-devel

Name:           %{pkgname}
Version:        2.2.20
Release:        0
Summary:        Lightweight library for GTK+ programs using C++
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            http://cxx-gtk-utils.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/cxx-gtk-utils/cxx-gtk-utils/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  guile-devel
%if %{with gtk}
BuildRequires:  %{gtk_dev_pkg}
%endif

%description
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%package -n %{libname}
Summary:        Lightweight library for GTK+ programs using C++
Group:          System/Libraries

%description -n %{libname}
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%package -n %{devname}
Summary:        Lightweight library for GTK+ programs using C++ -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{devname}
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
if [ "%{config_script}" != "configure" ]
then
  cp -a %{config_script} configure
  cp -a %{config_script}.ac configure.ac
fi

%configure \
    --disable-static \
    --docdir=%{_docdir}/%{pkgname} \
    %{?with_gtk:--with-gtk} \
    %{!?with_gtk:--without-gtk} \
    %{nil}
%make_build

%install
%make_install
# Clean up
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libcxx-gtk-utils-%{_gtk}-2.2.so.*

%files -n %{devname}
%doc ChangeLog
%doc %{_docdir}/%{pkgname}
%{_includedir}/c++-gtk-utils-%{_gtk}-2.2/
%{_libdir}/libcxx-gtk-utils-%{_gtk}-2.2.so
%{_libdir}/pkgconfig/c++-gtk-utils-%{_gtk}-2.2.pc

%changelog
