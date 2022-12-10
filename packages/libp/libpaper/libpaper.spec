#
# spec file for package libpaper
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 2

Name:           libpaper
Version:        2.0.4
Release:        0
Summary:        Enables users to indicate their preferred paper size
License:        GPL-3.0-or-later
URL:            https://github.com/rrthomas/libpaper
Source:         %{url}/releases/download/v%{version}/libpaper-%{version}.tar.gz
BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  perl
# libpaper-utils meanly packaged doc files in /usr/share/doc/packaes/libpaper
Conflicts:      libpaper-utils <= 1.1.28
# /etc/paperspecs used to live in paper (main package)
Provides:       paper:/etc/paperspecs
Conflicts:      paper <= 2.3

%description
This package enables users to indicate their preferred paper
size, provides the libpaper(1) utility to find the user's preferred
default libpaper size and give information about known sizes, and
specifies system-wide and per-user libpaper size catalogues, which can be
can also be used directly (see libpaperspecs(5)).

%package -n %{name}%{sover}
Summary:        This package contains the paper library
# To get /etc/paperspecs installed as used by libpaper
Requires:       %{name} >= %{version}

%description -n %{name}%{sover}
This package provides the paper library

%package -n %{name}-tools
Summary:        Tools that make use of libpaper
Provides:       paper = 2.4
Obsoletes:      paper <= 2.3
Provides:       libpaper-utils = 2.4
Obsoletes:      libpaper-utils <= 2.3

%description -n %{name}-tools
This package provides the 'paper' binary

%package devel
Summary:        This package contains the development files needed by libpaper
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains all devel files needed by the libpaper package

%prep
%autosetup -p1

%build
%configure \
  --disable-static
%make_build

%install
%make_install
rm -vRf %{buildroot}%{_datadir}/doc/libpaper/README
find %{buildroot}%{_libdir} -name *libpaper.la -delete

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README
%config %{_sysconfdir}/paperspecs
%{_mandir}/man5/paperspecs.5.gz

%files -n %{name}-tools
%{_bindir}/paper
%{_mandir}/man1/paper.1.gz

%files -n %{name}%{sover}
%{_libdir}/libpaper.so.%{sover}
%{_libdir}/libpaper.so.%{sover}.*

%files devel
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%changelog
