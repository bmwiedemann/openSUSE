#
# spec file for package transset
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


Name:           transset
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrender)
URL:            https://gitlab.freedesktop.org/xorg/app/transset
Version:        1.0.3
Release:        0
Summary:        Simple program to make windows transparent
License:        MIT
Group:          System/X11/Utilities
Source:         transset-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
transset manipulates the _NET_WM_WINDOW_OPACITY property to make
windows transparent.

%prep
%setup -n %{name}-%{version}

%build
%configure
%make_build

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%license COPYING
%doc README.md ChangeLog
%{_bindir}/transset
%{_mandir}/man1/transset.1%{?ext_man}

%changelog
