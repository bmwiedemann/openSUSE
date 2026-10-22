#
# spec file for package libchewing
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define soname	3
Name:           libchewing
Version:        0.13.1
Release:        0
Summary:        Intelligent Phonetic Input Method Library for Traditional Chinese
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/chewing/libchewing
Source:         https://codeberg.org/chewing/libchewing/releases/download/v%{version}/libchewing-%{version}.tar.zst
Source1:        vendor.tar.zst
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  corrosion
BuildRequires:  fdupes
BuildRequires:  rust
BuildRequires:  zstd
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sqlite3)

%description
Intelligent phonetic input method library for traditional Chinese.

%package devel
Summary:        Development package for libchewing
Requires:       %{name}%{soname} = %{version}

%description devel
Development package for libchewing.

%package -n %{name}%{soname}
Summary:        Chewing libraries
Requires:       chewing-data

%description -n %{name}%{soname}
This package contains libraries for Chewing.

%package -n chewing-cli
Summary:        Chewing Command Line

%description -n chewing-cli
This package provides command-line tool for Chewing.

%package -n chewing-data
Summary:        Data for libchewing
BuildArch:      noarch

%description -n chewing-data
This package contains data files for libchewing.

%prep
%autosetup -a 1

%build
cmake --preset rust-with-sqlite-release --install-prefix %{_prefix}
cmake --build build

%check
cmake --build build -t test

%install
cmake --install build --prefix %{buildroot}%{_prefix}

%fdupes %{buildroot}%{_includedir}

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libchewing.so.3
%{_libdir}/libchewing.so.3.3.1

%files -n chewing-cli
%{_bindir}/chewing-cli
%{_mandir}/man1/chewing-cli*.gz

%files -n chewing-data
%{_datadir}/%{name}/

%files devel
%{_includedir}/chewing/
%{_libdir}/libchewing.so
%{_libdir}/cmake/Chewing
%{_libdir}/pkgconfig/chewing.pc

%changelog
