#
# spec file for package rfb
#
# Copyright (c) 2021 SUSE LLC
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


Name:           rfb
Version:        0.6.1
Release:        0
Summary:        heXoNet RFB (remote control for the X Window System)
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
Source0:        rfb-0.6.1.tar.bz2
Patch0:         rfb-0.6.1-rpmoptflags.patch
Patch1:         rfb-0.6.1-gcc3.dif
Patch2:         rfb-0.6.1-socklen_t.dif
Patch3:         %{name}-%{version}-gcc4.3.diff
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xclass-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
Requires:       xclass

%description
The heXoNet RFB Software package includes many different projects. The
goal of this package is to provide a comprehensive collection of
rfb-enabled tools and applications. One application, x0rfbserver, was,
and maybe still is, the only complete remote control solution for the X
Window System.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wall"
%make_build depend
%make_build

%install
mkdir -p %{buildroot}%{_mandir}/man1 %{buildroot}%{_bindir}
install -m 644 man/man1/* %{buildroot}%{_mandir}/man1
install -m 755 x0rfbserver/x0rfbserver %{buildroot}%{_bindir}/
install -m 755 xrfbviewer/{xrfbviewer,xplayfbs} %{buildroot}%{_bindir}/
install -m 755 rfbcat/rfbcat %{buildroot}%{_bindir}/
install -m 755 xvncconnect/xvncconnect %{buildroot}%{_bindir}/

%files
%license COPYING
%doc README rfm_fbs.1.0.html
%{_bindir}/rfbcat
%{_bindir}/x0rfbserver
%{_bindir}/xplayfbs
%{_bindir}/xrfbviewer
%{_bindir}/xvncconnect
%{_mandir}/man1/x0rfbserver.1%{?ext_man}
%{_mandir}/man1/xplayfbs.1%{?ext_man}
%{_mandir}/man1/xrfbviewer.1%{?ext_man}

%changelog
