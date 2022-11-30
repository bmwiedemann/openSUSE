#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global pkg_name xmonad
%bcond_with tests
Name:           %{pkg_name}
Version:        0.17.1
Release:        0
Summary:        A tiling window manager
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source10:       xmonad.desktop
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-X11-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-setlocale-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xinerama)
Suggests:       ghc-xmonad-contrib-devel
Suggests:       ghc-xmonad-devel
# windowmanager is a generic provides for every WM - there are things (like Xvnc)
# That rely on the prsence of 'a WM', but do not care which one it is
Provides:       windowmanager
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-quickcheck-classes-devel
%endif

%description
Xmonad is a tiling window manager for X. Windows are arranged automatically to
tile the screen without gaps or overlap, maximising screen use. All features of
the window manager are accessible from the keyboard: a mouse is strictly
optional. xmonad is written and extensible in Haskell. Custom layout
algorithms, and other extensions, may be written by the user in config files.
Layouts are applied dynamically, and different layouts may be used on each
workspace. Xinerama is fully supported, allowing windows to be tiled on several
screens.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun):ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}
install -m0644 -D man/xmonad.1 %{buildroot}%{_mandir}/man1/xmonad.1
gzip %{buildroot}%{_mandir}/man1/xmonad.1
%define desktop_src %{buildroot}%{_datadir}/xsessions/xmonad.desktop
install -m0644 -D %{SOURCE10} %{desktop_src}
%suse_update_desktop_file %{desktop_src}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGES.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/xmonad.1%{?ext_man}
%{_datadir}/xsessions/xmonad.desktop

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGES.md README.md

%changelog
