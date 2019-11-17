#
# spec file for package freemarker
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


%bcond_with jp_minimal
Name:           freemarker
Version:        2.3.28
Release:        0
Summary:        The Apache FreeMarker Template Engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://freemarker.apache.org/
Source0:        https://github.com/apache/incubator-freemarker/archive/v%{version}/%{name}-%{version}.tar.gz
# Remove JSP 2.0 API usage
Patch1:         jsp-api.patch
# Compile only the classes compatible with the version of jython that we have
Patch2:         jython-compatibility.patch
# illegal character in the javadoc comment
Patch3:         fix-javadoc-encoding.patch
# Disable JRebel integration, it is not free software and not available in openSUSE
Patch5:         no-javarebel.patch
# enable jdom extension
Patch6:         enable-jdom.patch
# Fix compatibility with javacc 7
Patch7:         javacc-7.patch
BuildRequires:  ant fdupes
BuildRequires:  apache-commons-logging
BuildRequires:  apache-parent
BuildRequires:  aqute-bnd
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  hamcrest
BuildRequires:  ivy-local
BuildRequires:  javacc >= 7.0
BuildRequires:  jaxen >= 1.1
BuildRequires:  jcl-over-slf4j
BuildRequires:  jdom >= 1.0
BuildRequires:  junit
BuildRequires:  log4j-over-slf4j
BuildRequires:  slf4j
BuildRequires:  xalan-j2 >= 2.7.0
BuildConflicts: java-devel >= 9
BuildArch:      noarch
%if %{without jp_minimal}
BuildRequires:  dom4j
BuildRequires:  jython
BuildRequires:  rhino >= 1.6
BuildRequires:  saxpath
%endif

%description
Apache FreeMarker is a template engine: a Java library to generate text output
(HTML web pages, e-mails, configuration files, source code, etc.) based on
templates and changing data. Templates are written in the FreeMarker Template
Language (FTL), which is a simple, specialized language (not a full-blown
programming language like PHP).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name "*.jar" -delete
find -type f -name "*.class" -delete

%patch1
%patch2 -p1
%patch3
%patch5
%patch6
%patch7 -p1

# Use system ivy settings
rm ivysettings.xml

# Correct classpath for Javadoc generation
sed -i 's/cachepath conf="IDE"/cachepath conf="javadoc"/' build.xml
sed -i '/conf name="IDE"/i<conf name="javadoc" extends="build.jython2.2,build.jsp2.1" />' ivy.xml

# Drop unnecessary dep on avalon
sed -i -e '/avalon-logkit/d' ivy.xml
rm src/main/java/freemarker/log/_AvalonLoggerFactory.java

%if %{with jp_minimal}
# Drop dep on optional extra deps for minimal build
sed -i -e '/"rhino"/d' -e '/"jython"/d' ivy.xml
rm -rf src/main/java/freemarker/ext/{rhino,jython,ant}
rm src/main/java/freemarker/template/utility/JythonRuntime.java
# Drop dep on additional xml backends for minimal build
sed -i -e '/dom4j/d' -e '/saxpath/d' ivy.xml
rm src/main/java/freemarker/ext/xml/_Dom4jNavigator.java
%endif

%{mvn_file} org.%{name}:%{name} %{name}

%build
ant -Divy.mode=local -Ddeps.available=true javacc jar javadoc maven-pom

%install
%{mvn_artifact} build/pom.xml build/%{name}.jar
%mvn_install -J build/api
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md RELEASE-NOTES
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
