#
# spec file for package c++-gtk-utils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         soname 2_2-0

Name:           c++-gtk-utils
Version:        2.2.15
Release:        0
Summary:        Lightweight library for GTK+ programs using C++
License:        LGPL-2.1
Group:          System/Libraries
Url:            http://cxx-gtk-utils.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/cxx-gtk-utils/cxx-gtk-utils/%{version}/c++-gtk-utils-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  guile-devel
%if 0%{?favor_gtk2}
%define         _gtk 2
BuildRequires:  gtk2-devel
%else
%define         _gtk 3
BuildRequires:  gtk3-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%package -n libcxx-gtk-utils-%{_gtk}-%{soname}
Summary:        Lightweight library for GTK+ programs using C++
Group:          System/Libraries

%description -n libcxx-gtk-utils-%{_gtk}-%{soname}
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%package -n libcxx-gtk-utils-%{_gtk}-devel
Summary:        Lightweight library for GTK+ programs using C++ -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libcxx-gtk-utils-%{_gtk}-%{soname} = %{version}

%description -n libcxx-gtk-utils-%{_gtk}-devel
This is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper
such as gtkmm or wxWidgets.

%prep
%setup -q

%build
%if 0%{?favor_gtk2}
cp -a configure-gtk2 configure
cp -a configure-gtk2.ac configure.ac
%endif
%configure \
    --disable-static \
    --docdir=%{_docdir}/%{name}
make %{?_smp_flags}

%install
%make_install
# Clean up
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post -n libcxx-gtk-utils-%{_gtk}-%{soname} -p /sbin/ldconfig

%postun -n libcxx-gtk-utils-%{_gtk}-%{soname} -p /sbin/ldconfig

%files -n libcxx-gtk-utils-%{_gtk}-%{soname}
%defattr(-,root,root,-)
%doc COPYING NEWS
%{_libdir}/libcxx-gtk-utils-%{_gtk}-2.2.so.*

%files -n libcxx-gtk-utils-%{_gtk}-devel
%defattr(-,root,root,-)
%doc ChangeLog
%doc %{_docdir}/%{name}
%{_includedir}/c++-gtk-utils-%{_gtk}-2.2/
%{_libdir}/libcxx-gtk-utils-%{_gtk}-2.2.so
%{_libdir}/pkgconfig/c++-gtk-utils-%{_gtk}-2.2.pc
%changelog
