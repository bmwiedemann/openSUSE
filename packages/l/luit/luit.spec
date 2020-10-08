#
# spec file for package luit
#
# Copyright (c) 2020 SUSE LLC
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


Name:           luit
Version:        20201003
Release:        0
Summary:        Locale and ISO 2022 support for Unicode terminals
License:        MIT
Group:          System/X11/Utilities
URL:            http://invisible-island.net/luit/
Source0:        ftp://ftp.invisible-island.net/%{name}/%{name}-%{version}.tgz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Luit is a filter that can be run between an arbitrary application and a
UTF-8 terminal emulator. It will convert application output from the
locale's encoding into UTF-8, and convert terminal input from UTF-8 into
the locale's encoding.

%prep
%setup -q

%build
%configure --with-localealiasfile=%{_datadir}/X11/locale/locale.alias
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/luit
%{_mandir}/man1/luit.1%{?ext_man}

%changelog
