#
# spec file for package util-macros
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


Name:           util-macros
Version:        1.20.0
Release:        0
Summary:        The X Protocol
#Source URL:    http://xorg.freedesktop.org/releases/individual/util/
#BuildRequires:  autoconf >= 2.60
#BuildRequires:  automake
#BuildRequires:  libtool
License:        HPND
Group:          Development/Libraries/X11
URL:            https://xorg.freedesktop.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig

%description
Utility Macro Headers for X development

%package -n %{name}-devel
Summary:        The X Protocol
# Added within the 13.2 Development Cycle
Group:          Development/Libraries/X11
Provides:       xorg-x11-proto-devel:/%{_libdir}/pkgconfig/xorg-macros.pc

%description -n %{name}-devel
Utility Macro Headers for X development

%prep
%setup -q

%build
#autoreconf -fi
./configure CFLAGS="%{optflags} -fno-strict-aliasing" \
              --prefix=%{_prefix} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_datadir}/util-macros/INSTALL

%files -n %{name}-devel
%license COPYING
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4
%{_datadir}/pkgconfig/*.pc

%changelog
