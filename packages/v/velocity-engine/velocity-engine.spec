#
# spec file for package velocity-engine
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

Name:           velocity-engine
Version:        2.3
Release:        0
Summary:        Apache Velocity - Engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://velocity.apache.org/
Source0:        %{name}-%{version}.tar.xz
Patch1:         build.patch
BuildRequires:  fdupes
BuildRequires:  junit
BuildRequires:  maven-local
%if 0%{?rhel} >=9
BuildRequires:  xmvn-tools
BuildRequires:  xmvn-minimal
%endif
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity-master:pom:)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description

%package core
Summary:        Apache Velocity - Engine
Group:          Development/Libraries/Java

%description core
%{desc}

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
%setup -q
%patch1 -p1

%pom_disable_module spring-velocity-support

%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.codehaus.mojo:templating-maven-plugin velocity-engine-core
%pom_remove_plugin com.google.code.maven-replacer-plugin:replacer velocity-engine-core
%pom_remove_plugin :maven-clean-plugin velocity-custom-parser-example
%if 0%{?rhel}
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_parent
%endif
%pom_xpath_inject '/pom:project' '<groupId>org.apache.velocity</groupId>'
%pom_xpath_inject 'pom:plugins/pom:plugin[pom:artifactId/text()="maven-compiler-plugin"]' '<version>3.8.1</version>'

sed 's/\${project\.version}/2.2/' \
    velocity-engine-core/src/main/java-templates/org/apache/velocity/runtime/VelocityEngineVersion.java \
    >velocity-engine-core/src/main/java/org/apache/velocity/runtime/VelocityEngineVersion.java

sed -i 's:template:xtemplate:g' \
    velocity-engine-core/src/main/parser/Parser.jjt

%build
%{mvn_build} -f -s -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files core -f .mfiles-%{name}-core
%license LICENSE NOTICE
%doc README.md

%files parent -f .mfiles-%{name}-parent
%license LICENSE NOTICE

%files examples -f .mfiles-%{name}-examples
%license LICENSE NOTICE

%files scripting -f .mfiles-%{name}-scripting
%license LICENSE NOTICE

%files -n velocity-custom-parser-example -f .mfiles-velocity-custom-parser-example
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc

%changelog
