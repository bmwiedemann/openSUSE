#
# spec file for package velocity-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global desc \
VelocityTools is an integrated collection of Velocity subprojects \
with the common goal of creating tools and infrastructure to speed \
and ease development of both web and non-web applications using the \
Velocity template engine.
Name:           velocity-tools
Version:        3.2
Release:        0
Summary:        Apache Velocity Tools
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://velocity.apache.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Patch0:         0001-Port-to-backward-compatible-json-simple-2.3.1.patch
BuildRequires:  ant
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-digester3
BuildRequires:  apache-commons-lang3
BuildRequires:  fdupes
BuildRequires:  glassfish-el-api
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local >= 6
BuildRequires:  json-simple
BuildRequires:  slf4j
BuildRequires:  velocity-engine-core
BuildArch:      noarch

%description
VelocityTools is an integrated collection of Velocity subprojects
with the common goal of creating tools and infrastructure to speed
and ease development of both web and non-web applications using the
Velocity template engine.

%package generic
Summary:        Apache Velocity Tools - Generic tools
Group:          Development/Libraries/Java

%description generic
%{desc}

Generic tools that can be used in any context.

%package view
Summary:        Apache Velocity Tools - View tools
Group:          Development/Libraries/Java

%description view
%{desc}

Tools to be used in a servlet context.

%package view-jsp
Summary:        Apache Velocity Tools - JSP support
Group:          Development/Libraries/Java

%description view-jsp
%{desc}

Enables the use of Velocity under a JSP environment.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
%{desc}

This package contains Javadoc documentation

%prep
%autosetup -p1 -n %{name}-%{version} -a1

%pom_disable_module velocity-tools-examples

%build
mkdir -p lib
build-jar-repository -s lib \
    commons-beanutils \
    commons-digester3 \
    commons-lang3 \
    glassfish-el-api \
    glassfish-jsp-api/javax.servlet.jsp-api \
    glassfish-servlet-api \
    json-simple \
    slf4j/api \
    velocity-engine/velocity-engine-core
ant package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for module in generic view view-jsp; do
  install -pm 0644 %{name}-${module}/target/%{name}-${module}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-${module}.jar
  %{mvn_install_pom} %{name}-${module}/pom.xml \
    %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${module}.pom
  %add_maven_depmap %{name}/%{name}-${module}.pom %{name}/%{name}-${module}.jar -f ${module}
  cp -r %{name}-${module}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${module}
done
%fdupes -s %{buildroot}%{_javadocdir}

%files generic -f .mfiles-generic
%license LICENSE NOTICE
%doc README.md

%files view -f .mfiles-view
%license LICENSE NOTICE

%files view-jsp -f .mfiles-view-jsp
%license LICENSE NOTICE

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
