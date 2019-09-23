#
# spec file for package felix-osgi-core
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


%global bundle org.osgi.core
Name:           felix-osgi-core
Version:        1.4.0
Release:        0
Summary:        Felix OSGi R4 Core Bundle
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org/site/apache-felix-osgi-core.html
Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1:        %{name}-%{version}-build.xml.tar.gz
Patch0:         jdk9.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version} -a1
%patch0 -p1

mkdir -p .m2/repository

%pom_remove_parent .
%pom_xpath_inject "pom:project" "<groupId>org.apache.felix</groupId>" .

%build
%{ant} -Dmaven.settings.offline=true \
     -Dmaven.repo.local=.m2/repository \
     package javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/felix/%{bundle}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}/felix
install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/felix/%{bundle}.pom
%add_maven_depmap felix/%{bundle}.pom felix/%{bundle}.jar -a "org.osgi:%{bundle}"

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
