#
# spec file for package deadbeef-plugin-mpris2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Hillwood Yang <hillwood@opensuse.org>
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


%define _name   deadbeef-mpris2-plugin
Name:           deadbeef-plugin-mpris2
Version:        1.12
Release:        0
Summary:        MPRISv2 plugin for the DeaDBeeF music player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
Url:            https://github.com/Serranya/deadbeef-mpris2-plugin
Source:         https://github.com/Serranya/%{_name}/releases/download/v%{version}/%{_name}-%{version}.tar.xz
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  deadbeef-devel >= 0.6.2
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
Requires:       deadbeef >= 0.6.2
Obsoletes:      %{_name} <= %{version}
Provides:       %{_name} = %{version}
Provides:       deadbeef-MPRIS-plugin = %{version}
Obsoletes:      deadbeef-MPRIS-plugin < %{version}

%description
This plugin aims to implement the MPRISv2 D-Bus interface for
DeaDBeeF for instance to integrate DeaDBeeF into Sound Menu.

%prep
%setup -q -n deadbeef-%{version}

%build
autoreconf -fi
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root)
%{_libdir}/deadbeef/

%changelog
