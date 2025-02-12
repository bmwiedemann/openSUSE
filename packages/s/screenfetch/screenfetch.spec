#
# spec file for package screenfetch
#
# Copyright (c) 2025 SUSE LLC
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


Name:           screenfetch
Version:        3.9.9
Release:        0
Summary:        Fetches system/theme information in terminal for Linux desktop screenshots
License:        GPL-3.0-only
Group:          System/X11/Terminals
URL:            https://github.com/KittyKatt/screenFetch
Source0:        %{URL}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       bc
Requires:       xprop
Recommends:     curl
Recommends:     lsb-release
Recommends:     scrot
Recommends:     xdpyinfo
BuildArch:      noarch

%description
screenFetch is a "Bash Screenshot Information Tool". This handy Bash
script can be used to generate one of those nifty terminal theme
information + ASCII distribution logos you see in everyone's screenshots
nowadays. It will auto-detect your distribution and display an ASCII
version of that distribution's logo and some valuable information to the
right. There are options to specify no ascii art, colors, taking a
screenshot upon displaying info, and even customizing the screenshot
command! This script is very easy to add to and can be easily extended.

%prep
%autosetup -n screenFetch-%{version}

%build
sed -i "s|%{_bindir}/env |/bin/|g" %{name}-dev

%install
install -D -p -m 0755 %{name}-dev \
  %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1   \
  %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc README.mkdn CHANGELOG TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_info}

%changelog
