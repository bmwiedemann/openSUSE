#
# spec file for package aho-corasick-double-array-trie
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


Name:           aho-corasick-double-array-trie
Version:        1.2.1
Release:        0
Summary:        Aho Corasick algorithm implementation based on Double Array Trie
License:        Apache-2.0
URL:            https://github.com/hankcs/AhoCorasickDoubleArrayTrie
Source0:        https://github.com/hankcs/AhoCorasickDoubleArrayTrie/archive/v%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildArch:      noarch

%description
An extremely fast implementation of Aho Corasick algorithm based on Double Array Trie.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n AhoCorasickDoubleArrayTrie-%{version}
cp %{SOURCE1} .

%pom_remove_plugin :maven-source-plugin

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
