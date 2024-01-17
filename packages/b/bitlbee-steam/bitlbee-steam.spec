#
# spec file for package bitlbee-steam
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bitlbee-steam
Version:        1.4.2
Release:        0
Summary:        Steam protocol plugin for BitlBee 
License:        GPL-2.0
Group:          Productivity/Networking/IRC
Url:            https://github.com/bitlbee/bitlbee-steam
Source:         https://github.com/bitlbee/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bitlbee)
BuildRequires:  libgcrypt-devel
# TODO why does the following not work?
#BuildRequires:  pkgconfig(libgcrypt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Steam protocol plugin for BitlBee 

%prep
%setup -q

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/bitlbee/steam.la

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%dir %{_libdir}/bitlbee
%{_libdir}/bitlbee/steam.so

%changelog
