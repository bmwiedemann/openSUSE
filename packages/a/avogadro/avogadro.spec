#
# spec file for package avogadro
#
# Copyright (c) 2025 SUSE LLC
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


%define src_name avogadroapp-%{version}
%define i18n_rev 1.98.0

%if 0%{?suse_version} < 1600
# Requires gcc-c++ with <filesystem> support
%define gcc_ver 8
%endif

# Disable: Tests require paraview QtTesting, unavailable for openSUSE [as of 2025-05-12]
%bcond_with tests
Name:           avogadro
Version:        1.100.0
Release:        0
Summary:        A Molecular design tool
License:        GPL-2.0-only
Group:          Productivity/Scientific/Chemistry
URL:            https://two.avogadro.cc/
Source0:        https://github.com/OpenChemistry/avogadroapp/archive/refs/tags/%{version}.tar.gz#/%{src_name}.tar.gz
Source1:        https://github.com/OpenChemistry/avogadro-i18n/archive/refs/tags/%{i18n_rev}.tar.gz#/avogadro-i18n-%{i18n_rev}.tar.gz
# Needed for testing
# Source2:        https://github.com/OpenChemistry/avogadrodata/archive/refs/tags/%%{version}.tar.gz#/avogadrodata-%%{version}.tar.gz
BuildRequires:  cmake >= 3.24
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(AvogadroLibs) >= 1.100.0
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(eigen3)
%if %{with tests}
BuildRequires:  xvfb-run
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6Test)
%endif

%lang_package

%description
Avogadro is an advanced molecular editor designed
for cross-platform use in computational chemistry,
molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and
a powerful plugin architecture.

%prep
%setup -qn %{src_name} -b 1 %{?with_tests:-b 2}
ln -s avogadro-i18n-%{i18n_rev} ../avogadro-i18n
%if %{with tests}
ln -s avogadrodata-%{version} ../avogadrodata
%endif

%build
# Note: Avogadro_ENABLE_RPC requires Molequeue, which is abandonware; see https://github.com/OpenChemistry/avogadroapp/issues/561
%cmake \
  -DCMAKE_CXX_COMPILER:STRING=g++%{?gcc_ver:-%{gcc_ver}} \
  -DAvogadro_ENABLE_RPC=OFF \
  -DENABLE_TESTING:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DQT_VERSION=6 \
  %{nil}
%cmake_build

%install
%cmake_install
# remove docs insyalled by cmake - we package them as %%doc directly
rm -rf %{buildroot}%{_docdir}/%{name}
rm -rfv %{buildroot}%{_datadir}/doc/AvogadroApp
%fdupes %{buildroot}%{_datadir}

%if %{with tests}
%check
cd %__builddir
xvfb-run --server-args="-screen 0 1920x1080x24" -a \
ctest --output-on-failure --force-new-ctest-process
cd ..
%endif

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/avogadro2
%dir %{_datadir}/avogadro2
%dir %{_datadir}/avogadro2/i18n
%if 0%{?suse_version} < 1600
%dir %{_datadir}/icons/hicolor/16x16@2
%dir %{_datadir}/icons/hicolor/16x16@2/apps
%dir %{_datadir}/icons/hicolor/32x32@2
%dir %{_datadir}/icons/hicolor/32x32@2/apps
%endif
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml

%files lang
%{_datadir}/avogadro2/i18n/*

%changelog
