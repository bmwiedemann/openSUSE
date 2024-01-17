#
# spec file for package XyGrib
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018-2022 Dr. Axel Braun <DocB@opensuse.org>
# Copyright (c) 2018 Dominig ar Foll (Intel Open Source)
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


Name:           XyGrib
Version:        1.2.6.1
Release:        0
Summary:        A weather visualization package
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://opengribs.org/en/
Source0:        https://github.com/opengribs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         QPainter.patch
Patch1:         libjpeg24.diff
Patch2:         proj8.diff
Patch3:         projection.diff
Patch4:         proj9.diff
BuildRequires:  cmake
BuildRequires:  libnova-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} < 1500
Requires(post): update-desktop-files
Requires(postun):update-desktop-files
%endif

%description
XyGrib is a weather visualization package that interacts with
OpenGribs's Grib server providing a choice of global and large area
atmospheric and wave models.

XyGrib also uses pre-cut Gribs of high-resolution regional models
found on OpenSkiron.org.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{S:1} %{S:2} .

#check for Leap version = 15.4
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
%patch2 -p1
%else
%patch4 -p1
%endif
%patch3 -p1

%build
# -DNO_UPDATE=1 deactivates XyGrib internal SW update
# -DOPENSUSE=1  macro for optional openSUSE friendly options in the source code
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_datadir}/openGribs \
	-DCMAKE_CXX_FLAGS="%{optflags} -DNO_UPDATE=1 -DOPENSUSE=1"
%cmake_build

%install
%cmake_install

# xygrib Makefile install is not very Linux
mkdir %{buildroot}/%{_bindir}
mv %{buildroot}/%{_datadir}/openGribs/XyGrib/XyGrib %{buildroot}/%{_bindir}/XyGrib

# Uses handmade xygrib.desktop file from OSB
%suse_update_desktop_file -i %{name}

# Starting with openSUSE 15.0 this is automatic
%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc README.md
%license LICENSE
%dir %attr(0755, root, root) %{_datadir}/openGribs
%{_bindir}/%{name}
%{_datadir}/openGribs/%{name}
%{_datadir}/applications/XyGrib.desktop
%{_datadir}/pixmaps/XyGrib.png

%changelog
