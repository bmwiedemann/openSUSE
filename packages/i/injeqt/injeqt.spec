#
# spec file for package injeqt
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015-2016 Mariusz Fik <fisiu@opensuse.org>.
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


%define libname libinjeqt1

Name:           injeqt
Version:        1.2.0
Release:        0
Summary:        Dependency injection framework for Qt
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            https://github.com/vogel/injeqt
Source:         %{name}-%{version}.tar.gz
Patch0:         fix-gcc71-compilation-errors.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
injeqt is an attempt to build a powerful and reliable dependency injection
framework on Qt's reflection based on MOC (meta-object compiler).

%package        devel
Summary:        Dependency injection framework for Qt
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
injeqt is an attempt to build a powerful and reliable dependency injection
framework on Qt's reflection based on MOC (meta-object compiler).

Files mandatory for development.

%package -n     %{libname}
Summary:        Dependency injection framework for Qt
Group:          Development/Libraries/C and C++

%description -n %{libname}
injeqt is an attempt to build a powerful and reliable dependency injection
framework on Qt's reflection based on MOC (meta-object compiler).

%prep
%setup -q
%patch0 -p0

%build
%cmake \
  -DDISABLE_EXAMPLES=ON \
  -DDISABLE_TESTS=ON
make %{?_smp_mflags}

%install
cd build
%make_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/injeqt.pc
%{_includedir}/%{name}

%changelog
