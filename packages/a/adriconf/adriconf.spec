#
# spec file for package adriconf
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


Name:           adriconf
Version:        2.7.4
Release:        0
Summary:        Advanced DRI Configurator
License:        GPL-3.0-only
URL:            https://gitlab.freedesktop.org/mesa/adriconf
# NOTE: upstream tagged this release "v.2.7.4" (with a stray dot after v),
# unlike the plain "v2.7.x" used before, hence the "v." in the paths below.
Source0:        https://gitlab.freedesktop.org/mesa/adriconf/-/archive/v.%{version}/adriconf-v.%{version}.tar.bz2
Source1:        adriconf.desktop
Source2:        driconf-icon.png
# PATCH-FIX-OPENSUSE adriconf-system-gtest.patch mpluskal@suse.com -- build unit tests against the system GTest/GMock instead of downloading googletest at build time
Patch0:         adriconf-system-gtest.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel >= 1.60
BuildRequires:  libboost_locale-devel >= 1.60
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atkmm-2.36)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pugixml)

%description
adriconf (Advanced DRI CONFigurator) is a GUI tool used to configure open
source graphics drivers. It works by setting options and writing them to
the standard drirc file used by the Mesa drivers.

%lang_package

%prep
%autosetup -p1 -n %{name}-v.%{version}

%build
%cmake \
	-DENABLE_UNIT_TESTS=ON
%cmake_build

%install
%cmake_install
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{SOURCE2} \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%find_lang %{name}

%check
%ctest

%files
%license LICENSE
%{_bindir}/adriconf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
