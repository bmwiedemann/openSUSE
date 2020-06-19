#
# spec file for package ghc-hxt
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


%global pkg_name hxt
Name:           ghc-%{pkg_name}
Version:        9.3.1.18
Release:        0
Summary:        A collection of tools for processing XML with Haskell
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hxt-charproperties-devel
BuildRequires:  ghc-hxt-regex-xmlschema-devel
BuildRequires:  ghc-hxt-unicode-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros

%description
The Haskell XML Toolbox bases on the ideas of HaXml and HXML, but introduces a
more general approach for processing XML with Haskell. The Haskell XML Toolbox
uses a generic data model for representing XML documents, including the DTD
subset and the document subset, in Haskell. It contains a validating XML
parser, a HTML parser, namespace support, an XPath expression evaluator, an
XSLT library, a RelaxNG schema validator and funtions for serialization and
deserialization of user defined data. The library makes extensive use of the
arrow approach for processing XML. Since version 9 the toolbox is partitioned
into various (sub-)packages. This package contains the core functionality,
hxt-curl, hxt-tagsoup, hxt-relaxng, hxt-xpath, hxt-xslt, hxt-regex-xmlschema
contain the extensions. hxt-unicode contains encoding and decoding functions,
hxt-charproperties char properties for unicode and XML.

Changes from 9.3.1.15: Bug in quoting PI instructions in showXmlTrees fixed

Changes from 9.3.1.14: For ghc-7.10 network-uri is automatically selected

Changes from 9.3.1.13: ghc-7.10 compatibility

Changes from 9.3.1.12: Bug when unpickling an empty attribute value removed

Changes from 9.3.1.11: Bug fix in haddock comments

Changes from 9.3.1.10: Bug in DTD validation, space and time leak in delta
removed

Changes from 9.3.1.9: lower bound of mtl dependency lowered to 2.0.1

Changes from 9.3.1.8: Bug in hread removed

Changes from 9.3.1.7: Foldable and Traversable instances for NTree added
Control.Except used instead of deprecated Control.Error

Changes from 9.3.1.6: canonicalize added in hread and hreadDoc

Changes from 9.3.1.4: conditionally (no default) dependency from networt
changed to network-uri with flag "network-uri"

Changes from 9.3.1.3: warnings from ghc-7.8.1 removed

Changes from 9.3.1.2: https as protocol added

Changes from 9.3.1.1: new parser xreadDoc

Changes from 9.3.1.0: in readString all input decoding switched off

Changes from 9.3.0.1: lower bound for network set to be >= 2.4

Changes from 9.3.0: upper bound for network set to be < 2.4 (URI signatures
changed in 2.4)

Changes from 9.2.2: XMLSchema validation integrated

Changes from 9.2.1: user defined mime type handlers added

Changes from 9.2.0: New warnings from ghc-7.4 removed.

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
%doc examples

%changelog
