#
# spec file for package xmobar
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


%global pkg_name xmobar
%bcond_with tests
Name:           %{pkg_name}
Version:        0.46
Release:        0
Summary:        A Minimalistic Text Based Status Bar
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-X11-devel
BuildRequires:  ghc-X11-xft-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-alsa-core-devel
BuildRequires:  ghc-alsa-mixer-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cairo-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-dbus-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-extensible-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hinotify-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-libmpd-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-netlink-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-pango-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-numbers-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-compat-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-timezone-olson-devel
BuildRequires:  ghc-timezone-series-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-temporary-devel
%endif

%description
Xmobar is a minimalistic text based status bar.

Inspired by the Ion3 status bar, it supports similar features, like dynamic
color management, output templates, and extensibility through plugins.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       libXpm-devel
Requires:       libXrandr-devel
Requires:       libXrender-devel
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%autosetup

%build
%define cabal_configure_options -fall_extensions
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license license
%doc changelog.md doc readme.org
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license license

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc changelog.md doc readme.org

%changelog
