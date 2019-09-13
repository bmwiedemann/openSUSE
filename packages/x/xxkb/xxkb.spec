#
# spec file for package xxkb
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xxkb
Version:        1.11.1
Release:        0
Summary:        A keyboard layout indicator and switcher
License:        Artistic-2.0
Group:          System/X11/Utilities
Url:            http://xxkb.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}-src.tar.gz
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xxkb program is a keyboard layout switcher and indicator. Unlike the
programs that reload keyboard maps and use their own hot-keys, xxkb is a
simple GUI for XKB (X KeyBoard extension) and just sends commands to and
accepts events from XKB. That means that it will work with the existing
setup of your X Server without any modifications.

%prep
%setup -q

%build
xmkmf -a
make %{?_smp_mflags}

%install
make install install.man DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc README* LICENSE CHANGES.koi8
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.xpm
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XXkb
%{_mandir}/man1/%{name}.1x.gz

%changelog
