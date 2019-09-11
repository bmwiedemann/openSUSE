#
# spec file for package suil
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


%define _description \
Suil is a lightweight C library for loading and wrapping LV2 plugin UIs.\
\
Suil makes it possible to load a UI of any toolkit in a host using any\
other toolkit (assuming the toolkits are both supported by Suil).\
Hosts do not need to build against or link to foreign toolkit libraries\
to use UIs written with that toolkit (Suil performs its magic at\
runtime using dynamically loaded modules). The API is designed such that\
hosts do not need to explicitly support particular toolkits whatsoever.\
If Suil supports a particular toolkit, then all hosts that use Suil will\
support that toolkit.

Name:           suil
Version:        0.10.2
Release:        0
Summary:        Lightweight C library for loading and wrapping LV2 plugin UIs
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://drobilla.net/software/suil/
Source:         https://download.drobilla.net/suil-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM suil-wrong-cocoa-detection.patch
Patch0:         suil-wrong-cocoa-detection.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel >= 3.14.0
BuildRequires:  lv2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-rdflib
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1.0

%description
%{_description}

%package     -n libsuil-0-0
Summary:        Lightweight C library for loading and wrapping LV2 plugin UIs
Group:          System/Libraries

%description -n libsuil-0-0
%{_description}

%package        devel
Summary:        Development files for the suil library
Group:          Development/Libraries/C and C++
Requires:       libsuil-0-0 = %{version}
Requires:       pkgconfig

%description    devel
Development files needed to build applications against suil library.

%package     -n suil-plugin-gtk2-in-qt5
Summary:        Shared object for GTK2 hosts displaying Qt5 LV2 GUIs
Group:          System/Libraries
Requires:       gtk2-tools
Requires:       libsuil-0-0 = %{version}
Supplements:    packageand(gtk2:lv2)

%description -n suil-plugin-gtk2-in-qt5
Module plugin for:
* GTK2 hosts displaying Qt5 LV2 GUIs using suil

%package     -n suil-plugin-qt5-in-gtk2
Summary:        Shared object for Qt5 hosts displaying GTK2 LV2 GUIs
Group:          System/Libraries
Requires:       libsuil-0-0 = %{version}
Requires:       python-qt5
Supplements:    packageand(libQt5Widgets5:lv2)

%description -n suil-plugin-qt5-in-gtk2
Module plugin for:
* Qt5 hosts displaying GTK2 LV2 GUIs using suil

%package     -n suil-plugin-x11
Summary:        Shared object for X11 LV2 GUIs
Group:          System/Libraries
Requires:       libsuil-0-0 = %{version}
Supplements:    packageand(libX116:lv2)

%description -n suil-plugin-x11
Module plugin for:
* X11 LV2 GUIs using suil

%package     -n suil-plugin-x11-in-gtk2
Summary:        Shared object for GTK2 hosts displaying X11 LV2 GUIs
Group:          System/Libraries
Requires:       gtk2-tools
Requires:       libsuil-0-0 = %{version}
Supplements:    packageand(gtk2:lv2)
Obsoletes:      libsuil-x11-in-gtk2 < %{version}
Provides:       libsuil-x11-in-gtk2 = %{version}

%description -n suil-plugin-x11-in-gtk2
Module plugin for:
* GTK2 hosts displaying X11 LV2 GUIs using suil

%package     -n suil-plugin-x11-in-gtk3
Summary:        Shared object for GTK3 hosts displaying X11 LV2 GUIs
Group:          System/Libraries
Requires:       gtk3-tools
Requires:       libsuil-0-0 = %{version}
Supplements:    packageand(gtk3:lv2)

%description -n suil-plugin-x11-in-gtk3
Module plugin for:
* GTK3 hosts displaying X11 LV2 GUIs using suil

%package     -n suil-plugin-x11-in-qt5
Summary:        Shared object for Qt5 hosts displaying X11 LV2 GUIs
Group:          System/Libraries
Requires:       libsuil-0-0 = %{version}
Requires:       python-qt5
Supplements:    packageand(libQt5Widgets5:lv2)

%description -n suil-plugin-x11-in-qt5
Module plugin for:
* Qt5 hosts displaying x11 LV2 GUIs using suil

%prep
%setup -q
%patch0 -p1
# run waf with python 3
find waflib -type f -name *.py -exec sed -i 's|/usr/bin/env python|%{_bindir}/python3|' {} \;
sed -i 's|/usr/bin/env python|%{_bindir}/python3|' wscript waf waflib/waf

%build
./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf

%install
./waf install --destdir=%{buildroot}

%post -n libsuil-0-0 -p /sbin/ldconfig
%postun -n libsuil-0-0 -p /sbin/ldconfig

%files devel
%license COPYING
%doc README.md
%dir %{_includedir}/suil-0/
%dir %{_includedir}/suil-0/suil
%{_libdir}/libsuil-0.so
%{_includedir}/suil-0/suil/*.h
%{_libdir}/pkgconfig/suil-0.pc

%files -n libsuil-0-0
%license COPYING
%doc README.md
%dir %{_libdir}/suil-0
%{_libdir}/libsuil-0.so.*

%files -n suil-plugin-gtk2-in-qt5
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_gtk2_in_qt5.so

%files -n suil-plugin-qt5-in-gtk2
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_qt5_in_gtk2.so

%files -n suil-plugin-x11
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_x11.so

%files -n suil-plugin-x11-in-gtk2
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_x11_in_gtk2.so

%files -n suil-plugin-x11-in-gtk3
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_x11_in_gtk3.so

%files -n suil-plugin-x11-in-qt5
%license COPYING
%doc README.md
%{_libdir}/suil-0/libsuil_x11_in_qt5.so

%changelog
