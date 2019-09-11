#
# spec file for package xdriinfo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xdriinfo
Version:        1.0.6
Release:        0
Summary:        Query configuration information of DRI drivers
License:        MIT
Group:          System/X11/Utilities
Url:            https://wiki.freedesktop.org/dri/
Source0:        http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2
Source1:        http://ftp.x.org/pub/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
Driinfo can be used to query configuration information of direct rendering
drivers (DRI).

%prep
%setup -q

%build
%configure --x-includes=%{_includedir} --x-libraries=%{_libdir}

make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.1%{ext_man}

%changelog
