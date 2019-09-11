#
# spec file for package plexus-component-api
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


%define base_ver 1.0
%define alpha_ver 15
%define project_version %{base_ver}-alpha-%{alpha_ver}
Name:           plexus-component-api
Version:        %{base_ver}~alpha%{alpha_ver}
Release:        0
Summary:        Plexus Component API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-%{project_version}/%{name}/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar cJf plexus-component-api-1.0-alpha-15.tar.xz plexus-component-api-1.0-alpha-15/
Source0:        %{name}-%{project_version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-local
BuildRequires:  plexus-classworlds
Requires:       mvn(org.codehaus.plexus:plexus-classworlds)
BuildArch:      noarch

%description
Plexus Component API

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{project_version}
cp %{SOURCE1} build.xml

%pom_remove_parent

%pom_xpath_inject "pom:project" "<groupId>org.codehaus.plexus</groupId>"

%build
mkdir -p lib
build-jar-repository -s lib plexus/classworlds
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{project_version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
