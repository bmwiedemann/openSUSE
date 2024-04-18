#
# spec file for package i3lock
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 B1 Systems GmbH, Vohburg, Germany.
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


# Please submit bugfixes or comments via http://bugs.opensuse.org/
Name:           i3lock
Version:        2.15
Release:        0
Summary:        Screen Locker for the i3 Window Manager
License:        BSD-3-Clause
URL:            https://i3wm.org/i3lock/
Source:         https://i3wm.org/i3lock/%{name}-%{version}.tar.xz
# borrowed from gnome-icon-theme
Source2:        i3lock-icon.png
Source3:        xlock.sh
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
i3lock is a simple screen locker like slock. After starting it, you will see a
white screen (you can configure the color/an image). You can return to your
screen by entering your password.

%package xlock-compat
Summary:        Xlock-compatibility script which calls i3lock
Requires:       ImageMagick
Requires:       xdpyinfo
Conflicts:      xlockmore

%description xlock-compat
This package provides a script %{_bindir}/xlock which calls i3lock to lock your screen.
This is handy for hard-coded screen-saver invocations e.g. in XFCE4, so you can use
i3lock instead of xlock with them.

%prep
%autosetup -p 1

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install

install -D -m0644 %{name}.1 "%{buildroot}%{_mandir}/man1/%{name}.1"
install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/i3lock-xlock-compat/i3lock-icon.png
install -m0755 %{SOURCE3} %{buildroot}/%{_bindir}/xlock
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/* %{buildroot}%{_pam_vendordir}/
%endif

%pre
for i in pam.d/i3lock ; do
  test -f /etc/${i}.rpmsave && mv -v /etc/${i}.rpmsave /etc/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in pam.d/i3lock ; do
  test -f /etc/${i}.rpmsave && mv -v /etc/${i}.rpmsave /etc/${i} ||:
done

%files xlock-compat
%{_bindir}/xlock
%{_datadir}/%{name}-xlock-compat

%files
%license LICENSE
%doc CHANGELOG README.md
%if 0%{?suse_version} >= 1550
%{_pam_vendordir}/%{name}
%else
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
