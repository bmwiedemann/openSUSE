#
# spec file for package mchange-commons
#
# Copyright (c) 2024 SUSE LLC
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


%global git_tag mchange-commons-java-%{version}
Name:           mchange-commons
Version:        0.2.20
Release:        0
Summary:        A collection of general purpose utilities for c3p0
License:        EPL-1.0 OR LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            https://github.com/swaldman/mchange-commons-java
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{git_tag}.tar.gz
Patch0:         fix-javadoc-lint-errors.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  log4j >= 2.0
BuildRequires:  slf4j
BuildRequires:  typesafe-config >= 1.3.0
BuildArch:      noarch

%description
Originally part of c3p0, mchange-commons is a set of general purpose
utilities.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{git_tag}
%patch -P 0 -p1

find -name '*.class' -delete
find -name '*.jar' -delete

%build
export CLASS_PATH=$(build-classpath log4j log4j/log4j-{api,core} slf4j/slf4j-api typesafe-config)
mkdir -p target/classes
javac -d target/classes \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    --release 8 \
%else
    -source 8 -target 8 \
%endif
  -cp  "$CLASS_PATH" \
  $(find src/main/java -name \*.java | xargs)

jar --create \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --file=target/%{git_tag}.jar -C target/classes .
jar --update \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --file=target/%{git_tag}.jar -C src/main/resources .

mkdir -p target/api
javadoc -d target/api -source 8 \
  -classpath "$CLASS_PATH" \
  -notimestamp \
  $(find src/main/java -name \*.java | xargs)
sed "s/@mchange-commons-java.version.maven@/%{version}/g" \
  src/main/maven/pom.xml > target/%{git_tag}.pom

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -pm 644 target/%{git_tag}.jar %{buildroot}%{_javadir}/%{name}/mchange-commons-java.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} target/%{git_tag}.pom %{buildroot}%{_mavenpomdir}/%{name}/mchange-commons-java.pom
%add_maven_depmap %{name}/mchange-commons-java.pom %{name}/mchange-commons-java.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -a target/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE*

%files javadoc
%license LICENSE*
%{_javadocdir}/%{name}

%changelog
