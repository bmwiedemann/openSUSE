#
# spec file for package parboiled
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


%global scala_short_version 2.10
Name:           parboiled
Version:        1.1.6
Release:        0
Summary:        Java/Scala library providing parsing of input text based on PEGs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://parboiled.org/
Source0:        https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
Source1:        %{name}-%{version}-build.tar.xz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source2:        http://repo1.maven.org/maven2/org/parboiled/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/parboiled/%{name}-java/%{version}/%{name}-java-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/parboiled/%{name}-scala_%{scala_short_version}/%{version}/%{name}-scala_%{scala_short_version}-%{version}.pom
Patch0:         parboiled-port-to-objectweb-asm-5.0.1.patch
BuildRequires:  ant
BuildRequires:  ant-scala
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  objectweb-asm
BuildConflicts: java-devel >= 9
Requires:       mvn(org.ow2.asm:asm)
Requires:       mvn(org.ow2.asm:asm-analysis)
Requires:       mvn(org.ow2.asm:asm-tree)
Requires:       mvn(org.ow2.asm:asm-util)
BuildArch:      noarch

%description
parboiled is a mixed Java/Scala library providing parsing of
arbitrary input text based on Parsing expression grammars (PEGs).
PEGs are an alternative to context free grammars (CFGs) for formally
specifying syntax, they make a replacement for regular expressions
and generally have some advantages over the "traditional" way of
building parser via CFGs.

%package scala
Summary:        Parboiled for Scala
Group:          Development/Libraries/Java
Requires:       mvn(org.parboiled:parboiled-core) = 1.1.6
Requires:       mvn(org.scala-lang:scala-library)

%description scala
An internal Scala DSL for efficiently defining your parser rules.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -a1

find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p1

%build
mkdir -p lib
build-jar-repository -s lib objectweb-asm
%{ant} -Dscala.libDir=%{_datadir}/scala/lib package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
for i in core java scala; do
  install -pm 0644 %{name}-${i}/target/%{name}-${i}*%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
done
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}/core.pom
%add_maven_depmap %{name}/core.pom %{name}/core.jar
install -pm 0644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}/java.pom
%add_maven_depmap %{name}/java.pom %{name}/java.jar
install -pm 0644 %{SOURCE4} %{buildroot}%{_mavenpomdir}/%{name}/scala.pom
%add_maven_depmap %{name}/scala.pom %{name}/scala.jar -f scala
# javadoc
for i in core java scala; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGELOG README.markdown
%license LICENSE

%files scala -f .mfiles-scala
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
