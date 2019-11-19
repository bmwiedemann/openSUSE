#
# spec file for package eclipse-jgit
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global gittag 5.1.3.201810200350-r
Version:        5.1.3
Release:        0
Summary:        Eclipse JGit
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/egit/
# Use github mirror for now, see: https://bugs.eclipse.org/bugs/show_bug.cgi?id=522144
Source0:        https://github.com/eclipse/jgit/archive/v%{gittag}/jgit-v%{gittag}.tar.gz
Patch0:         fix_jgit_sh.patch
# Change how feature deps are specified, to avoid embedding versions
Patch1:         jgit-feature-deps.patch
# For main build
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.javaewah:JavaEWAH)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-continuation)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.tukaani:xz)
BuildConflicts: java-devel >= 9
BuildArch:      noarch
%if %{with bootstrap}
Name:           eclipse-jgit-bootstrap
%else
Name:           eclipse-jgit
# For building the eclipse features
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  jgit-bootstrap = %{version}
BuildRequires:  tycho
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  jgit
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: log4j eclipse-emf-core eclipse-ecf-core
Requires:       eclipse-platform
Requires:       jgit = %{version}-%{release}
Requires:       jzlib
%endif

%description
A pure Java implementation of the Git version control system.

%package -n     jgit-javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description -n jgit-javadoc
%{summary}.

%if %{with bootstrap}
%package -n     jgit-bootstrap
%else
%package -n     jgit
Obsoletes:      jgit-bootstrap
%endif
Summary:        Java-based command line Git interface
Group:          Development/Libraries/Java

%if %{with bootstrap}
%description -n jgit-bootstrap
%else
%description -n jgit
%endif
Command line Git tool built entirely in Java.

%prep
%setup -q -n jgit-%{gittag}

%patch0
%patch1

# Disable multithreaded build
rm .mvn/maven.config

# Javaewah change
sed -i -e "s/javaewah/com.googlecode.javaewah.JavaEWAH/g" org.eclipse.jgit.packaging/org.eclipse.jgit{,.pgm}.feature/feature.xml

# Don't try to get deps from local *maven* repo, use tycho resolved ones
%pom_remove_dep com.googlecode.javaewah:JavaEWAH
for p in $(find org.eclipse.jgit.packaging -name pom.xml) ; do
  grep -q dependencies $p && %pom_xpath_remove "pom:dependencies" $p
done

# Disable "errorprone" compiler
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='compile-with-errorprone']" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution[pom:id='default-compile']/pom:configuration" pom.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:dependencies" pom.xml

# Don't need target platform or repository modules with xmvn
%pom_disable_module org.eclipse.jgit.target org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.repository org.eclipse.jgit.packaging
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target" org.eclipse.jgit.packaging/pom.xml

# Don't build source features
%pom_disable_module org.eclipse.jgit.source.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.pgm.source.feature org.eclipse.jgit.packaging

# Use newer Felix dep
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# Remove unnecessary plugins for RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-enforcer-plugin org.eclipse.jgit.packaging
%pom_remove_plugin -r :japicmp-maven-plugin

# Don't attach shell script artifact
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin org.eclipse.jgit.pgm

# Remove org.apache.log4j
%pom_remove_dep log4j:log4j . org.eclipse.jgit.pgm
%pom_change_dep org.slf4j:slf4j-log4j12 org.slf4j:slf4j-simple . org.eclipse.jgit.pgm

# org.slf4j.api -> slf4j.api
# org.slf4j.impl.log4j12 -> slf4j.simple
sed -i 's/org\.slf4j\.api/slf4j\.api/
        s/org\.slf4j\.impl\.log4j12/slf4j\.simple/' \
org.eclipse.jgit.packaging/org.eclipse.jgit.feature/feature.xml

pushd org.eclipse.jgit.packaging
%{mvn_package} "::pom::" __noinstall
popd
%{mvn_package} ":*.test" __noinstall

%build
# Due to a current limitation of Tycho it is not possible to mix pom-first and
# manifest-first builds in the same reactor build hence two separate invocations

%if %{with bootstrap}
%global no_javadoc "-j"
%else
%global no_javadoc %{nil}
%endif
# First invocation installs jgit so the second invocation will succeed
# One test always fails "RacyGitTests.testRacyGitDetection" so ignore failures for now
%{mvn_build} --post install:install -f %{no_javadoc} -- -Pjavac \
  -Dmaven.repo.local=$(pwd)/org.eclipse.jgit.packaging/.m2 -Dmaven.test.failure.ignore=true

# Second invocation builds the eclipse features
%if %{without bootstrap}
pushd org.eclipse.jgit.packaging
%{mvn_build} -j -f -- -Dfedora.p2.repos=$(pwd)/.m2
popd
%endif

%install
# The macro does not allow us to change the "namespace" value, but here we want to
# set it to something other than the SRPM name, so explode the macro
xmvn-install -R .xmvn-reactor -n jgit -d %{buildroot}
%if %{without bootstrap}
install -dm755 %{buildroot}%{_javadocdir}/jgit
cp -pr .xmvn/apidocs/* %{buildroot}%{_javadocdir}/jgit
echo '%{_javadocdir}/jgit' >>.mfiles-javadoc

pushd org.eclipse.jgit.packaging
%mvn_install
popd
%endif

# Binary
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

# Ant task configuration
install -dm 755 %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/jgit <<EOF
javaewah jzlib jsch jgit/org.eclipse.jgit jgit/org.eclipse.jgit.ant slf4j/slf4j-api slf4j/slf4j-simple httpcomponents/httpcore httpcomponents/httpclient commons-logging commons-codec
EOF

%fdupes -s %{buildroot}%{_javadocdir}

%if %{without bootstrap}
%files -f org.eclipse.jgit.packaging/.mfiles
%license LICENSE
%doc README.md

%files -n jgit -f .mfiles
%else
%files -n jgit-bootstrap -f .mfiles
%endif
%license LICENSE
%doc README.md
%{_bindir}/jgit
%config(noreplace) %{_sysconfdir}/ant.d/jgit

%if %{without bootstrap}
%files -n jgit-javadoc -f .mfiles-javadoc
%license LICENSE
%endif

%changelog
