#
# spec file for package amtterm
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


Name:           amtterm
Version:        1.6
Release:        0
Summary:        Serial-over-lan (sol) client for Intel AMT
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://www.kraxel.org/releases/amtterm/
Source:         https://www.kraxel.org/releases/amtterm/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(vte-2.91)
Requires:       perl-SOAP-Lite

%description
AMT (included in Intel vPro and Centrino Pro) provides out-of-band
(OOB) management for Desktops and Laptops, using an agent integrated in
the network adapter and in the motherboard.

Serial-over-lan provides a (secure) way to connect a remote computer,
through a pseudo serial interface.

This package provide 2 terminals (amtterm and gamt) to connect to that
pseudo serial interface from a remote computer. amttool is a perl
script to gather informations about and remotely control AMT managed
computers.

%package gtk
Summary:    Serial-over-lan (sol) graphical client
License:        GPL-2.0-or-later
Group:          System/Management
Requires:       %{name} = %{version}

%description gtk
Graphical client for the amtterm utility

%prep
%setup -q

%build
make %{?_smp_mflags} prefix=%{_prefix}

%install
%make_install prefix=%{_prefix} STRIP=""

# fix icon and category
sed -i "/Icon/s/gnome-terminal/utilities-terminal/" %{buildroot}/%{_datadir}/applications/gamt.desktop
sed -i "/Categories/s/=.*/=System;Monitor/" %{buildroot}/%{_datadir}/applications/gamt.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/gamt.desktop

%files
%doc VERSION INSTALL
%license COPYING
%{_bindir}/amtterm
%{_bindir}/amttool
%{_mandir}/man1/amtterm.1%{?ext_man}
%{_mandir}/man1/amttool.1%{?ext_man}
%{_mandir}/man7/amt-howto.7%{?ext_man}

%files gtk
%{_bindir}/gamt
%{_mandir}/man1/gamt.1%{?ext_man}
%{_datadir}/applications/gamt.desktop

%changelog
