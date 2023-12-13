#
# spec file for package avogadro
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


%define src_name avogadroapp-%{version}
%define i18n_rev 1.98.0

Name:           avogadro
Version:        1.98.1
Release:        0
Summary:        A Molecular design tool
License:        GPL-2.0-only
Group:          Productivity/Scientific/Chemistry
URL:            https://two.avogadro.cc/
Source0:        https://github.com/OpenChemistry/avogadroapp/archive/refs/tags/%{version}.tar.gz#/%{src_name}.tar.gz
Source1:        https://github.com/OpenChemistry/avogadro-i18n/archive/refs/tags/%{i18n_rev}.tar.gz#/avogadro-i18n-%{i18n_rev}.tar.gz
BuildRequires:  cmake >= 3.24
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  cmake(AvogadroLibs) >= 1.98.0
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(eigen3)
Recommends:     %{name}-lang

%lang_package

%description
Avogadro is an advanced molecular editor designed
for cross-platform use in computational chemistry,
molecular modeling, bioinformatics, materials science,
and related areas. It offers flexible rendering and
a powerful plugin architecture.

%prep
%setup -qn %{src_name} -b 1
ln -s avogadro-i18n-%{i18n_rev} ../avogadro-i18n

%build
%cmake \
  -DAvogadro_ENABLE_RPC=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install
rm -rfv %{buildroot}%{_datadir}/doc/AvogadroApp
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/avogadro2
%dir %{_datadir}/avogadro2
%dir %{_datadir}/avogadro2/i18n
%{_datadir}/pixmaps/avogadro2.png
%{_datadir}/applications/avogadro2.desktop
%{_datadir}/metainfo/avogadro2.appdata.xml

%files lang
%{_datadir}/avogadro2/i18n/*

%changelog
