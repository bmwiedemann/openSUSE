#
# spec file for package bsh2
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2000-2008, JPackage Project
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


%define orig_name bsh
Name:           bsh2
Version:        2.1.1
Release:        0
Summary:        Scripting for Java (BeanShell Version 2.x)
License:        LGPL-2.0-or-later OR SPL-1.0
Group:          Development/Libraries/Java
URL:            http://www.beanshell.org/
Source0:        beanshell-%{version}.tar.xz
#PATCH-FIX-OPENSUSE: use html output and JVM's built-in xmlns:redirect
Patch3:         bsh-2.0b5-docs.patch
Patch1001:      reproducible.patch
Patch1002:      0000-source-target-1.8.patch
BuildRequires:  ant
BuildRequires:  bsf
BuildRequires:  bsf-javadoc
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local
Requires:       bsf
Requires:       javapackages-tools
BuildArch:      noarch

%description
BeanShell is an embeddable Java source interpreter with object
scripting language features, written in Java. BeanShell executes
standard Java statements and expressions, in addition to obvious
scripting commands and syntax. BeanShell supports scripted objects as
simple method closures like those in Perl and JavaScript. BeanShell
can be used interactively for Java experimentation and debugging or
as a scripting engine for applications.

%package bsf
Summary:        BSF support for bsh2
Group:          Development/Libraries/Java
Requires:       bsf

%description bsf
Scripting for Java (BeanShell Version 2.x) (BSF support).

%package classgen
Summary:        ASM support for bsh2
Group:          Development/Libraries/Java

%description classgen
Scripting for Java (BeanShell Version 2.x) (ASM support).

%package manual
Summary:        Documentation for bsh2
Group:          Documentation/HTML

%description manual
Scripting for Java (BeanShell Version 2.x) (Manual).

%package javadoc
Summary:        Javadoc for bsh2
Group:          Documentation/HTML

%description javadoc
Scripting for Java (BeanShell Version 2.x) (Java Documentation).

%package demo
Summary:        Demonstrations and samples for bsh2
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
Scripting for Java (BeanShell Version 2.x) (demo and samples).

%prep
%setup -q -n beanshell-%{version}
%patch3 -p1
%patch1001 -p1
%patch1002 -p1

sed -i 's,org.apache.xalan.xslt.extensions.Redirect,http://xml.apache.org/xalan/redirect,' docs/manual/xsl/*.xsl

%build
build-jar-repository -s -p lib bsf javacc glassfish-servlet-api
ant dist

%install
# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
rm -f dist/%{orig_name}-%{version}-src.jar
rm -f dist/%{orig_name}-%{version}-sources.jar
for jar in dist/*.jar; do
  install -m 644 ${jar} %{buildroot}%{_javadir}/%{name}/`basename ${jar} -%{version}.jar`.jar
done

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-bsh.pom
%add_maven_depmap JPP.%{name}-bsh.pom %{name}/bsh.jar -a org.beanshell:%{name},bsh:bsh,bsh:bsh-bsf,org.beanshell:bsh

# manual
find docs "(" -name ".cvswrappers" -o -name "*.xml" -o -name "*.xsl" -o -name "*.log" ")" -delete
(cd docs/manual && mv -f html/* . && rm -Rf html xsl)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a javadoc/* %{buildroot}%{_javadocdir}/%{name}

# demo
for i in `find tests -name "*.bsh"`; do
  perl -p -i -e 's,^\n?#!(/(usr/)?bin/java bsh\.Interpreter|/bin/sh),#!%{_bindir}/%{name},' $i
done

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a tests %{buildroot}%{_datadir}/%{name}
find %{buildroot}%{_datadir}/%{name} -type d \
  | sed 's|'%{buildroot}'|%dir |' >  %{name}-demo-%{version}.files
find %{buildroot}%{_datadir}/%{name} -type f -name "*.bsh" \
  | sed 's|'%{buildroot}'|%attr(0755,root,root) |'      >> %{name}-demo-%{version}.files
find %{buildroot}%{_datadir}/%{name} -type f ! -name "*.bsh" \
  | sed 's|'%{buildroot}'|%attr(0644,root,root) |'      >> %{name}-demo-%{version}.files
# bshservlet
mkdir -p %{buildroot}%{_datadir}/%{name}/bshservlet
(cd %{buildroot}%{_datadir}/%{name}/bshservlet
jar xf $RPM_BUILD_DIR/beanshell-%{version}/dist/bshservlet.war
)
# scripts
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script
# JPackage Project (http://jpackage.sourceforge.net)
# Source functions library
. %{_datadir}/java-utils/java-functions
# Source system prefs
if [ -f %{_sysconfdir}/%{name}.conf ] ; then
  . %{_sysconfdir}/%{name}.conf
fi
# Source user prefs
if [ -f \$HOME/.%{name}rc ] ; then
  . \$HOME/.%{name}rc
fi
# Configuration
MAIN_CLASS=bsh.Interpreter
if [ -n "\$BSH_DEBUG" ]; then
  BASE_FLAGS=-Ddebug=true
fi
BASE_JARS="%{name}.jar"
# Set parameters
set_jvm
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS
# Let's start
run "\$@"
EOF
cat > %{buildroot}%{_bindir}/%{name}doc << EOF
#!/usr/bin/env %{_bindir}/%{name}
EOF
cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/%{name}doc
%fdupes -s %{buildroot}
%fdupes docs/

%files -f .mfiles
%{_javadir}/%{name}/%{orig_name}.jar
%{_javadir}/%{name}/%{orig_name}-classpath*.jar
%{_javadir}/%{name}/%{orig_name}-commands*.jar
%{_javadir}/%{name}/%{orig_name}-core*.jar
%{_javadir}/%{name}/%{orig_name}-engine*.jar
%{_javadir}/%{name}/%{orig_name}-reflect*.jar
%{_javadir}/%{name}/%{orig_name}-util*.jar
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}doc
%license LICENSE
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bshservlet

%files bsf
%{_javadir}/%{name}/%{orig_name}-bsf*.jar

%files classgen
%{_javadir}/%{name}/%{orig_name}-classgen*.jar

%files manual
%doc docs/*

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}

%files demo -f %{name}-demo-%{version}.files

%changelog
