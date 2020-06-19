#
# spec file for package ghc-rfc5051
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name rfc5051
Name:           ghc-%{pkg_name}
Version:        0.1.0.4
Release:        0
Summary:        Simple unicode collation as per RFC5051
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-rpm-macros

%description
This library implements 'i;unicode-casemap', the simple, non locale-sensitive
unicode collation algorithm described in RFC 5051
(<http://www.rfc-editor.org/rfc/rfc5051.txt>). Proper unicode collation can be
done using text-icu, but that is a big dependency that depends on a large C
library, and rfc5051 might be better for some purposes.

Here is a list of strings sorted by the Prelude's 'sort' function: 'Abe Oeb abe
ab&#233; oeb &#193;be &#196;be &#212;eb &#225;be &#228;be &#244;eb'.

Here is the same list sorted by 'sortBy compareUnicode':

'Abe abe ab&#233; &#193;be &#225;be &#196;be &#228;be Oeb oeb &#212;eb
&#244;eb'.

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

%files devel -f %{name}-devel.files

%changelog
