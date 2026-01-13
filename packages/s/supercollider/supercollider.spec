#
# spec file for package supercollider
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


Name:           supercollider
Version:        3.14.1
%global tar_version 3.14.1
Release:        0
Summary:        Programming environment for audio synthesis and composition
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://supercollider.github.io/
Source0:        https://github.com/supercollider/supercollider/releases/download/Version-%{tar_version}/SuperCollider-%{tar_version}-Source.tar.bz2
Source1:        https://github.com/supercollider/supercollider/releases/download/Version-%{tar_version}/SuperCollider-%{tar_version}-Source.tar.bz2.asc
Source2:        supercollider.keyring
Patch0:         000-SuperCollider-Fix-qt-6.10.1-build.patch
Patch1:         001-SuperCollider-remove-NO_GPL3-option.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  cmake
BuildRequires:  emacs-nox
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libcurl-devel
# BuildRequires:  libcwiid-devel
BuildRequires:  libicu-devel
BuildRequires:  libjack-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  ruby
BuildRequires:  w3m
BuildRequires:  yaml-cpp-devel
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Sensors)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(atomic_ops)
%if 0%{?suse_version} > 1500
# Force pipewire over jack itself
Requires:       pipewire-libjack-0_3
%else
Requires:       jack
%endif

%description
SuperCollider is a platform for audio synthesis and algorithmic composition,
used by musicians, artists, and researchers working with sound.
SuperCollider consists of three separate components:
  1. scsynth or supernova - audio engine (the "server")
  2. sclang - programming language runtime interpreter including Qt graphical user interfaces
  3. IDE (integrated development environment) - an editor for writing code and running supercollider

%package devel
Summary:        Development files for SuperCollider
Group:          Development/Libraries/C and C++
Requires:       alsa-devel
Requires:       avahi-devel
Requires:       libjack-devel
Requires:       libsndfile-devel
Requires:       libudev-devel
Requires:       pkgconfig
Requires:       supercollider = %{version}-%{release}

%description devel
This package includes include files and libraries neede to develop
SuperCollider applications

%package emacs
Summary:        SuperCollider support for Emacs
Group:          Development/Tools/IDE
Requires:       supercollider = %{version}-%{release}
BuildArch:      noarch

%description emacs
SuperCollider support for the Emacs text editor.

%package vim
Summary:        SuperCollider support for Vim
Group:          Development/Tools/IDE
Requires:       supercollider = %{version}-%{release}
BuildArch:      noarch

%description vim
SuperCollider support for the Vim text editor.

%prep
%setup -q -n SuperCollider-%{tar_version}-Source
%autopatch -p1

%build
# remove exec flag from boost
find external_libraries/boost -type f -exec chmod -x {} \;

%cmake \
%ifarch %{ix86} x86_64
	-DSSE=ON \
	-DSSE2=ON \
%else
	-DSUPERNOVA=OFF -DNATIVE=OFF \
	-DSSE=OFF \
	-DSSE2=OFF \
%endif
%if 0%{?suse_version} > 1320
	-DCMAKE_CXX_FLAGS="-fext-numeric-literals %{optflags}" \
%endif
	-DSC_EL=ON -DSC_VIM=ON -DSUPERNOVA=ON

%make_build

%install
%cmake_install

# install external libraries needed to build external ugens
mkdir -p %{buildroot}%{_includedir}/SuperCollider/external_libraries
pushd external_libraries/
tar cf - boost* nova* | (cd %{buildroot}%{_includedir}/SuperCollider/external_libraries; tar xpf -)
popd

# install the version file
install -m0644 SCVersion.txt %{buildroot}%{_includedir}/SuperCollider/

# Remove unneeded
rm -rf %{buildroot}%{_datadir}/doc/SuperCollider

%fdupes %{buildroot}%{_includedir}/SuperCollider
%fdupes -s %{buildroot}%{_datadir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README*
%{_bindir}/sclang
# in doc
%exclude %{_datadir}/SuperCollider/AUTHORS
%exclude %{_datadir}/SuperCollider/COPYING
%exclude %{_datadir}/SuperCollider/CHANGELOG.md
%exclude %{_datadir}/SuperCollider/README.md
%exclude %{_datadir}/SuperCollider/README_LINUX.md
%{_datadir}/SuperCollider
%exclude %{_datadir}/SuperCollider/Extensions/*
%{_datadir}/mime/packages/supercollider.xml
# scsynth
%{_bindir}/scsynth
%dir %{_libdir}/SuperCollider
%{_libdir}/SuperCollider/plugins
%{_bindir}/supernova
# ide
%{_bindir}/scide
%{_datadir}/applications/SuperColliderIDE.desktop
%{_datadir}/icons/hicolor/scalable/apps/sc_ide.svg
%{_datadir}/icons/hicolor/*x*/apps/supercollider.*
%{_datadir}/metainfo/online.supercollider.SuperCollider.metainfo.xml

%files devel
%{_includedir}/SuperCollider

%files emacs
%doc editors/sc-el/README.md
%{_datadir}/emacs/site-lisp/SuperCollider
%{_datadir}/SuperCollider/Extensions/scide_scel

%files vim
%doc editors/scvim/README.md
# %{_bindir}/sclangpipe_app
# %{_bindir}/scvim
# %{_datadir}/scvim
%{_datadir}/SuperCollider/Extensions/scide_scvim/
# %dir %{_datadir}/vim
# %dir %{_datadir}/vim/addons
# %dir %{_datadir}/vim/addons/ftplugin
# %dir %{_datadir}/vim/addons/indent
# %dir %{_datadir}/vim/addons/syntax
# %{_datadir}/vim/addons/*/supercollider*
# %dir %{_datadir}/vim/registry
# %{_datadir}/vim/registry/supercollider-vim.yaml

%changelog
