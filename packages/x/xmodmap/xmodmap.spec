#
# spec file for package xmodmap
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


%if 0%{?suse_version} >= 1550
%define UsrEtcMove 1
%endif

Name:           xmodmap
Version:        1.0.10
Release:        0
Summary:        Utility to modify keymaps and pointer button mappings in X
License:        MIT
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        Xmodmap.template
Source2:        Xmodmap.remote.template
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xmodmap program is used to edit and display the keyboard modifier
map and keymap table that are used by client applications to convert
event keycodes into keysyms. It is usually run from the user's
session startup script to configure the keyboard according to personal
tastes.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%if 0%{?UsrEtcMove}
install -m0644 -D %{SOURCE1} %{buildroot}%{_distconfdir}/X11/Xmodmap
install -m0644 -D %{SOURCE2} %{buildroot}%{_distconfdir}/X11/Xmodmap.remote
%else
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/Xmodmap
install -m0644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/Xmodmap.remote
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README.md
%if 0%{?UsrEtcMove}
%dir %{_distconfdir}/X11
%{_distconfdir}/X11/Xmodmap
%{_distconfdir}/X11/Xmodmap.remote
%else
%config %{_sysconfdir}/X11/Xmodmap
%config %{_sysconfdir}/X11/Xmodmap.remote
%endif
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1%{?ext_man}

%changelog
