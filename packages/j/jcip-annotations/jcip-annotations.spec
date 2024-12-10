#
# spec file for package jcip-annotations
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


Name:           jcip-annotations
Version:        1.0
Release:        0
Summary:        Java Concurrency in Practice
License:        CC-BY-2.5
Group:          Development/Libraries/Java
URL:            http://www.jcip.net/
Source0:        http://www.jcip.net/jcip-annotations-src.jar
Source1:        https://repo1.maven.org/maven2/net/jcip/jcip-annotations/1.0/jcip-annotations-1.0.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
Class, field, and method level annotations for describing thread-safety
policies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Class, field, and method level annotations for describing thread-safety
policies.

%prep
%setup -q -c
mkdir -p target/site/apidocs/
mkdir -p target/classes/
mkdir -p src/main/java/
mv net src/main/java

%build
javac -source 1.8 -target 1.8 -d target/classes $(find src/main/java -name "*.java")
javadoc -source 1.8 -notimestamp -d target/site/apidocs -sourcepath src/main/java net.jcip.annotations
for f in $(find aQute/ -type f -not -name "*.class"); do
    cp $f target/classes/$f
done
pushd target/classes
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --manifest=../../META-INF/MANIFEST.MF --file=../%{name}-%{version}.jar *
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.github.stephenc.jcip:%{name}"

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
