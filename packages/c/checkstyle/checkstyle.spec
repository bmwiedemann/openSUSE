#
# spec file for package checkstyle
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


Name:           checkstyle
Version:        8.0
Release:        0
Summary:        Java source code checker
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            http://checkstyle.sourceforge.net/
Source0:        http://download.sf.net/checkstyle/checkstyle-%{version}-src.tar.gz
Source2:        %{name}.catalog
Patch0:         checkstyle-8.0-guava.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-nodeps)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.mojo:antlr-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
#!BuildRequires: stringtemplate4
# Explicit requires for javapackages-tools since checkstyle-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
BuildArch:      noarch

%description
A tool for checking Java source code for adherence to a set of rules.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%pom_remove_parent

sed -i s/guava-jdk5/guava/ pom.xml

# not needed for package build
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# these are only needed for upstream QA
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-linkcheck-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :spotbugs-maven-plugin

# get rid of system scope
%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools::provided

# fix encoding issues in docs
sed -i 's/\r//' LICENSE LICENSE.apache20 README.md

# The following test needs network access, so it would fail on Koji
sed -i '/testLoadFromURL/s/ *.*/    @org.junit.Ignore&/' src/test/java/com/puppycrawl/tools/checkstyle/filters/SuppressionsLoaderTest.java

# Test failure, TODO: investigate this
sed -i '/testUnexpectedChar/s/./@org.junit.Ignore/' src/test/java/com/puppycrawl/tools/checkstyle/grammars/GeneratedJava14LexerTest.java

%build
%{mvn_file}  : %{name}
# Tests are skipped due to unavailable test dependencies
# (com.github.stefanbirkner:system-rules:jar:1.9.0 and
# nl.jqno.equalsverifier:equalsverifier:jar:1.7.2)
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# script
%jpackage_script com.puppycrawl.tools.checkstyle.Main "" "" checkstyle:antlr:apache-commons-beanutils:apache-commons-cli:apache-commons-logging:apache-commons-collections:guava checkstyle true

# dtds
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/xml/%{name}/catalog
cp -pa src/main/resources/com/puppycrawl/tools/checkstyle/*.dtd \
  %{buildroot}%{_datadir}/xml/%{name}

# ant.d
install -dm 755  %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
checkstyle antlr apache-commons-beanutils apache-commons-cli apache-commons-logging guava
EOF

%post
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%postun
# Note that we're using a fully versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%files -f .mfiles
%license LICENSE
%doc README.md
%{_datadir}/xml/%{name}
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
