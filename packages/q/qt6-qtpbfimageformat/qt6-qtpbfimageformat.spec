#
# spec file for package libqt5-qtpbfimageformat
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           qt6-qtpbfimageformat
Version:        3.1
Release:        1
Summary:        Qt6 PBF Image Format Plugin
License:        LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://github.com/tumic0/QtPBFImagePlugin
Source0:        https://github.com/tumic0/QtPBFImagePlugin/archive/%{version}/QtPBFImagePlugin-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pkgconfig.patch - fix for broken OpenSUSE linker
Patch0:         pkgconfig.patch

BuildRequires:  gcc-c++
BuildRequires:  make
%if 0%{?suse_version}
BuildRequires:  qt6-core-devel
BuildRequires:  qt6-gui-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
%else
%if 0%{?fedora_version}
BuildRequires:  qt6-qtbase
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-devel
BuildRequires:  zlib-devel
BuildRequires:  protobuf-lite-devel
%else
# Mageia
BuildRequires:  libqt6core-devel
BuildRequires:  libqt6gui-devel
%ifarch x86_64
BuildRequires:  lib64protobuf-devel
BuildRequires:  lib64zlib-devel
%else
BuildRequires:  libprotobuf-devel
BuildRequires:  libzlib-devel
%endif
%endif
%endif

%description
Qt image plugin for displaying Mapbox vector tiles.

%prep
%setup -q -n QtPBFImagePlugin-%{version}
%autopatch -p0

%build
%if 0%{?suse_version}
%{qmake6} pbfplugin.pro
%else
%{qmake_qt6} pbfplugin.pro
%endif
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
install -d 755 %{buildroot}/%{_datadir}/mime/packages
install -m 644 pkg/pbfplugin.xml %{buildroot}/%{_datadir}/mime/packages/%{name}.xml

%files
%if 0%{?suse_version}
%{_qt6_pluginsdir}/imageformats/libpbf.so
%else
%{_qt6_plugindir}/imageformats/libpbf.so
%endif
%{_datadir}/mime/packages/*

%changelog
