#
# spec file for package felix-gogo-runtime
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


%global bundle  org.apache.felix.gogo.runtime
Name:           felix-gogo-runtime
Version:        1.1.0
Release:        0
Summary:        Apache Felix Gogo command line shell for OSGi
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz
Source1:        %{bundle}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  osgi-compendium
BuildRequires:  osgi-core
BuildArch:      noarch

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
cp %{SOURCE1} build.xml

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"

%build
mkdir -p lib
build-jar-repository -s lib osgi-core osgi-compendium
%{ant} jar javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/felix/%{bundle}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/felix
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/felix/%{bundle}.pom
%add_maven_depmap felix/%{bundle}.pom felix/%{bundle}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
