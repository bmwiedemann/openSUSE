#
# spec file for package xcm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Version:        0.5.4
Release:        0
Source:         xcm-%{version}.tar.bz2
Summary:        X Color Management tools
License:        MIT
Group:          System/X11/Utilities

Name:           xcm
Url:            http://www.oyranos.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(oyranos) >= 0.9.6
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcm)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }
%if 0%{?mandriva_version} > 0
BuildRequires:  Mesa
BuildRequires:  gcc-c++
BuildRequires:  libXcm-devel
BuildRequires:  liboyranos-devel >= 0.9.6
BuildRequires:  libtool-devel
BuildRequires:  mesagl-devel
BuildRequires:  pkgconfig
%endif
%if 0%{?fedora_version} > 0
BuildRequires:  libtool-ltdl-devel
%endif
%if 0%{?fedora_version} > 0 || 0%{?rhel_version} > 0 || 0%{?centos_version} > 0
BuildRequires:  Mesa
BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  libXcm-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires:  liboyranos-devel >= 0.9.6
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-Mesa-devel
%endif

%description
The Xcm tools are colour management helpers for Xorg.
A EDID parser and a colour management events observer are included.



%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static --with-udev-dir=%{_udevrulesdir}
make %{?_smp_mflags}

%install
%make_install

#Remove installed doc
rm -fr %{buildroot}/%{_datadir}/doc/%{name}

%files
%defattr(-, root, root)
%{_bindir}/%{name}events
%{_bindir}/%{name}edid
%{_bindir}/%{name}ddc
%{_bindir}/%{name}hextobin
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}ddc.1*
%{_mandir}/man1/%{name}edid.1*
%{_mandir}/man1/%{name}events.1*
%{_mandir}/man1/%{name}hextobin.1*
%{_udevrulesdir}/90-xcm-i2c.rules
%doc docs/AUTHORS docs/COPYING docs/ChangeLog README.md

%changelog
