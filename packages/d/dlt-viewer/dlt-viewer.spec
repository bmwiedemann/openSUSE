#
# spec file for package dlt-viewer
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


Name:           dlt-viewer
Version:        2.23.0
Release:        0
Summary:        Diagnostic Log and Trace viewing program
License:        MPL-2.0
Group:          Development/Tools/Other
URL:            https://github.com/COVESA/dlt-viewer
Source:         https://github.com/COVESA/dlt-viewer/archive/refs/tags/v%{version}.tar.gz
Patch1:         change-additional-files-installation-path.patch
Patch2:         do-not-install-docs.patch
Patch3:         do-not-install-some-resources.patch
Patch4:         force-pie.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.1
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Widgets)
Provides:       dlt-viewer = %{version}

%description
The Diagnostic Log and Trace Viewer is an application that can send and receive control messages to the DLT daemon.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DDLT_PARSER=OFF \
       -DDLT_APP_DIR_NAME=dlt-viewer \
       -DDLT_LIBRARY_INSTALLATION_PATH="%{_libdir}" \
       -DDLT_EXECUTABLE_INSTALLATION_PATH="%{_bindir}" \
       -DDLT_RESOURCE_INSTALLATION_PATH="%{_datadir}" \
       -DDLT_PLUGIN_INSTALLATION_PATH="%{_libdir}/dlt-viewer/plugins"

%cmake_build

%install
%cmake_install

# remove sdk for now, needs subpackage
rm -rf %{buildroot}%{_prefix}/sdk/

%suse_update_desktop_file org.genivi.DLTViewer

%files
%doc README.md ReleaseNotes_Viewer.txt doc/dlt_viewer_user_manual.pdf
%license LICENSE.txt MPL.txt
%{_datadir}/dlt-viewer
%{_datadir}/applications/org.genivi.DLTViewer.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/org.genivi.DLTViewer.png
%dir %{_libdir}/dlt-viewer/
%{_libdir}/dlt-viewer/plugins
%{_libdir}/libqdlt.so
%{_bindir}/dlt-viewer

%changelog
