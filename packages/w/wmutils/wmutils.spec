#
# spec file for package wmutils
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           wmutils
Version:        1.4
Release:        0
Summary:        Set of tools for X windows manipulation
License:        ISC
Group:          System/X11/Utilities
URL:            https://github.com/wmutils/core
Source:         https://github.com/%{name}/core/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE wmutils-cflags.patch fixes spurious "compiled without $RPM_OPT_FLAGS" warning -- aloisio@gmx.com
Patch0:         wmutils-cflags.patch
# PATCH-FIX-OPENSUSE wmutils-conflict.patch fixes conflict with wtf from bsd-games -- aloisio@gmx.com
Patch1:         wmutils-conflict.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)

%description
wmutils's core is a set of tools for manipulating X11 windows.
Each tool only has one purpose.

%prep
%setup -q -n core-%{version}
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags}

%install
%make_install \
  PREFIX=%{_prefix}    \
  MANPREFIX=%{_mandir}

%files
%license LICENSE
%doc README.md
%{_bindir}/chwb
%{_bindir}/chwso
%{_bindir}/ignw
%{_bindir}/killw
%{_bindir}/lsw
%{_bindir}/mapw
%{_bindir}/pfw
%{_bindir}/wattr
%{_bindir}/wmp
%{_bindir}/wmv
%{_bindir}/wm_wtf
%{_bindir}/wrs
%{_bindir}/wtp
%{_mandir}/man1/chwb.1%{ext_man}
%{_mandir}/man1/chwso.1%{ext_man}
%{_mandir}/man1/ignw.1%{ext_man}
%{_mandir}/man1/killw.1%{ext_man}
%{_mandir}/man1/lsw.1%{ext_man}
%{_mandir}/man1/mapw.1%{ext_man}
%{_mandir}/man1/pfw.1%{ext_man}
%{_mandir}/man1/wattr.1%{ext_man}
%{_mandir}/man1/wmp.1%{ext_man}
%{_mandir}/man1/wmutils.1%{ext_man}
%{_mandir}/man1/wmv.1%{ext_man}
%{_mandir}/man1/wm_wtf.1%{ext_man}
%{_mandir}/man1/wrs.1%{ext_man}
%{_mandir}/man1/wtp.1%{ext_man}

%changelog
