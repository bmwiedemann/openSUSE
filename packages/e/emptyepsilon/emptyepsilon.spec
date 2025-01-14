#
# spec file for package emptyepsilon
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


Name:           emptyepsilon
Version:        2024.12.08
Release:        0
Summary:        Open source spaceship bridge simulator
License:        GPL-2.0-only
Group:          Amusements/Games/Other
URL:            https://daid.github.io/EmptyEpsilon/
Source:         EmptyEpsilon-%{version}.tar.gz
Source1:        SeriousProton-%{version}.tar.gz
Source2:        download.sh
Source3:        basis_universal.zip
Source5:        meshoptimizer.zip
Patch0:         use_bundled_basis_universal.patch
Patch1:         use_bundled_meshoptimizer.patch
BuildRequires:  SDL2-devel
BuildRequires:  bsdtar
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  sfml2-devel
BuildRequires:  xorg-x11
%if 0%{?sle_version:1}
# if sle_version is defined, this is not tumbleweed
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
%endif

%description
EmptyEpsilon places you in the roles of a spaceship's bridge officers, like those seen in Star Trek. While you can play EmptyEpsilon alone or with friends, the best experience involves 6 players working together on each ship.
Each officer fills a unique role: Captain, Helms, Weapons, Relay, Science, and Engineering. Except for the Captain, each officer operates part of the ship through a specialized screen. The Captain relies on their trusty crew to report information and follow orders.

%prep
# extract EE and SP inside the EE dir
%setup -q -a1 -n EmptyEpsilon-EE-%{version}
find -name .gitignore | xargs rm
pushd SeriousProton-EE-%{version}
%patch -P 0 -p1
popd
%patch -P 1 -p1

# extract bundled dependencies
mkdir -p SeriousProton/externals/basis
bsdtar xvf $RPM_SOURCE_DIR/basis_universal.zip --strip-components=1 -C SeriousProton/externals/basis
mkdir -p externals/meshoptimizer
bsdtar xvf $RPM_SOURCE_DIR/meshoptimizer.zip --strip-components=1 -C externals/meshoptimizer

# symlink dependencies into build dir
mkdir -p build
pushd build
ln -s ../SeriousProton-EE-%{version}
ln -s ../SeriousProton
ln -s ../externals
popd

%build
%if 0%{?sle_version}
# if sle_version is defined, this is not tumbleweed
export CC=gcc-10
export CXX=g++-10
%endif
%cmake -DSERIOUS_PROTON_DIR="SeriousProton-EE-%{version}" \
 -DCMAKE_BUILD_TYPE=Release \
 -DCPACK_PACKAGE_VERSION_MAJOR="$(echo %{version} | cut -d. -f1)" \
 -DCPACK_PACKAGE_VERSION_MINOR="$(echo %{version} | cut -d. -f2)" \
 -DCPACK_PACKAGE_VERSION_PATCH="$(echo %{version} | cut -d. -f3)" \
%if 0%{?sle_version}
 -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
%endif
 -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build -j 8

%install
%cmake_install
%fdupes %{buildroot}/%{_datadir}

%files
%doc README.md
%{_bindir}/EmptyEpsilon
%{_docdir}/emptyepsilon/script_reference.html
%{_datadir}/emptyepsilon/
%{_datadir}/applications/io.github.daid.EmptyEpsilon.desktop
%{_datadir}/icons/hicolor/512x512/apps/io.github.daid.EmptyEpsilon.png
%{_datadir}/metainfo/io.github.daid.EmptyEpsilon.metainfo.xml
%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/512x512

%changelog
