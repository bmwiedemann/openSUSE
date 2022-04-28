#
# spec file for package sisu
#
# Copyright (c) 2022 SUSE LLC
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


%global reltype release
Name:           sisu
Version:        0.3.5
Release:        0
Summary:        Eclipse dependency injection framework
# sisu is EPL-1.0, bundled asm is BSD
License:        BSD-3-Clause AND EPL-1.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/sisu/
Source0:        https://github.com/eclipse/sisu.inject/archive/refs/tags/releases/%{version}.tar.gz#/sisu-inject-%{version}.tar.gz
Source1:        https://github.com/eclipse/sisu.plexus/archive/refs/tags/releases/%{version}.tar.gz#/sisu-plexus-%{version}.tar.gz
Source2:        %{name}-build.tar.xz
Source100:      %{name}-inject.pom
Source101:      %{name}-plexus.pom
Patch0:         %{name}-OSGi-import-guava.patch
Patch1:         %{name}-no-dependency-on-glassfish-servlet-api.patch
Patch2:         %{name}-ignored-tests.patch
Patch3:         %{name}-osgi-api.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  cdi-api
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  google-guice
BuildRequires:  guice-servlet
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  osgi-core
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
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
Requires:       mvn(javax.enterprise:cdi-api)

%description    inject
This package contains %{summary}.

%package        plexus
Summary:        Sisu Plexus
Group:          Development/Libraries/Java
Requires:       mvn(org.codehaus.plexus:plexus-classworlds)
Requires:       mvn(org.codehaus.plexus:plexus-component-annotations)
Requires:       mvn(org.codehaus.plexus:plexus-utils)
Requires:       mvn(org.eclipse.sisu:org.eclipse.sisu.inject) = %{version}

%description    plexus
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu
Group:          Documentation/HTML

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -c -T
tar xf %{SOURCE0} && mv sisu.inject-releases-%{version} sisu-inject
tar xf %{SOURCE1} && mv sisu.plexus-releases-%{version} sisu-plexus
tar xf %{SOURCE2}

cp %{SOURCE100} sisu-inject/pom.xml
cp %{SOURCE101} sisu-plexus/pom.xml

%patch0
%patch1
%patch2
%patch3

%pom_remove_dep :servlet-api sisu-inject

for i in inject plexus; do
  %pom_xpath_set -r /pom:project/pom:version %{version} %{name}-${i}
  %pom_remove_dep :::provided: %{name}-${i}
  %pom_xpath_remove pom:project/pom:build %{name}-${i}
done
%pom_change_dep :org.eclipse.sisu.inject org.eclipse.sisu:org.eclipse.sisu.inject:%{version} %{name}-plexus

%build
mkdir -p lib
build-jar-repository -s lib \
  glassfish-annotation-api \
  google-guice-no_aop \
  guice/guice-servlet \
  javax.enterprise.inject/cdi-api \
  javax.inject/atinject \
  junit \
  osgi-core/osgi.core \
  plexus/utils \
  plexus/classworlds \
  plexus-containers/plexus-component-annotations \
  slf4j/api \
  testng
%{ant} package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}-inject/target/org.eclipse.sisu.inject-%{version}.jar %{buildroot}%{_javadir}/org.eclipse.sisu.inject.jar
install -pm 0644 %{name}-plexus/target/org.eclipse.sisu.plexus-%{version}.jar %{buildroot}%{_javadir}/org.eclipse.sisu.plexus.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{name}-inject/pom.xml %{buildroot}%{_mavenpomdir}/org.eclipse.sisu.inject.pom
%add_maven_depmap org.eclipse.sisu.inject.pom org.eclipse.sisu.inject.jar -f inject
install -pm 0644 %{name}-plexus/pom.xml %{buildroot}%{_mavenpomdir}/org.eclipse.sisu.plexus.pom
%add_maven_depmap org.eclipse.sisu.plexus.pom org.eclipse.sisu.plexus.jar -f plexus -a org.sonatype.sisu:sisu-inject-plexus

# javadoc
for i in inject plexus; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{name}-${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}

%files inject -f .mfiles-inject
%license sisu-inject/LICENSE.txt

%files plexus -f .mfiles-plexus

%files javadoc
%license sisu-inject/LICENSE.txt
%{_javadocdir}/%{name}

%changelog
