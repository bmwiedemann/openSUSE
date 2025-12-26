#
# spec file for package pcollections
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           pcollections
Version:        5.0.0
Release:        0
Summary:        A Persistent Java Collections Library
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/hrldcpr/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  maven-local
BuildArch:      noarch

%description
PCollections serves as a persistent and immutable analogue of the Java
Collections Framework. This includes efficient, thread-safe, generic,
immutable, and persistent stacks, maps, vectors, sets, and bags, compatible
with their Java Collections counterparts.

Persistent and immutable datatypes are increasingly appreciated as a simple,
design-friendly, concurrency-friendly, and sometimes more time- and
space-efficient alternative to mutable datatypes.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup

cp %{SOURCE1} pom.xml

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc {CHANGELOG,README}.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
