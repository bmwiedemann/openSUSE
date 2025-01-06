#
# spec file for package libchewing
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


Name:           libchewing
%define soname	3
Version:        0.9.1
Release:        0
Summary:        Intelligent Phonetic Input Method Library for Traditional Chinese
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/chewing
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  corrosion
BuildRequires:  ncurses-devel
BuildRequires:  rust
BuildRequires:  sqlite3-devel
BuildRequires:  zstd
BuildRequires:  fdupes

%description
Intelligent phonetic input method library for traditional Chinese.

%package devel
Summary:        Development package for libchewing
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
Development package for libchewing.

%package -n %{name}%{soname}
Summary:        Chewing libraries
Group:          System/Libraries
Requires:       chewing-data

%description -n %{name}%{soname}
This package contains libraries for Chewing.

%package -n chewing-cli
Summary:        Chewing Command Line
Group:          System/I18n/Chinese

%description -n chewing-cli
This package provides command-line tool for Chewing.

%package -n chewing-data
Summary:        Data for libchewing
Group:          System/I18n/Chinese
BuildArch:      noarch

%description -n chewing-data
This package contains data files for libchewing.

%prep
%autosetup -a 1

%build
mkdir .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
cmake --preset rust-with-sqlite-release --install-prefix %{buildroot}%{_prefix}
cmake --build build

%check
cmake --build build -t test

%install
sed -i "s|prefix=%{buildroot}%{_prefix}|prefix=%{_prefix}|" build/chewing.pc
cmake --build build -t install

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
