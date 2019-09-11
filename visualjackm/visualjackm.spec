#
# spec file for package visualjackm
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           visualjackm
Version:        0.0+20120307
Release:        0
Summary:        Connects ProjectM Visualization with Jack
License:        GPL-2.0-or-later
Group:          System/Sound Daemons
Url:            https://bitbucket.org/asiniscalchi/visualjackm
Source0:        visualjackm-20120307.tar.bz2
Source1:        visualjackm.png
# PATCH-FIX-OPENSUSE visualjackm-projectM-qt5.patch -- build with Qt5
Patch0:         visualjackm-projectM-qt5.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libqjack-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libprojectM-qt-qt5)
BuildRequires:  pkgconfig(libprojectM-qt5)
Requires:       jack
Requires:       projectM-qt5-data

%description
This application lets you connect projectM visualization to jack.

%prep
%setup -q -n visualjackm
%patch0 -p1

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
make %{?_smp_mflags}

%install
install -D -m0755 build/visualjackm \
    %{buildroot}%{_bindir}/%{name}
install -D -m0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

%suse_update_desktop_file -c "%{name}" "%{name}" "Connect Jack to ProjectM" %{name} %{name} AudioVideo Midi

%files
%defattr(-,root,root)
%doc README
%{_bindir}/visualjackm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
