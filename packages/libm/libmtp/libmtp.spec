#
# spec file for package libmtp
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


%define sonum   9
%{!?_udevrulesdir: %global _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d }
%{!?_udevdir: %global _udevdir %(pkg-config --variable=udevdir udev) }
Name:           libmtp
Version:        1.1.18
Release:        0
Summary:        Commandline utilities for access to MTP Players
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://sf.net/projects/libmtp
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  doxygen
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
This package contains binaries and documentation that allow access to
USB based media players based on the MTP (Media Transfer Protocol)
authored by Microsoft.

Common devices using this technology are Creative Zen, iRiver, Samsung
and others.

%package     -n %{name}-udev
Summary:        Udev rules for accessing MTP devices
Group:          Hardware/Mobile
Requires:       pkgconfig(udev)

%description -n %{name}-udev
This package contains the udev rules that allow access to USB based media
players based on the MTP (Media Transfer Protocol) authored by
Microsoft.

%package    -n %{name}%{sonum}
Summary:        Library for accessing MTP Players
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name}-udev >= %{version}

%description -n %{name}%{sonum}
This package contains the libraries that allow access to USB based media
players based on the MTP (Media Transfer Protocol) authored by
Microsoft.

Common devices using this technology are Creative Zen, iRiver, Samsung
and others.

%package -n mtp-tools
Summary:        Commandline utilities for access to MTP Players
Group:          Productivity/Multimedia/Sound/Players

%description -n mtp-tools
This package contains binaries that allow command line access to USB
based media players based on the MTP (Media Transfer Protocol) authored
by Microsoft. For graphical user interfaces use Amarok or Banshee.

%package devel
Summary:        Development files for access to MTP Player library
Group:          Development/Libraries/Other
Requires:       %{name}%{sonum} = %{version}

%description devel
This package contains the development headers for the libmtp library
that allows access to USB based media players based on the MTP (Media
Transfer Protocol) authored by Microsoft.

%prep
%setup -q

%build
echo 'HTML_TIMESTAMP=NO' >> doc/Doxyfile.in
%configure --with-udev=%{_udevdir} --disable-static --enable-doxygen
make %{?_smp_mflags}

%install
%make_install
#install -d $RPM_BUILD_ROOT/usr/share/hal/fdi/information/20thirdparty/
#install -c -m 644 libmtp.fdi $RPM_BUILD_ROOT/usr/share/hal/fdi/information/20thirdparty/10-usb-music-players-libmtp.fdi
rm -rf %{buildroot}%{_datadir}/doc/libmtp*
find %{buildroot} -type f -name "*.la" -delete -print

%post -n   %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig

%files -n mtp-tools
%{_bindir}/*

%files -n %{name}%{sonum}
%license COPYING
%doc README ChangeLog AUTHORS
%{_libdir}/lib*.so.*

%files -n %{name}-udev
%{_udevdir}
%{_udevrulesdir}

%files devel
%doc doc/html TODO
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libmtp.pc
%{_includedir}/libmtp.h

%changelog
