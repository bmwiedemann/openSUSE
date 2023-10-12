#
# spec file for package parboiled
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


Name:           parboiled
Version:        1.4.1
Release:        0
Summary:        Java library providing parsing of input text based on PEGs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://parboiled.org/
Source0:        https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
Source1:        %{name}-build.tar.xz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source2:        https://repo1.maven.org/maven2/org/parboiled/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/parboiled/%{name}-java/%{version}/%{name}-java-%{version}.pom
Patch0:         restore-java8-compatibility.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  objectweb-asm
BuildArch:      noarch

%description
parboiled is a mixed Java library providing parsing of
arbitrary input text based on Parsing expression grammars (PEGs).
PEGs are an alternative to context free grammars (CFGs) for formally
specifying syntax, they make a replacement for regular expressions
and generally have some advantages over the "traditional" way of
building parser via CFGs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p1

cp %{SOURCE2} %{name}-core/pom.xml
cp %{SOURCE3} %{name}-java/pom.xml

%build
mkdir -p lib
build-jar-repository -s lib \
	objectweb-asm
%{ant} \
	package javadoc

%install
%global modules core java
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
for i in %{modules}; do
  # jar
  install -pm 0644 %{name}-${i}/target/%{name}-${i}*%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  # pom
  %{mvn_install_pom} %{name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
  # javadoc
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG README.markdown
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
