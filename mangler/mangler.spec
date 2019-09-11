#
# spec file for package mangler
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mangler
Version:        1.2.5
Release:        0
Summary:        Ventrilo Compatible Client for Linux
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Talk/Clients
Url:            http://www.mangler.org/
Source:         http://www.mangler.org/downloads/%{name}-%{version}.tar.bz2
BuildRequires:  alsa-devel
BuildRequires:  dbus-1-glib-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  espeak-ng-compat-devel
%else
BuildRequires:  espeak-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  gtkmm2-devel
BuildRequires:  libgsm-devel
BuildRequires:  libpulse-devel
BuildRequires:  speex-devel
BuildRequires:  update-desktop-files
BuildRequires:  xosd-devel
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig(opus) >= 0.9.11
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mangler is an open source VOIP client capable of connecting to
Ventrilo 3.x servers. It is capable of performing almost all standard
user functionality found in a Windows Ventrilo client.

%package -n libventrilo3-0
Summary:        Networking library for communicating with Ventrilo servers
Group:          System/Libraries

%description -n libventrilo3-0
Libventrilo3 is a networking library for communicating with Ventrilo
servers. It performs audio encoding/decoding, signal processing and
network communications.

%package -n libventrilo3-devel
Summary:        Networking library for communicating with Ventrilo servers -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libventrilo3-0 = %{version}

%description -n libventrilo3-devel
Libventrilo3 is a networking library for communicating with Ventrilo
servers. It performs audio encoding/decoding, signal processing and
network communications.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
%suse_update_desktop_file %{name} Telephony

%clean
rm -rf %{buildroot}

%post -n libventrilo3-0 -p /sbin/ldconfig

%postun -n libventrilo3-0 -p /sbin/ldconfig

%files
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.zlib
%{_bindir}/mangler
%{_datadir}/applications/mangler.desktop
%{_datadir}/pixmaps/mangler_logo.svg
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libventrilo3-0
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.LGPL
%{_libdir}/libventrilo3.so.*

%files -n libventrilo3-devel
%defattr (-,root,root)
%{_includedir}/ventrilo3.h
%{_libdir}/libventrilo3.so

%changelog
