#
# spec file for package libpcd
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define sover 2

Name:           libpcd
Version:        1.0.1
Release:        0
Summary:        Library For Reading PhotoCD Images
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://bytesex.org/libpcd.html
Source:         http://www.kraxel.org/releases/libpcd/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libraries for reading PhotoCD images.

%package -n %{name}%{sover}
Summary:        Library For Reading PhotoCD Images
Group:          Development/Libraries/C and C++

%description -n %{name}%{sover}
Libraries for reading PhotoCD images.

%package      devel
Summary:        Library For Reading PhotoCD Images
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Header files for library for reading PhotoCD images.

%prep
%setup -q

%build
make prefix=%{_prefix} CFLAGS="%{optflags}" libdir=%{_libdir}  all

%install
make prefix=%{_prefix} CFLAGS="%{optflags}" DESTDIR=%{buildroot} libdir=%{buildroot}%{_libdir} install
rm -f %{buildroot}%{_libdir}/libpcd.a

%clean
rm -rf %{buildroot}

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%{_libdir}/libpcd.so.%{sover}*

%files devel
%defattr(-,root,root)
%doc pcd.html pcd.css
%doc README
%{_includedir}/pcd.h
%{_libdir}/libpcd.so

%changelog
