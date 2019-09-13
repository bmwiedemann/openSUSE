#
# spec file for package asusfan
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


Name:           asusfan
Url:            http://www.consultmatt.co.uk/asusfan/
BuildRequires:  automake
BuildRequires:  pkgconfig(xproto)
Version:        0.1
Release:        0
Summary:        Fan Control for Nvidia-Based ASUS Graphics Cards
License:        GPL-2.0+
Group:          System/X11/Utilities
Source:         asusfan-0.1-nodocs.tar.bz2
Patch:          asusfan-0.1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64

%description
This command line tool allows you to control the speed of your graphics
card's fan, which usually runs at full speed under Linux. It has been
tested with V9999 and V9750TD models and may work with other cards as
well.

%prep
%setup -q
%patch -p1

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
/usr/bin/asusfan
%_libdir/libasus*

%changelog
