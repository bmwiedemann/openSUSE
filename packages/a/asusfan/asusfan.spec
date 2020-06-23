#
# spec file for package asusfan
#
# Copyright (c) 2020 SUSE LLC
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


Name:           asusfan
Version:        0.1
Release:        0
Summary:        Fan Control for Nvidia-Based ASUS Graphics Cards
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://www.consultmatt.co.uk/asusfan/
Source:         asusfan-0.1-nodocs.tar.bz2
Patch0:         asusfan-0.1.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xproto)
ExclusiveArch:  %{ix86} x86_64

%description
This command line tool allows you to control the speed of your graphics
card's fan, which usually runs at full speed under Linux. It has been
tested with V9999 and V9750TD models and may work with other cards as
well.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags} -fcommon"
%configure \
  --disable-static \
  --with-pic
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README
%{_bindir}/asusfan
%{_libdir}/libasus*

%changelog
