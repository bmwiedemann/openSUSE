#
# spec file for package dunst
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?_userunitdir:%define _userunitdir %{_prefix}/lib/systemd/user}
Name:           dunst
Version:        1.4.1
Release:        0
Summary:        A customizable notification daemon
License:        BSD-3-Clause
Group:          System/GUI/Other
URL:            https://dunst-project.org
Source:         https://github.com/dunst-project/dunst/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         makefile.patch
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)

%description
Dunst is a customizable replacement for the notification daemons
provided by most desktop environments.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags}" make %{?_smp_mflags} all dunstify

%install
%make_install PREFIX=%{_prefix}
install -Dm755 dunstify %{buildroot}%{_bindir}/dunstify

sed -i -e 's/Exec.*/Exec=\/usr\/bin\/dunst/' %{buildroot}/%{_datadir}/dbus-1/services/org.knopwob.dunst.service
sed -i -e 's/ExecStart.*/ExecStart=\/usr\/bin\/dunst/' %{buildroot}/%{_userunitdir}/dunst.service

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/dunst
%{_bindir}/dunstify
%{_datadir}/dbus-1/services/org.knopwob.dunst.service
%{_userunitdir}/dunst.service
%{_datadir}/dunst
%{_mandir}/man1/dunst.1%{?ext_man}

%changelog
