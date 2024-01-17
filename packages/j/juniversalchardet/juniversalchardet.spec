#
# spec file for package juniversalchardet
#
# Copyright (c) 2021 SUSE LLC
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


Name:           juniversalchardet
Version:        1.0.3
Release:        0
Summary:        Encoding detector library
License:        MPL-1.1
Group:          Development/Libraries/Java
URL:            https://code.google.com/archive/p/juniversalchardet/
Source0:        https://repo1.maven.org/maven2/com/googlecode/%{name}/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/com/googlecode/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://www.mozilla.org/media/MPL/1.1/index.0c5913925d40.txt
Source3:        README.txt
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  java-javadoc >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
JUNIVERSALCHARDET is a Java port of 'universalchardet', that is the encoding
detector library of Mozilla.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -T -c
mkdir -p src/main/java
pushd src/main/java
jar -xvf %{SOURCE0}
popd
cp %{SOURCE2} LICENSE.txt
cp %{SOURCE3} .

%build
mkdir -p target/classes
javac -source 8 -target 8 -encoding UTF-8 -sourcepath src/main/java -d target/classes $(find src/main/java -name \*.java)
jar -cvf %{name}-%{version}.jar -C target/classes .
javadoc -source 8 -encoding UTF-8 \
    -d target/apidocs \
    -sourcepath src/main/java \
    -link file://%{_javadocdir}/java \
	org.mozilla.universalchardet

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc README.txt
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
