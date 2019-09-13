#
# spec file for package xli
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xli
Version:        1.17+git20170726.0bb4fb4
Release:        0
Summary:        X11 Image Loading Utility
License:        MIT
Group:          System/X11/Utilities
Url:            https://github.com/openSUSE/xli
Source:         %{name}-%{version}.tar.xz
BuildRequires:  imake
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Provides:       xli115
Provides:       xloadimage = %{version}

%description
xli is a version of xloadimage.

This utility will view several types of images under X11, or load
images onto the X11 root window.

%prep
%setup -q

%build
xmkmf -a
make %{?_smp_mflags} all CCOPTIONS="%{optflags}"

%install
%make_install install.man
ln -s xli %{buildroot}%{_bindir}/xloadimage
ln -s xli.1x %{buildroot}%{_mandir}/man1/xloadimage.1x

%files
%doc README* ABOUTGAMMA LICENSE
%{_mandir}/man1/xli.1x%{ext_man}
%{_mandir}/man1/xlito.1x%{ext_man}
%{_mandir}/man1/xloadimage.1x%{ext_man}
%{_bindir}/xli
%{_bindir}/xlito
%{_bindir}/xloadimage
%{_bindir}/xsetbg
%{_bindir}/xview
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xli

%changelog
