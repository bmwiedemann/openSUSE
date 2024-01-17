#
# spec file for package jafama
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


Name:           jafama
Version:        2.3.1
Release:        0
Summary:        A (Strict) FastMath class with 1e-15ish accuracy
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jeffhain/jafama
Source0:        https://repo1.maven.org/maven2/net/jafama/jafama/%{version}/jafama-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/net/jafama/jafama/%{version}/jafama-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 6
BuildRequires:  maven-local
BuildRequires:  unzip
BuildArch:      noarch

%description
Jafama (Java Fast Math) is a Java library aiming at providing faster versions
of java.lang.Math treatments, at the eventual cost of 1e-15ish accuracy errors
but still handling special cases properly (NaN, +-Infinity, ties, etc.).
It also provides additional features, such as angles normalization methods,
inverse hyperbolic trigonometry, etc.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}-sources

cp %{SOURCE1} pom.xml

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.txt
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt
%doc README.txt

%changelog
