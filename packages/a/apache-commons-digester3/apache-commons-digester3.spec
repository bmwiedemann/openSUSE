#
# spec file for package apache-commons-digester3
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define base_name       digester3
%define short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        3.2
Release:        0
Summary:        Apache Commons Digester
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-digester/
Source0:        https://archive.apache.org/dist/commons/digester/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-logging
BuildRequires:  cglib
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
The Apache Commons Digester package lets you configure an XML to Java object
mapping module which triggers certain actions called rules whenever a
particular pattern of nested XML elements is recognized.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin
%pom_remove_plugin :maven-jar-plugin

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-logging-api \
    cglib/cglib \
    commons-beanutils
ant jar javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}.jar
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt NOTICE.txt

%changelog
