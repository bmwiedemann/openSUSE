#
# spec file for package qolibri
#
# Copyright (c) 2021 SUSE LLC
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


Name:           qolibri
Version:        2.1.4
Release:        0
Group:          Productivity/Office/Dictionary
Summary:        EPWING Dictionary Viewer
License:        GPL-2.0-or-later
URL:            https://github.com/ludios/qolibri
Source:         https://github.com/ludios/qolibri/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  eb-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  update-desktop-files

%description
qolibri is a dictionary viewer for the proprietary EPWING dictionary format
(originally developed for electronic pocket dictionaries). Most monolingual
Japanese dictionaries can only be found in the EPWING format.

%prep
%setup -q

%build
%cmake

%install
%cmake_install

install -D -m0644 qolibri.desktop %{_buildroot}%{_datadir}/applications/qolibri.desktop
%suse_update_desktop_file -i -r -G "Dictionary" qolibri Utility Office Dictionary Qt

%files
%license License.txt
%{_bindir}/qolibri
%{_datadir}/applications/qolibri.desktop

%changelog
