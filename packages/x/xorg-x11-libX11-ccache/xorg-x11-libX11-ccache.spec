#
# spec file for package xorg-x11-libX11-ccache
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


%define mkcomposecache mkcomposecache-1.2.1

Name:           xorg-x11-libX11-ccache
Version:        7.6
Release:        0
Summary:        X
License:        MIT
Group:          System/Libraries
Url:            http://xorg.freedesktop.org/
Source:         http://xorg.freedesktop.org/archive/individual/app/%{mkcomposecache}.tar.bz2
Source1:        LICENSE
BuildRequires:  mkcomposecache
BuildRequires:  xbiff
BuildRequires:  xkeyboard-config
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-fonts
Provides:       xorg-x11:/var/X11R6/compose-cache/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cache for X.Org compose files.

%prep
%setup -q -n '%{mkcomposecache}'

%build

%install
cp -t. '%{SOURCE1}'
'./mkallcomposecaches.sh' \
 'prefix=%{_prefix}' \
 cachedir="%{buildroot}/%{_localstatedir}/cache/libx11/compose" xvfbopts="'-fp '\''%{_datadir}/fonts/misc'\'" /

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_localstatedir}/cache/libx11
%{_localstatedir}/cache/libx11/compose/

%changelog
