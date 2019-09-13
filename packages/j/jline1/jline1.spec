#
# spec file for package jline1
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


%global artifactId jline
Name:           %{artifactId}1
Version:        1.0
Release:        0
Summary:        Java library for reading and editing user input in console applications
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://jline.sourceforge.net/
Source0:        http://download.sourceforge.net/sourceforge/%{artifactId}/%{artifactId}-%{version}.zip
Source1:        CatalogManager.properties
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  xml-commons-resolver
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java

%description
JLine is a java library for reading and editing user input in console
applications. It features tab-completion, command history, password
masking, customizable keybindings, and pass-through handlers to use to
chain to other console applications.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}

# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Remove pre-built Windows-only binary artifacts
rm src/src/main/resources/jline/jline*.dll

# Use locally installed DTDs
mkdir build
cp -p %{SOURCE1} build/

cp -p %{SOURCE2} src/build.xml

%build
# Use locally installed DTDs
export CLASSPATH=%{_builddir}/%{name}-%{version}/build

mv src tmp
mv tmp/* .

%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 target/%{artifactId}-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{artifactId}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
%add_maven_depmap %{name}/%{artifactId}.pom %{name}/%{artifactId}.jar -v %{version},1
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}


%files -f .mfiles
%license LICENSE.txt

%files javadoc
%{_javadocdir}

%changelog
