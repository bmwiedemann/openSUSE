#
# spec file for package stl-thumb-kde
#
# Copyright (c) 2024 SUSE LLC
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


Name:           stl-thumb-kde
Version:        0.5.0
Release:        0
Summary:        Stl-thumb is a fast lightweight thumbnail generator for STL files.
License:        MIT
URL:            https://github.com/unlimitedbacon/stl-thumb-kde
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         cmake.patch
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-filesystem
BuildRequires:  stl-thumb-devel
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)

%description
This is the KDE / KIO plugin for stl-thumb.
It shows previews of .stl files in Dolphin and throughout the KDE desktop.

%prep
%autosetup -p1

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

%files
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/stlthumbnail.so

%changelog
