#
# spec file for package rfb
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


Name:           rfb
Version:        0.6.1
Release:        0
Summary:        heXoNet RFB (remote control for the X Window System)
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://www.hexonet.de/software/rfb/
#Original source: http://www.hexonet.de/download/rfb-0.6.1.tar.gz
Source0:        http://www.hexonet.de/download/rfb-0.6.1.tar.bz2
Patch0:         rfb-0.6.1-rpmoptflags.patch
Patch1:         rfb-0.6.1-gcc3.dif
Patch2:         rfb-0.6.1-socklen_t.dif
Patch3:         %{name}-%{version}-gcc4.3.diff
BuildRequires:  gcc-c++
BuildRequires:  xclass-devel
Requires:       xclass
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The heXoNet RFB Software package includes many different projects. The
goal of this package is to provide a comprehensive collection of
rfb-enabled tools and applications. One application, x0rfbserver, was,
and maybe still is, the only complete remote control solution for the X
Window System.

%prep
%setup0
%patch0 -p1
%patch1
%patch2
%patch3

%build
export CFLAGS="%{optflags} -Wall"
make %{?_smp_mflags} depend
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_mandir}/man1 %{buildroot}%{_prefix}/bin
install -m 644 man/man1/* %{buildroot}%{_mandir}/man1
install -m 755 x0rfbserver/x0rfbserver %{buildroot}%{_bindir}/
install -m 755 xrfbviewer/{xrfbviewer,xplayfbs} %{buildroot}%{_bindir}/
install -m 755 rfbcat/rfbcat %{buildroot}%{_bindir}/
install -m 755 xvncconnect/xvncconnect %{buildroot}%{_bindir}/

%files
%defattr(-, root, root)
%doc COPYING INSTALL README rfm_fbs.1.0.html
%doc %{_mandir}/man1/*.1*
%{_bindir}/*

%changelog
