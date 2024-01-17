#
# spec file for package jose
#
# Copyright (c) 2023 SUSE LLC
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


%define so_ver 0

Name:           jose
Version:        11
Release:        0
Summary:        C-language implementation of Javascript Object Signing and Encryption
License:        Apache-2.0
URL:            https://github.com/latchset/jose
Source0:        https://github.com/latchset/jose/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson) >= 2.10
BuildRequires:  pkgconfig(libcrypto) >= 1.0.2
BuildRequires:  pkgconfig(zlib)

%description
José is a C-language implementation of the Javascript Object Signing and Encryption standards.

%package -n lib%{name}%{so_ver}
Summary:        C-language implementation of Javascript Object Signing and Encryption

%description -n lib%{name}%{so_ver}
José is a C-language implementation of the Javascript Object Signing and Encryption standards.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{so_ver} = %{version}
Requires:       pkgconfig(jansson) >= 2.10
Requires:       pkgconfig(libcrypto) >= 1.0.2

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n lib%{name}%{so_ver}
%license COPYING
%{_libdir}/*.so.*
%{_mandir}/man3/*

%files -n lib%{name}-devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
