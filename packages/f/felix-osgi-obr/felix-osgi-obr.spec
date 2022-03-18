#
# spec file for package felix-osgi-obr
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


%global bundle org.osgi.service.obr
Name:           felix-osgi-obr
Version:        1.0.2
Release:        0
Summary:        Felix OSGi OBR Service API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
Source0:        http://archive.apache.org/dist/felix/org.osgi.service.obr-%{version}-project.tar.gz
Source1:        %{bundle}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  osgi-core
Requires:       mvn(org.osgi:osgi.core)
BuildArch:      noarch

%description
OSGi OBR Service API.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
cp %{SOURCE1} build.xml

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"

# Use latest OSGi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core

%build
mkdir -p lib
build-jar-repository -s lib osgi-core
%{ant} package javadoc

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
