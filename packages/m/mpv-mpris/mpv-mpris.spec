#
# spec file for package mpv-mpris
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


Name:           mpv-mpris
Version:        0.5
Release:        0
Summary:        MPRIS plugin for mpv
License:        MIT
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/hoyon/mpv-mpris
Source0:        https://github.com/hoyon/mpv-mpris/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  mpv
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(mpv)
Supplements:    mpv
Obsoletes:      mpv-plugin-mpris

%description
This package contains a plugin for mpv which allows control of the
player using the MPRIS D-Bus interface, which enables control with
multimedia keys in desktop environments such as GNOME and KDE
as well as through tools like playerctl.

%prep
%setup -q

%build
%make_build

%install
install -Dm0755 mpris.so %{buildroot}%{_libdir}/mpv/mpris.so
mkdir -p %{buildroot}%{_sysconfdir}/mpv/scripts
ln -s %{_libdir}/mpv/mpris.so %{buildroot}%{_sysconfdir}/mpv/scripts/mpris.so

%files
%license LICENSE
%{_libdir}/mpv
%{_sysconfdir}/mpv/scripts/mpris.so

%changelog
