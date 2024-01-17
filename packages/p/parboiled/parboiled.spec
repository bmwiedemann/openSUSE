#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "scala"
%bcond_without scala
%else
%bcond_with scala
%endif
%global scala_short_version 2.13
%global base_name parboiled
%if %{with scala}
Name:           %{base_name}-scala
Summary:        Parboiled for Scala
%else
Name:           %{base_name}
Summary:        Java library providing parsing of input text based on PEGs
%endif
Version:        1.4.1
Release:        0
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://parboiled.org/
Source0:        https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
Source1:        %{base_name}-build.tar.xz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source2:        https://repo1.maven.org/maven2/org/parboiled/%{base_name}-core/%{version}/%{base_name}-core-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/parboiled/%{base_name}-java/%{version}/%{base_name}-java-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/parboiled/%{base_name}-scala_%{scala_short_version}/%{version}/%{base_name}-scala_%{scala_short_version}-%{version}.pom
Patch0:         restore-java8-compatibility.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
%if %{with scala}
BuildRequires:  parboiled
BuildRequires:  scala-ant
%else
BuildRequires:  objectweb-asm
%endif
BuildArch:      noarch

%description
%if %{with scala}
An internal Scala DSL for efficiently defining your parser rules.

%endif
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
This package contains javadoc for %{base_name}.

%prep
%setup -q -n %{base_name}-%{version} -a1
%patch0 -p1

cp %{SOURCE2} %{base_name}-core/pom.xml
cp %{SOURCE3} %{base_name}-java/pom.xml
cp %{SOURCE4} %{base_name}-scala/pom.xml

%build
mkdir -p lib
build-jar-repository -s lib \
%if %{with scala}
	%{base_name} scala
%else
	objectweb-asm
%endif
%{ant} \
%if %{with scala}
	-f build-scala.xml \
%endif
	package javadoc

%install
%if %{with scala}
%global modules scala
%else
%global modules core java
%endif
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
for i in %{modules}; do
  # jar
  install -pm 0644 %{base_name}-${i}/target/%{base_name}-${i}*%{version}.jar %{buildroot}%{_javadir}/%{base_name}/${i}.jar
  # pom
  %{mvn_install_pom} %{base_name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/${i}.pom
  %add_maven_depmap %{base_name}/${i}.pom %{base_name}/${i}.jar
  # javadoc
  install -dm 0755 %{buildroot}%{_javadocdir}/%{base_name}/${i}
  cp -pr %{base_name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{base_name}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG README.markdown
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{base_name}

%changelog
