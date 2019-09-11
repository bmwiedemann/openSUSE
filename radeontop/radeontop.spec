#
# spec file for package radeontop
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


Name:           radeontop
Version:        1.2
Release:        0
Summary:        View Radeon GPU utilization
License:        GPL-3.0-only
Group:          System/Monitoring
URL:            https://github.com/clbr/radeontop
Source0:        https://github.com/clbr/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        radeontop-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdrm) >= 2.4.63
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri2)
Recommends:     %{name}-lang = %{version}

%description
View Radeon GPU utilization, both for the total activity percent and individual
blocks.
Supported cards R600 and up, even Southern Islands should work fine. Works with
both the open drivers and AMD Catalyst.
The total GPU utilization is also valid for OpenCL loads; the other blocks are
only useful in GL loads.

%lang_package

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} debug=1 nostrip=1 amdgpu=1

%install
%make_install LIBDIR=%{_lib}
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_sbindir}/%{name}
%{_libdir}/lib%{name}_xcb.so
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
