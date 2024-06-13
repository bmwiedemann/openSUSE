#
# spec file for package xkeyboard-config
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xkeyboard-config
Version:        2.42
Release:        0
Summary:        The X Keyboard Extension
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://www.freedesktop.org/Software/XKeyboardConfig
Source:         https://xorg.freedesktop.org/archive/individual/data/%{name}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE disable-2xalt_2xctrl-toggle.diff fdo#4927 -- This is just a workaround until fdo#4927 is fixed
Patch109:       n_disable-2xalt_2xctrl-toggle.diff
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  xsltproc
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
Requires(post): coreutils
BuildArch:      noarch

%description
The X Keyboard Extension essentially replaces the core protocol
definition of keyboard. The extension makes possible to clearly and
explicitly specify most aspects of keyboard behaviour on per-key basis
and to more closely track the logical and physical state of the
keyboard. It also includes a number of keyboard controls designed to
make keyboards more accessible to people with physical impairments.

%lang_package

%prep
%autosetup -p1

%build
%{meson} \
    -Dxkb-base=%{_datadir}/X11/xkb \
    -Dcompat-rules=true \
    -Dxorg-rules-symlinks=true
%{meson_build}

%install
%{meson_install}
mkdir -p %{buildroot}%{_localstatedir}/lib/xkb
# Bug 335553
mkdir -p %{buildroot}%{_localstatedir}/lib/xkb/compiled/
ln -snf %{_localstatedir}/lib/xkb/compiled/ %{buildroot}%{_datadir}/X11/xkb/compiled
%find_lang %{name}
%fdupes -s %{buildroot}%{_datadir}/X11/xkb

%post
rm -rf %{_localstatedir}/lib/xkb/compiled/server*.xkm

%files
%license COPYING
%doc AUTHORS README docs/HOWTO.* docs/README.*
%dir %{_localstatedir}/lib/xkb
%dir %{_localstatedir}/lib/xkb/compiled
%dir %{_datadir}/X11
%{_datadir}/X11/xkb/
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man7/*

%files lang -f %{name}.lang

%changelog
