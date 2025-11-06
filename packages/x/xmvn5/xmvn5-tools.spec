#
# spec file for package xmvn5-tools
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


%global parent xmvn
%global version_suffix 5
%global subname tools
Name:           %{parent}%{version_suffix}-%{subname}
Version:        5.1.0
Release:        0
Summary:        Local Extensions for Apache Maven
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{parent}-%{version}.tar.xz
Source1:        %{parent}-build.tar.xz
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  kojan-xml
BuildRequires:  objectweb-asm
BuildRequires:  picocli
BuildRequires:  sisu-inject
BuildRequires:  slf4j2
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package -n %{parent}%{version_suffix}-api
Summary:        XMvn%{version_suffix} API
Group:          Development/Tools/Building

%description -n %{parent}%{version_suffix}-api
This package provides XMvn%{version_suffix} API module which contains public interface
for functionality implemented by XMvn%{version_suffix} Core.

%package -n %{parent}%{version_suffix}-core
Summary:        XMvn%{version_suffix} Core
Group:          Development/Tools/Building

%description -n %{parent}%{version_suffix}-core
This package provides XMvn%{version_suffix} Core module, which implements the essential
functionality of XMvn%{version_suffix} such as resolution of artifacts from system
repository.

%package -n %{parent}%{version_suffix}-resolve
Summary:        XMvn%{version_suffix} Resolver
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}%{version_suffix}-api = %{version}
Requires:       %{parent}%{version_suffix}-core = %{version}
Requires:       java >= 17
Requires:       javapackages-tools

%description -n %{parent}%{version_suffix}-resolve
This package provides XMvn%{version_suffix} Resolver, which is a very simple
command-line tool to resolve Maven artifacts from system repositories.
Basically it's just an interface to artifact resolution mechanism
implemented by XMvn%{version_suffix} Core.  The primary intended use case of XMvn
Resolver is debugging local artifact repositories.

%package -n %{parent}%{version_suffix}-subst
Summary:        XMvn%{version_suffix} Subst
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}%{version_suffix}-api = %{version}
Requires:       %{parent}%{version_suffix}-core = %{version}
Requires:       java >= 17
Requires:       javapackages-tools

%description -n %{parent}%{version_suffix}-subst
This package provides XMvn%{version_suffix} Subst, which is a tool that can substitute
Maven artifact files with symbolic links to corresponding files in
artifact repository.

%package -n %{parent}%{version_suffix}-install
Summary:        XMvn%{version_suffix} Install
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Group:          Development/Tools/Building
Requires:       %{parent}%{version_suffix}-api = %{version}
Requires:       %{parent}%{version_suffix}-core = %{version}
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       apache-commons-lang3
Requires:       java >= 17
Requires:       javapackages-tools
Requires:       kojan-xml
Requires:       objectweb-asm
Requires:       picocli
Requires:       slf4j2

%description -n %{parent}%{version_suffix}-install
This package provides XMvn%{version_suffix} Install, which is a command-line interface
to XMvn%{version_suffix} installer.  The installer reads reactor metadata and performs
artifact installation according to specified configuration.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

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
%pom_remove_plugin -r :spotless-maven-plugin

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

# Normalize slf4j version to 2
%pom_xpath_set pom:project/pom:properties/pom:slf4jVersion 2 xmvn-parent

%build
mkdir -p lib
build-jar-repository -s lib \
  apache-commons-lang3 \
  atinject \
  commons-compress \
  commons-io \
  kojan-xml/kojan-xml \
  objectweb-asm/asm \
  org.eclipse.sisu.inject \
  picocli/picocli \
  slf4j/api-2

ant -Dtest.skip=true package javadoc

%install
%{mvn_compat_version} : %{version_suffix} %{version}
%{mvn_file} :{*} %{parent}/@1

%{mvn_package} :%{parent}-tools __noinstall
%{mvn_package} :%{parent}-{*} @1

%{mvn_artifact} %{parent}-tools/pom.xml
install -dm 0755 target/site/apidocs
for i in api core; do
  %{mvn_artifact} %{parent}-${i}/pom.xml %{parent}-${i}/target/%{parent}-${i}-%{version}.jar
  cp -pr %{parent}-${i}/target/site/apidocs target/site/apidocs/${i}
done
for i in install resolve subst; do
  %{mvn_artifact} %{parent}-tools/%{parent}-${i}/pom.xml %{parent}-tools/%{parent}-${i}/target/%{parent}-${i}-%{version}.jar
  cp -pr %{parent}-tools/%{parent}-${i}/target/site/apidocs target/site/apidocs/${i}
done

%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# helper scripts
%jpackage_script org.fedoraproject.xmvn.tools.install.cli.InstallerCli "" "" %{parent}/%{parent}-install-%{version_suffix}:%{parent}/%{parent}-api-%{version_suffix}:%{parent}/%{parent}-core-%{version_suffix}:slf4j/api-2:slf4j/simple-2:objectweb-asm/asm:commons-compress:commons-io:apache-commons-lang3:picocli/picocli:kojan-xml/kojan-xml %{parent}%{version_suffix}-install
%jpackage_script org.fedoraproject.xmvn.tools.resolve.ResolverCli "" "" %{parent}/%{parent}-resolve-%{version_suffix}:%{parent}/%{parent}-api-%{version_suffix}:%{parent}/%{parent}-core-%{version_suffix}:picocli/picocli:kojan-xml/kojan-xml %{parent}%{version_suffix}-resolve
%jpackage_script org.fedoraproject.xmvn.tools.subst.SubstCli "" "" %{parent}/%{parent}-subst-%{version_suffix}:%{parent}/%{parent}-api-%{version_suffix}:%{parent}/%{parent}-core-%{version_suffix}:picocli/picocli:kojan-xml/kojan-xml %{parent}%{version_suffix}-subst

%files -n %{parent}%{version_suffix}-core -f .mfiles-core

%files -n %{parent}%{version_suffix}-api -f .mfiles-api
%license LICENSE NOTICE
%doc AUTHORS README.md

%files -n %{parent}%{version_suffix}-resolve -f .mfiles-resolve
%{_bindir}/%{parent}%{version_suffix}-resolve

%files -n %{parent}%{version_suffix}-subst -f .mfiles-subst
%{_bindir}/%{parent}%{version_suffix}-subst

%files -n %{parent}%{version_suffix}-install -f .mfiles-install
%{_bindir}/%{parent}%{version_suffix}-install

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
