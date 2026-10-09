#
# spec file for package shake-cursor
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define         realname Shake-Cursor
Name:           shake-cursor
Version:        1.0
Release:        0
Summary:        A utility to scale the cursor when shaken in X11
License:        MIT
URL:            https://github.com/Jonatas-Goncalves/Shake-Cursor
Source0:        https://github.com/Jonatas-Goncalves/%{realname}/archive/refs/tags/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
Recommends:     adwaita-icon-theme
Recommends:     xcursor-themes

%description
Shake-cursor is a lightweight X11 utility that temporarily enlarges the
mouse pointer dynamically when shaken rapidly, adapting to your active
desktop cursor theme.

%prep
%setup -q -n %{realname}-%{version}

%build
gcc %{optflags} -o shake-cursor shake-cursor.c -lX11 -lXcursor -lXrender -lXfixes -lXi -lm

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 shake-cursor %{buildroot}%{_bindir}/shake-cursor

mkdir -p %{buildroot}%{_userunitdir}
install -m 0644 shake-cursor.service %{buildroot}%{_userunitdir}/shake-cursor.service

%postun
%systemd_user_postun shake-cursor.service

%files
%license LICENSE
%{_bindir}/shake-cursor
%{_userunitdir}/shake-cursor.service

%changelog
