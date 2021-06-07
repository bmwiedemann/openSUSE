#
# spec file for package radare2-iaito
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without graphviz
%bcond_without python_bindings
%bcond_without syntax_highlighting

%define ts_version 5.2.1

Name:           radare2-iaito
Version:        5.2.2
Release:        0
Summary:        A Qt GUI for radare2 reverse engineering framework
License:        GPL-3.0-only
Group:          Development/Tools/Debuggers
URL:            https://github.com/radareorg/iaito
Source0:        https://github.com/radareorg/iaito/archive/refs/tags/%{version}.tar.gz#/radare2-iaito-%{version}.tar.gz
Source1:        https://github.com/radareorg/iaito-translations/archive/refs/tags/%{ts_version}.tar.gz#/radare2-iaito-translations-%{ts_version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  radare2-devel >= 5.2
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
%if %{with graphviz}
BuildRequires:  pkgconfig(libgvc)
%endif
%if %{with python_bindings}
BuildRequires:  cmake(PySide2)
BuildRequires:  cmake(Qt5Qml)
%endif
%if %{with syntax_highlighting}
BuildRequires:  cmake(KF5SyntaxHighlighting)
%endif
Requires:       radare2
# After the rizin fork, cutter was renamed back to iaito
Provides:       radare2-cutter
Obsoletes:      radare2-cutter <= 5.0

%description
A Qt and C++ GUI for radare2 reverse engineering framework.

%package devel
Summary:        Development files for Iaito
Group:          Development/Tools/Debuggers
Requires:       radare2-devel
Requires:       %{name} = %{version}

%description devel
Development files for the Iatio GUI

%prep
%setup -n iaito-%{version}
rm -rf radare2

%setup -D -T -b1 -n iaito-%{version}
mv ../iaito-translations-%{ts_version}/* ./src/translations/

%build
export CLANG_INSTALL_DIR=%{_prefix}
%cmake \
    -DIAITO_ENABLE_CRASH_REPORTS=OFF \
    -DIAITO_ENABLE_PYTHON=ON \
%if %{with python_bindings}
    -DIAITO_ENABLE_PYTHON_BINDINGS=ON \
%endif
    ../src/

%cmake_build

%install
%cmake_install

%files
%doc README.md CONTRIBUTING.md
%license COPYING
%{_bindir}/iaito
%dir %{_datadir}/RadareOrg
%dir %{_libdir}/iaito
%{_datadir}/RadareOrg/iaito
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/*.xml
%{_mandir}/man1/*

%files devel
%{_includedir}/iaito
%{_libdir}/iaito/*.cmake

%changelog
