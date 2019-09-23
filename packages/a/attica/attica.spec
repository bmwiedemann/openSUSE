#
# spec file for package attica
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define _soversion 0_4

Name:           attica
Version:        0.4.2
Release:        0
Summary:        Open Collaboration Service client library
License:        LGPL-2.1+
Group:          System/GUI/KDE
Url:            https://projects.kde.org/attica
Source:         ftp://ftp.kde.org/pub/kde/stable/%{name}/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  cmake >= 2.8
BuildRequires:  kde4-filesystem
BuildRequires:  libqt4-devel
Requires:       libattica%{_soversion} = %{version}
Requires:       libqt4 > 4.7.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Attica is a library to access Open Collaboration Service servers.

%package -n libattica%{_soversion}
Summary:        Open Collaboration Service client library - development files
Group:          System/GUI/KDE

%description -n libattica%{_soversion}
Attica is a library to access Open Collaboration Service servers.

%package -n libattica-devel
Summary:        Open Collaboration Service client library - development files
Group:          Development/Libraries/C and C++
Requires:       libattica%{_soversion} >= %{version}
Requires:       libqt4-devel

%description -n libattica-devel
Development files for attica, Attica a library to access Open Collaboration Service servers.

%prep
%setup -q

%build
export RPM_OPT_FLAGS="%optflags -fvisibility-inlines-hidden"
%cmake_kde4 -d build
%make_jobs

%install
cd build
make DESTDIR=%{buildroot} install

%post -n libattica%{_soversion} -p /sbin/ldconfig

%postun -n libattica%{_soversion} -p /sbin/ldconfig

%files -n libattica%{_soversion}
%defattr(-,root,root)
%doc README AUTHORS COPYING
%{_libdir}/libattica*.so.*

%files -n libattica-devel
%defattr(-,root,root)
%{_libdir}/libattica*.so
%{_libdir}/pkgconfig/libattica*.pc
%{_includedir}/attica

%changelog
