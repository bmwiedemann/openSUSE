#
# spec file for package dmenu
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


Name:           dmenu
Version:        4.8
Release:        0
Summary:        A generic and efficient menu for X
License:        MIT
Group:          System/GUI/Other
Url:            http://tools.suckless.org/dmenu/
Source:         http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch0:         dmenu-optflags.patch
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)

%description
dmenu is a dynamic menu for X, originally designed for dwm. It manages large numbers of user-defined menu items efficiently.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%optflags"
make X11LIB="%{_prefix}/X11R6/%{_lib}"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} \
    PREFIX="%{_prefix}"\
    DESTDIR=%{buildroot}
#

%files
%defattr(-,root,root)
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%{_bindir}/stest
%{_mandir}/man1/stest.1.gz

%changelog
