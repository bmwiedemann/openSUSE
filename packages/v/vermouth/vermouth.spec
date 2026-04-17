#
# spec file for package vermouth
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           vermouth
Version:        1.3.1
Release:        0
Summary:        A Wine/Proton game launcher for KDE
License:        MIT
URL:            https://github.com/dekomote/vermouth
Group:          System/Emulators/PC

# Get the source from tar_scm
Source0:        %{name}-%{version}.tar.xz

# Exclusions file
Source1:        %{name}.rpmlintrc

# BuildDeps
BuildRequires:  gcc-c++
BuildRequires:  AppStream
BuildRequires:  cmake >= 3.20
BuildRequires:  extra-cmake-modules >= 6.0.0
BuildRequires:  fdupes
BuildRequires:  cmake(KF6CoreAddons) >= 6.0.0
BuildRequires:  cmake(KF6I18n) >= 6.0.0
BuildRequires:  cmake(KF6Kirigami) >= 6.0.0
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= 6.0.0
BuildRequires:  cmake(Qt6Core) >= 6.6.0
BuildRequires:  cmake(Qt6DBus) >= 6.6.0
BuildRequires:  cmake(Qt6Gui) >= 6.6.0
BuildRequires:  cmake(Qt6Network) >= 6.6.0
BuildRequires:  cmake(Qt6Quick) >= 6.6.0
BuildRequires:  cmake(Qt6QuickControls2) >= 6.6.0
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0

# Runtime deps
Requires:       kf6-qqc2-desktop-style

# Only install gaming selinux policy on SLE +16 / Leap +16 / Tumbleweed / Slowroll
%if 0%{?suse_version} >= 1600 || 0%{?is_opensuse}
Requires:       (selinux-policy-targeted-gaming if selinux-policy-targeted)
%endif

# Recommended software
Recommends:     ca-certificates-steamtricks
Recommends:     gamemode%{?_isa}
Recommends:     gamescope
Recommends:     icoutils
Recommends:     libvkd3d-utils1%{?_isa}
Recommends:     libvkd3d1%{?_isa}
Recommends:     mangohud%{?_isa}
Recommends:     ntsync-autoload
Recommends:     ntsync-autoload-udev-rules

Obsoletes:      %{name} < %{version}

%description
Vermouth is a lightweight game and application launcher for
running Windows executables through Proton or Wine on KDE.
It works like Lutris, Heroic, Faugus or Bottles, but is KDE first
(written in Qt/QML and using Kirigami).

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove duplicated files
%fdupes %{buildroot}%{_datadir}

%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/*.xml

%files
%license LICENSE

# Binaries
%{_bindir}/vermouth

# .desktop files
%{_datadir}/applications/com.dekomote.vermouth.desktop

# icons
%{_datadir}/icons/hicolor/scalable/apps/com.dekomote.vermouth.svg

# Application data
%{_datadir}/metainfo/com.dekomote.vermouth.metainfo.xml

%changelog
