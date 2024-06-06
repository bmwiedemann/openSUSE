#
# spec file for package sisu
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


%global reltype milestones
Name:           sisu
Version:        0.9.0.M3
Release:        0
Summary:        Eclipse dependency injection framework
License:        BSD-3-Clause AND EPL-1.0 AND EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/sisu/
Source0:        https://github.com/eclipse-sisu/sisu-project/archive/refs/tags/%{reltype}/%{version}.tar.gz#/sisu-project-%{version}.tar.gz
Source1:        %{name}-build.tar.xz
Patch1:         sisu-no-dependency-on-glassfish-servlet-api.patch
Patch3:         sisu-osgi-api.patch
Patch4:         sisu-reproducible-index.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  cdi-api
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  google-guice
BuildRequires:  guice-servlet
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
BuildRequires:  junit5-minimal
BuildRequires:  osgi-core
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  slf4j
BuildRequires:  testng
BuildRequires:  unzip
BuildRequires:  xz
Provides:       bundled(objectweb-asm)
BuildArch:      noarch

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        inject
Summary:        Sisu inject
Group:          Development/Libraries/Java

%description    inject
This package contains %{summary}.

%package        plexus
Summary:        Sisu Plexus
Group:          Development/Libraries/Java
Requires:       %{name}-inject = %{version}
Obsoletes:      plexus-containers-container-default < 2.2.0
Provides:       plexus-containers-container-default = 2.2.0

%description    plexus
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu
Group:          Documentation/HTML

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -n sisu-project-%{reltype}-%{version} -a1

%patch -P 1 -p1
%patch -P 3 -p1
%patch -P 4 -p2

%build
mkdir -p lib
build-jar-repository -s lib \
  glassfish-annotation-api \
  google-guice-no_aop \
  javax.enterprise.inject/cdi-api \
  javax.inject/atinject \
  junit \
  junit5 \
  osgi-core/osgi.core \
  plexus/utils \
  plexus/xml \
  plexus/classworlds \
  plexus-containers/plexus-component-annotations \
  slf4j/api \
  testng
%{ant} package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 org.eclipse.sisu.inject/target/org.eclipse.sisu.inject-%{version}.jar \
    %{buildroot}%{_javadir}/org.eclipse.sisu.inject.jar
install -pm 0644 org.eclipse.sisu.plexus/target/org.eclipse.sisu.plexus-%{version}.jar \
    %{buildroot}%{_javadir}/org.eclipse.sisu.plexus.jar
# Compatibility symlink
install -dm 0755 %{buildroot}%{_javadir}/plexus-containers
ln -sf %{_javadir}/org.eclipse.sisu.plexus.jar %{buildroot}%{_javadir}/plexus-containers/plexus-container-default.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} org.eclipse.sisu.inject/pom.xml %{buildroot}%{_mavenpomdir}/org.eclipse.sisu.inject.pom
%add_maven_depmap org.eclipse.sisu.inject.pom org.eclipse.sisu.inject.jar -f inject
%{mvn_install_pom} org.eclipse.sisu.plexus/pom.xml %{buildroot}%{_mavenpomdir}/org.eclipse.sisu.plexus.pom
%add_maven_depmap org.eclipse.sisu.plexus.pom org.eclipse.sisu.plexus.jar -f plexus -a org.sonatype.sisu:sisu-inject-plexus,org.codehaus.plexus:plexus-container-default

# javadoc
for i in inject plexus; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  cp -pr org.eclipse.sisu.${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files inject -f .mfiles-inject
%license LICENSE.txt

%files plexus -f .mfiles-plexus
%{_javadir}/plexus-containers

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
