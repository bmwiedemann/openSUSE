#
# spec file for package innoextract
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           innoextract
Version:        1.9
Release:        0
Summary:        A tool to extract Inno Setup installers under non-windows systems
License:        Zlib
Group:          Productivity/Archiving/Backup
URL:            http://constexpr.org/innoextract/
Source:         http://constexpr.org/innoextract/files/%{name}-%{version}.tar.gz
Source1:        http://constexpr.org/innoextract/files/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
BuildRequires:  cmake >= 2.8.0
BuildRequires:  gcc-c++
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. Inno Extracts allows to extract such installers under
non-windows systems without running the actual installer using wine. Inno
Extract currently supports installers created by Inno Setup 1.2.10 to
5.4.3.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/innoextract
%{_mandir}/man1/innoextract.1%{?ext_man}

%changelog
