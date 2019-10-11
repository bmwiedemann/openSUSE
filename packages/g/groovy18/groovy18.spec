#
# spec file for package groovy18
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


%global majorversion 1.8
%global archiver 1_8_9
Name:           groovy18
Version:        1.8.9
Release:        0
Summary:        Dynamic language for the Java Platform
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://groovy-lang.org
Source0:        https://github.com/groovy/groovy-core/archive/GROOVY_%{archiver}.zip
# thanks to Johannes Lips and Matt Spaulding
Source1:        groovy18-script
Source2:        groovy18-starter.conf
Source3:        http://www.apache.org/licenses/LICENSE-2.0.txt
# thanks to Andy Grimm
Patch0:         groovy-inner-interface-annotations.patch
Patch1:         groovy-build-with-java8.patch
Patch2:         groovy-servlet31.patch
Patch3:         groovy-commons-cli-1.3.patch
Patch4:         groovy-CVE-2015-3253-and-CVE-2016-6814.patch
Patch5:         groovy18-sourcetarget.patch
Patch6:         groovy18-iterator.patch
Patch7:         groovy18-securitymanager.patch
BuildRequires:  ant
BuildRequires:  ant-antlr
BuildRequires:  antlr
BuildRequires:  apache-commons-cli
BuildRequires:  apache-ivy
BuildRequires:  asm3
BuildRequires:  bsf
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  jansi
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jline1
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xstream
BuildRequires:  mvn(javax.servlet:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildConflicts: java-devel >= 9
Requires:       %{name}-lib = %{version}-%{release}
# Used for servlet / gsp:
Requires:       glassfish-jsp-api
Requires:       glassfish-servlet-api
# Only used for BSF adapter:
Requires:       mvn(bsf:bsf)
# Used to dump out the AST, xpp only needed for reading:
Requires:       mvn(com.thoughtworks.xstream:xstream)
# Only used for command line tools:
Requires:       mvn(commons-cli:commons-cli)
Requires:       mvn(commons-logging:commons-logging)
# Used for richer interactive groovysh support:
Requires:       mvn(jline:jline:1)
# Following dependencies are optional from Maven POV,
# but upstream ships them in binary distribution
Requires:       mvn(junit:junit)
# Only used for Ant tasks & scripting tool:
Requires:       mvn(org.apache.ant:ant)
Requires:       mvn(org.apache.ant:ant-antlr)
Requires:       mvn(org.apache.ant:ant-junit)
Requires:       mvn(org.apache.ant:ant-launcher)
# Used for @Grab and Grapes:
Requires:       mvn(org.apache.ivy:ivy)
#Requires:       mvn(org.codehaus.gpars:gpars)
Requires:       mvn(org.fusesource.jansi:jansi)
# Joint compilation requires tools.jar from java-devel
Suggests:       java-devel
BuildArch:      noarch

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java byte-code so you can use it anywhere
you can use Java.

%package lib
Summary:        Groovy JAR artifact
Group:          Development/Libraries/Java

%description lib
This package contains Groovy JAR artifact.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n groovy-core-GROOVY_%{archiver}
find . -name "*.class" -delete
find . -name "*.jar" -delete

cp %{SOURCE3} .

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# build.xml is not compatible with Ant 1.10+
sed -i "s| depends=\"-excludeLegacyAntVersion\"||" build.xml

# We don't want to generate auto-R on optional dependencies
%pom_xpath_replace "pom:dependency[pom:optional[text()='true']]/pom:scope" "<scope>provided</scope>"

# java 7 apis
%pom_remove_dep org.livetribe:livetribe-jsr223
# explicit tomcat apis
sed -i "s|<groupId>javax.servlet</groupId>|<groupId>org.apache.tomcat</groupId>|" pom.xml
sed -i "s|<artifactId>jsp-api</artifactId>|<artifactId>tomcat-jsp-api</artifactId>|" pom.xml
sed -i "s|<version>2.0</version>|<version>any</version>|" pom.xml
sed -i "s|<artifactId>servlet-api</artifactId>|<artifactId>tomcat-servlet-api</artifactId>|" pom.xml
sed -i "s|<version>2.4</version>|<version>any</version>|" pom.xml

# fix non ASCII chars
for s in src/main/groovy/transform/NotYetImplemented.java\
  src/main/org/codehaus/groovy/transform/NotYetImplementedASTTransformation.java;do
  iconv -f UTF-8 -t ASCII//TRANSLIT -o ${s}.tmp ${s} && mv ${s}.tmp ${s}
done

%{mvn_package} : %{name}-lib
%{mvn_file} : groovy %{name}

%{mvn_alias} : :groovy-all :%{name}-all :%{name}
%{mvn_compat_version} : "1.8" "1.8.9"

%build
mkdir -p target/lib/{compile,tools}

# Construct classpath
build-jar-repository target/lib/compile glassfish-servlet-api glassfish-jsp-api/javax.servlet.jsp-api \
        asm3/asm-tree asm3/asm \
        asm3/asm-util asm3/asm-analysis \
        antlr ant/ant-antlr antlr \
        bsf jline1/jline-1 xstream ant junit apache-ivy commons-cli \
        jansi

# Build
# TODO: Build at least tests, maybe examples
export CLASSPATH=$(build-classpath ant/ant-antlr)
ant -DskipTests=on -DskipExamples=on -DskipFetch=on -DskipEmbeddable=on \
        createJars javadoc

%install
%{mvn_artifact} pom.xml target/dist/groovy.jar
%mvn_install -J target/html/api/
%fdupes -s %{buildroot}%{_javadocdir}

# Startup scripts
install -d %{buildroot}%{_bindir}
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
for TOOL in grape18 %{name}c %{name}Console java2%{name} %{name}sh
do
        ln %{buildroot}%{_bindir}/%{name} \
                %{buildroot}%{_bindir}/$TOOL
done

# Configuration
install -d %{buildroot}%{_sysconfdir}
install -p -m644 %{SOURCE2} \
        %{buildroot}%{_sysconfdir}/%{name}-starter.conf

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}-starter.conf
%doc README.md
%license LICENSE.txt LICENSE-2.0.txt NOTICE.txt

%files lib -f .mfiles-%{name}-lib
%license LICENSE.txt LICENSE-2.0.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt LICENSE-2.0.txt NOTICE.txt

%changelog
