#
# spec file for package typesafe-config
#
# Copyright (c) 2022 SUSE LLC
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


Name:           typesafe-config
Version:        1.4.1
Release:        0
Summary:        Configuration library for JVM languages
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/typesafehub/config
Source0:        %{URL}/archive/v%{version}.tar.gz#/config-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/typesafe/config/%{version}/config-%{version}.pom
Patch0:         fix-doc-lint.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
%if 0%{?rhel} >= 9
BuildRequires:  xmvn-tools
%endif

BuildArch:      noarch

%description
Configuration library for JVM languages.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n config-%{version}
%patch0 -p1

%build
pushd config
mkdir -p target/classes
javac -d target/classes \
  -source 8 \
  -target 8 \
  -g \
  -Xlint:unchecked \
  $(find src/main/java -name \*.java | xargs)
jar -cf target/config.jar -C target/classes .

%if ! 0%{?rhel} >= 9
mkdir -p target/api
javadoc -d target/api \
  -source 8 \
  -notimestamp \
  -group "Public API (version %{version})" "com.typesafe.config:com.typesafe.config.parser" \
  -group "Internal Implementation - Not ABI Stable" "com.typesafe.config.impl" \
  $(find src/main/java -name \*.java | xargs)
%endif

popd
cp %{SOURCE1} .
%mvn_artifact config-%{version}.pom config/target/config.jar

%install
%if 0%{?rhel}
%mvn_install
%else
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 config/target/config.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
%endif

%if ! 0%{?rhel} >= 9
#javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -a config/target/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}
%endif

%files -f .mfiles
%doc NEWS.md README.md
%license LICENSE-2.0.txt

%if ! 0%{?rhel} >= 9
%files javadoc
%license LICENSE-2.0.txt
%{_javadocdir}/*
%endif

%changelog
