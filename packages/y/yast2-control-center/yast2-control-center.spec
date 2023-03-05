#
# spec file for package yast2-control-center
#
# Copyright (c) 2023 SUSE LLC
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


Name:           yast2-control-center
Version:        4.6.0
Release:        0
URL:            https://github.com/yast/yast-control-center
Summary:        YaST2 - Control Center
License:        GPL-2.0-only
Group:          System/YaST

Source0:        yast2-control-center-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
%if 0%{?force_gcc_46}
BuildRequires:  gcc46
BuildRequires:  gcc46-c++
%else
BuildRequires:  gcc-c++ >= 4.6
%endif

Requires:       yast2
Requires:       yast2-control-center-binary

# control-center-gnome is dropped and this one should be used instead
Obsoletes:      yast2-control-center-gnome < %{version}
Provides:       yast2-control-center-gnome = %{version}

%description
This package contains the menu selection component for YaST2.

%package qt
Summary:        YaST2 - Control Center (Qt Version)
Group:          System/YaST

Requires:       libyui-qt
Requires:       yast2-control-center
# bsc#1130700: Need Qt SVG support for icons
Requires:       libQt5Svg5

Provides:       yast2-control-center-binary
Provides:       yast2-control-center:%{_prefix}/lib/YaST2/bin/y2controlcenter

Supplements:    (yast2 and plasma5-session)

%description qt
This package contains the menu selection component for YaST2 using the
Qt toolkit.

%prep
%setup -q

%build
mkdir build
cd build
%if 0%{?force_gcc_46}
export CC=gcc-4.6
export CXX=g++-4.6
%endif

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DLIB=%{_lib} \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make %{?jobs:-j %jobs} VERBOSE=1

%install
cd build
make install DESTDIR=%{buildroot}
cd ..

%suse_update_desktop_file -G "Administrator Settings"  %{buildroot}%{_datadir}/applications/org.opensuse.YaST.desktop Core-System X-SuSE-ControlCenter-System X-GNOME-SystemSettings
%suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/YaST-systemsettings.desktop

%files
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.opensuse.YaST.appdata.xml
%{_datadir}/applications/org.opensuse.YaST.desktop
%dir %{_datadir}/kde4/
%dir %{_datadir}/kde4/services
%{_datadir}/kde4/services/YaST-systemsettings.desktop
%dir %{_datadir}/kservices5
%{_datadir}/kservices5/YaST-systemsettings.desktop
%{yast_icondir}

%files qt
%{_prefix}/lib/YaST2/bin/y2controlcenter
%license COPYING.GPL2

%changelog
