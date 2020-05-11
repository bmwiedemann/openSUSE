#
# spec file for package ghc-HsYAML-aeson
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global pkg_name HsYAML-aeson
Name:           ghc-%{pkg_name}
Version:        0.2.0.0
Release:        0
Summary:        JSON to YAML Adapter
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsYAML-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel

%description
The [YAML 1.2](https://yaml.org/spec/1.2/spec.html) format provides a much
richer data-model and feature-set than the [JavaScript Object Notation
(JSON)](https://tools.ietf.org/html/rfc7159) format. However, sometimes it's
desirable to ignore the extra capabilities and treat YAML as if it was merely a
more convenient markup format for humans to write JSON data. To this end this
module provides a compatibility layer atop
[HsYAML](https://hackage.haskell.org/package/HsYAML) which allows decoding YAML
documents in the more limited JSON data-model while also providing convenience
by reusing [aeson](https://hackage.haskell.org/package/aeson)'s 'FromJSON'
instances for decoding the YAML data into native Haskell data types.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
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
%license LICENSE.GPLv2

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
