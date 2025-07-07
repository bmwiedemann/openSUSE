#
# spec file for package libmpdclient
#
# Copyright (c) 2025 SUSE LLC
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
Name:           libmpdclient
Version:        2.23
Release:        0
Summary:        Library for interfacing the Music Player Daemon
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://musicpd.org/libs/%{name}
Source0:        https://musicpd.org/download/%{name}/%{sover}/%{name}-%{version}.tar.xz
Source1:        https://musicpd.org/download/%{name}/%{sover}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        doxygen-nodatetime-footer.html
Patch0:         %{name}-doxygen_nodatetime.patch
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
A stable, documented, asynchronous API library for interfacing MPD (Music Player Daemon)
in the C, C++ & Objective C languages.

%package -n %{name}%{sover}
Summary:        Library for interfacing the Music Player Daemon
Group:          System/Libraries

%description -n %{name}%{sover}
A stable, documented, asynchronous API library for interfacing MPD (Music Player Daemon).

%package devel
Summary:        Development files for libmpdclient
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains the development files, e.g. header-files, for
libmpdclient - a stable, documented and asynchronous API library for
MPD (Music Player Daemon).

%prep
%autosetup -p1

%build
%meson -Ddocumentation=true -Dtest=true
cp %{SOURCE3} %{_vpath_builddir}/doc
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}/* %{buildroot}%{_docdir}/%{name}

%check
%meson_test

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSES/BSD-2-Clause.txt LICENSES/BSD-3-Clause.txt
%doc AUTHORS
%{_libdir}/%{name}.so.*

%files devel
%doc %{_docdir}/%{name}
%{_includedir}/mpd
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
