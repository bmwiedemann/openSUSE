#
# spec file for package qt6-quickeffectmaker
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


%define real_version 6.7.2
%define short_version 6.7
%define tar_name qtquickeffectmaker-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-quickeffectmaker%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Tool for creating shader effects for Qt Quick
License:        GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source1:        org.qt.quickeffectmaker6.desktop
Source2:        org.qt.quickeffectmaker.png
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-quick-private-devel
BuildRequires:  qt6-shadertools-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
BuildRequires:  cmake(Qt6Quick) = %{real_version}
BuildRequires:  cmake(Qt6Quick3DGlslParserPrivate) = %{real_version}
BuildRequires:  cmake(Qt6ShaderTools) = %{real_version}

%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Quick Effect Maker is a hybrid editor for creating shader effects for Qt
Quick applications and offers both a node editor and a code editor.

%if !%{qt6_docs_flavor}

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

# Desktop file
%suse_update_desktop_file -i org.qt.quickeffectmaker6
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/org.qt.quickeffectmaker.png

%files
%license LICENSES/* tools/qqem/qml/fonts/SourceCodePro.txt
%{_bindir}/qqem6
%{_datadir}/applications/org.qt.quickeffectmaker6.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.qt.quickeffectmaker.png
%{_qt6_bindir}/qqem
%{_qt6_qmldir}/QtQuickEffectMaker/

%endif

%changelog
