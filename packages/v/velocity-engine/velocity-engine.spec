#
# spec file for package velocity-engine
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "core"
%bcond_without core
%else
%bcond_with core
%endif
%global base_name velocity-engine
%global desc \
Velocity is a Java-based template engine. It permits anyone to use the\
simple yet powerful template language to reference objects defined in\
Java code.\
When Velocity is used for web development, Web designers can work in\
parallel with Java programmers to develop web sites according to the\
Model-View-Controller (MVC) model, meaning that web page designers can\
focus solely on creating a site that looks good, and programmers can\
focus solely on writing top-notch code. Velocity separates Java code\
from the web pages, making the web site more maintainable over the long\
run and providing a viable alternative to Java Server Pages (JSPs) or\
PHP.\
Velocity's capabilities reach well beyond the realm of web sites; for\
example, it can generate SQL and PostScript and XML (see Anakia for more\
information on XML transformations) from templates. It can be used\
either as a standalone utility for generating source code and reports,\
or as an integrated component of other systems. Velocity also provides\
template services for the Turbine web application framework.\
Velocity+Turbine provides a template service that will allow web\
applications to be developed according to a true MVC model.
Version:        2.4.1
Release:        0
Summary:        Apache Velocity - Engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://velocity.apache.org/
Source0:        %{base_name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch
%if %{with core}
Name:           %{base_name}-core
%else
Name:           %{base_name}
%endif
%if %{with core}
Source100:      %{base_name}-core-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
BuildRequires:  slf4j
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.apache.velocity:velocity-master:pom:)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.dom4j:dom4j)
%endif

%description

%package parent
Summary:        Apache Velocity - Engine parent pom
Group:          Development/Libraries/Java

%description parent
%{desc}

This packages contains a parent pom needed for maven build

%package examples
Summary:        Apache Velocity Engine - Examples
Group:          Development/Libraries/Java

%description examples
%{desc}

This package contains very simple examples to use Velocity.

%package scripting
Summary:        Apache Velocity - JSR 223 Scripting
Group:          Development/Libraries/Java

%description scripting
%{desc}

This package contains JSR 223 scripting support.

%package -n velocity-custom-parser-example
Summary:        Apache Velocity Custom Parser Example
Group:          Development/Libraries/Java

%description -n velocity-custom-parser-example
%{desc}

This package contains Custom Parser Example for Apache Velocity.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
%{desc}

This package contains Javadoc documentation

%prep
%autosetup -p1 -n %{base_name}-%{version}

%if %{with core}
cp %{SOURCE100} %{name}/build.xml
%endif

%pom_disable_module spring-velocity-support
%pom_disable_module velocity-engine-core

%pom_remove_plugin :maven-clean-plugin velocity-custom-parser-example
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

%build
%if %{with core}

mkdir -p %{name}/lib
build-jar-repository -s %{name}/lib commons-lang3 slf4j/api
ant -f %{name}/build.xml package javadoc

%else

%{mvn_build} -f -s -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%endif

%install

%if %{with core}
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -pm 0644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/%{name}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
%{mvn_install_pom} %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/%{name}.pom
%add_maven_depmap %{base_name}/%{name}.pom %{base_name}/%{name}.jar

install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%else

%mvn_install

%endif

%fdupes -s %{buildroot}%{_javadocdir}

%if %{with core}
%files -f .mfiles
%license LICENSE NOTICE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%else

%files parent -f .mfiles-%{name}-parent
%license LICENSE NOTICE

%files examples -f .mfiles-%{name}-examples
%license LICENSE NOTICE

%files scripting -f .mfiles-%{name}-scripting
%license LICENSE NOTICE

%files -n velocity-custom-parser-example -f .mfiles-velocity-custom-parser-example
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc

%endif

%changelog
