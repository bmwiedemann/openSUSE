#
# spec file for package adriconf
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.6.1
Release:        0
Summary:        Advanced DRI Configurator
License:        GPL-3.0-only
Group:          System/Packages
URL:            https://github.com/jlHertel/adriconf
Source0:        https://github.com/jlHertel/adriconf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        adriconf.desktop
Source2:        driconf-icon.png
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-obj-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libxml++-3.0)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)

%description
adriconf (Advanced DRI CONFigurator) is a GUI tool used to configure open
source graphics drivers. It works by setting options and writing them to
the standard drirc file used by the Mesa drivers.

%lang_package

%prep
%setup -q

%build
%cmake \
	-DENABLE_UNIT_TESTS=OFF
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/%{_datadir}/{applications,pixmaps}
install -D -m0755 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m0755 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files
%license LICENSE
%{_bindir}/adriconf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
