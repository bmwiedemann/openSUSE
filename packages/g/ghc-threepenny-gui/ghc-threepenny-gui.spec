#
# spec file for package ghc-threepenny-gui
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


%global pkg_name threepenny-gui
Name:           ghc-%{pkg_name}
Version:        0.9.0.0
Release:        0
Summary:        GUI framework that uses the web browser as a display
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-snap-server-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-websockets-devel
BuildRequires:  ghc-websockets-snap-devel

%description
Threepenny-GUI is a GUI framework that uses the web browser as a display.

It's very easy to install because everyone has a web browser installed.

A program written with Threepenny is essentially a small web server that
displays the user interface as a web page to any browser that connects to it.
You can freely manipulate the HTML DOM and handle JavaScript events from your
Haskell code.

Stability forecast: This is an experimental release! Send me your feedback!
Significant API changes are likely in future versions.

NOTE: This library contains examples, but they are not built by default.
To build and install the example, use the 'buildExamples' flag like this

'cabal install threepenny-gui -fbuildExamples'.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/samples
%dir %{_datadir}/%{pkg_name}-%{version}/samples/static
%dir %{_datadir}/%{pkg_name}-%{version}/samples/static/css
%{_datadir}/%{pkg_name}-%{version}/samples/static/*.html
%{_datadir}/%{pkg_name}-%{version}/samples/static/*.png
%{_datadir}/%{pkg_name}-%{version}/samples/static/*.wav
%{_datadir}/%{pkg_name}-%{version}/samples/static/css/*.css
%{_datadir}/%{pkg_name}-%{version}/samples/static/css/*.png

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
