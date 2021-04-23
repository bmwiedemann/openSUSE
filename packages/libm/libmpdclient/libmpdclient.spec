#
# spec file for package libmpdclient
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Tejas Guruswamy <tejas.guruswamy@opensuse.org>
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


%define so_name 2
%define vala_version %(rpm -q --queryformat='%{VERSION}' vala | sed 's/\.[0-9]*$//g')
Name:           libmpdclient
Version:        2.19
Release:        0
Summary:        Library for interfacing the Music Player Daemon
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://musicpd.org/libs/libmpdclient
Source0:        https://musicpd.org/download/libmpdclient/2/%{name}-%{version}.tar.xz
Source1:        doxygen-nodatetime-footer.html
Patch0:         libmpdclient-doxygen_nodatetime.patch
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  meson >= 0.37
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  vala

%description
A stable, documented, asynchronous API library for interfacing MPD (Music Player Daemon)
in the C, C++ & Objective C languages.

%package -n %{name}%{so_name}
Summary:        Library for interfacing the Music Player Daemon
Group:          System/Libraries

%description -n %{name}%{so_name}
A stable, documented, asynchronous API library for interfacing MPD (Music Player Daemon).

%package devel
Summary:        Development files for libmpdclient
Group:          Development/Languages/C and C++
Requires:       %{name}%{so_name} = %{version}

%description devel
This package contains the development files, e.g. header-files, for
libmpdclient - a stable, documented and asynchronous API library for
MPD (Music Player Daemon).

%prep
%setup -q
%patch0

%build
%meson -Ddocumentation=true -Dtest=true
cp %{SOURCE1} %{_vpath_builddir}/doc/
%meson_build

%install
%meson_install
mkdir -pv %{buildroot}%{_datadir}/vala-%{vala_version}/
mv %{buildroot}%{_datadir}/vala/* %{buildroot}%{_datadir}/vala-%{vala_version}/
rm -r %{buildroot}%{_datadir}/vala/
mkdir -p %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/doc/%{name}/* %{buildroot}%{_docdir}/%{name}/

%check
%meson_test

%post   -n %{name}%{so_name} -p /sbin/ldconfig
%postun -n %{name}%{so_name} -p /sbin/ldconfig

%files -n %{name}%{so_name}
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.*

%files devel
%doc %{_docdir}/%{name}/
%{_includedir}/mpd
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libmpdclient.pc
%dir %{_datadir}/vala-%{vala_version}/
%{_datadir}/vala-%{vala_version}/*

%changelog
