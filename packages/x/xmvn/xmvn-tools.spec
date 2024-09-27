#
# spec file for package xmvn-tools
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


%global parent xmvn
%global subname tools
Name:           %{parent}-%{subname}
Version:        4.3.0
Release:        0
Summary:        Local Extensions for Apache Maven
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        https://github.com/fedora-java/xmvn/releases/download/%{version}/%{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  atinject
BuildRequires:  beust-jcommander >= 1.82
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildArch:      noarch

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package -n %{parent}-api
Summary:        XMvn API
Group:          Development/Tools/Building

%description -n %{parent}-api
This package provides XMvn API module which contains public interface
for functionality implemented by XMvn Core.

%package -n %{parent}-core
Summary:        XMvn Core
Group:          Development/Tools/Building

%description -n %{parent}-core
This package provides XMvn Core module, which implements the essential
functionality of XMvn such as resolution of artifacts from system
repository.

%package -n %{parent}-resolve
Summary:        XMvn Resolver
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}-api = %{version}
Requires:       %{parent}-core = %{version}
Requires:       beust-jcommander >= 1.82
Requires:       javapackages-tools

%description -n %{parent}-resolve
This package provides XMvn Resolver, which is a very simple
command-line tool to resolve Maven artifacts from system repositories.
Basically it's just an interface to artifact resolution mechanism
implemented by XMvn Core.  The primary intended use case of XMvn
Resolver is debugging local artifact repositories.

%package -n %{parent}-subst
Summary:        XMvn Subst
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}-api = %{version}
Requires:       %{parent}-core = %{version}
Requires:       beust-jcommander
Requires:       javapackages-tools

%description -n %{parent}-subst
This package provides XMvn Subst, which is a tool that can substitute
Maven artifact files with symbolic links to corresponding files in
artifact repository.

%package -n %{parent}-install
Summary:        XMvn Install
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}-api = %{version}
Requires:       %{parent}-core = %{version}
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       beust-jcommander
Requires:       javapackages-tools
Requires:       objectweb-asm
Requires:       slf4j

%description -n %{parent}-install
This package provides XMvn Install, which is a command-line interface
to XMvn installer.  The installer reads reactor metadata and performs
artifact installation according to specified configuration.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
Obsoletes:      javadoc

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{parent}-%{version} -a1

%autopatch -p1

# Resolver IT won't work either - it tries to execute JAR file, which
# relies on Class-Path in manifest, which is forbidden in Fedora...
find -name ResolverIntegrationTest.java -delete

%pom_remove_plugin -r :maven-site-plugin

# Upstream code quality checks, not relevant when building RPMs
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
# FIXME pom macros don't seem to support submodules in profile
%pom_remove_plugin :jacoco-maven-plugin xmvn-it

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

# This test depends on OpenJDK directory layout that changed since version 9
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
rm -f xmvn-core/src/test/java/org/fedoraproject/xmvn/resolver/JavaHomeResolverTest.java
%endif

%build
mkdir -p lib
build-jar-repository -s lib \
  atinject \
  beust-jcommander \
  commons-compress \
  commons-io \
  objectweb-asm/asm \
  org.eclipse.sisu.inject \
  org.eclipse.sisu.plexus \
  slf4j/api

%{ant} -Dtest.skip=true package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{parent}
for i in api core; do
  install -pm 0644 %{parent}-${i}/target/%{parent}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{parent}/%{parent}-${i}.jar
done
for i in install resolve subst; do
  install -pm 0644 %{parent}-tools/%{parent}-${i}/target/%{parent}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{parent}/%{parent}-${i}.jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{parent}
for i in api core; do
  %{mvn_install_pom} %{parent}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{parent}/%{parent}-${i}.pom
  %add_maven_depmap %{parent}/%{parent}-${i}.pom %{parent}/%{parent}-${i}.jar -f ${i}
done
for i in install resolve subst; do
  %{mvn_install_pom} %{parent}-tools/%{parent}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{parent}/%{parent}-${i}.pom
  %add_maven_depmap %{parent}/%{parent}-${i}.pom %{parent}/%{parent}-${i}.jar -f ${i}
done

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{parent}
for i in api core; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{parent}/${i}
  cp -pr %{parent}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{parent}/${i}/
done
for i in install resolve subst; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{parent}/${i}
  cp -pr %{parent}-tools/%{parent}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{parent}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

# helper scripts
%jpackage_script org.fedoraproject.xmvn.tools.install.cli.InstallerCli "" "" %{parent}/%{parent}-install:%{parent}/%{parent}-api:%{parent}/%{parent}-core:beust-jcommander:slf4j/api:slf4j/simple:objectweb-asm/asm:commons-compress:commons-io %{parent}-install
%jpackage_script org.fedoraproject.xmvn.tools.resolve.ResolverCli "" "" %{parent}/%{parent}-resolve:%{parent}/%{parent}-api:%{parent}/%{parent}-core:beust-jcommander %{parent}-resolve
%jpackage_script org.fedoraproject.xmvn.tools.subst.SubstCli "" "" %{parent}/%{parent}-subst:%{parent}/%{parent}-api:%{parent}/%{parent}-core:beust-jcommander %{parent}-subst

%files -n %{parent}-core -f .mfiles-core

%files -n %{parent}-api -f .mfiles-api
%license LICENSE NOTICE
%doc AUTHORS README.md

%files -n %{parent}-resolve -f .mfiles-resolve
%{_bindir}/%{parent}-resolve

%files -n %{parent}-subst -f .mfiles-subst
%{_bindir}/%{parent}-subst

%files -n %{parent}-install -f .mfiles-install
%{_bindir}/%{parent}-install

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{parent}

%changelog
