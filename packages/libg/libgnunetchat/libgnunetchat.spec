#
# spec file for package libgnunetchat
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libgnunetchat
Version:        0.5.0
Release:        0
Summary:        Library for applications to utilize the Messenger service of GNUnet
License:        AGPL-3.0-or-later
URL:            https://www.gnunet.org/
Source:         https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/pub/gnu/gnunet/%{name}-%{version}.tar.gz.sig
# https://gnunet.org/~schanzen/3D11063C10F98D14BD24D1470B0998EF86F59B6A
Source3:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnunetarm) >= 0.21.2
BuildRequires:  pkgconfig(gnunetfs) >= 0.21.2
BuildRequires:  pkgconfig(gnunetgns) >= 0.21.2
BuildRequires:  pkgconfig(gnunetidentity) >= 0.21.2
BuildRequires:  pkgconfig(gnunetmessenger) >= 0.21.2
BuildRequires:  pkgconfig(gnunetnamestore) >= 0.21.2
BuildRequires:  pkgconfig(gnunetreclaim) >= 0.21.2
BuildRequires:  pkgconfig(gnunetregex) >= 0.21.2
BuildRequires:  pkgconfig(gnunetutil) >= 0.21.2

%description
This library is an abstraction layer using the client API from different GNUnet
services to provide the functionality of a typical messenger application. The
goal is to make developing such applications easier and independent of the GUI
toolkit. So people can develop different interfaces being compatible with
eachother despite visual differences, a few missing features or differences in
overall design.

%package devel
Summary:        Development files for libgnunetchat
Requires:       %{name} = %{version}

%description devel
This library is an abstraction layer using the client API from different GNUnet
services to provide the functionality of a typical messenger application. The
goal is to make developing such applications easier and independent of the GUI
toolkit. So people can develop different interfaces being compatible with
eachother despite visual differences, a few missing features or differences in
overall design.

This package contains files required for building with libgnunetchat

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc AUTHORS ChangeLog HOWTO.md
%{_libdir}/libgnunetchat.so

%files devel
%license COPYING
%{_includedir}/gnunet/gnunet_chat_lib.h
%{_libdir}/pkgconfig/gnunetchat.pc

%changelog
