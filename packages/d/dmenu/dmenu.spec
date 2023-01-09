#
# spec file for package dmenu
#
# Copyright (c) 2023 SUSE LLC
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


Name:           dmenu
Version:        5.2
Release:        0
Summary:        A generic and efficient menu for X
License:        MIT
Group:          System/GUI/Other
URL:            https://tools.suckless.org/dmenu/
Source:         http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         dmenu-optflags.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft) >= 2.3.5
BuildRequires:  pkgconfig(xinerama)

%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages
large numbers of user-defined menu items efficiently.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%make_build X11LIB="%{_prefix}/X11R6/%{_lib}"

%install
%make_install \
  PREFIX="%{_prefix}"\
  DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README
%{_bindir}/dmenu
%{_bindir}/dmenu_path
%{_bindir}/dmenu_run
%{_bindir}/stest
%{_mandir}/man1/dmenu.1%{?ext_man}
%{_mandir}/man1/stest.1%{?ext_man}

%changelog
