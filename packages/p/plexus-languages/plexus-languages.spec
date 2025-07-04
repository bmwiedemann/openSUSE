#
# spec file for package plexus-languages
#
# Copyright (c) 2025 SUSE LLC
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           plexus-languages
Version:        1.5.0
Release:        0
Summary:        Plexus Languages
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-languages
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      plexus-java-build.xml
Patch0:         plexus-languages-atinject.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  objectweb-asm
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  qdox >= 2
BuildRequires:  sisu-inject
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

cp %{SOURCE1} .
cp %{SOURCE100} plexus-java/build.xml

%pom_xpath_inject "pom:project" "<groupId>org.codehaus.plexus</groupId>" .
%pom_remove_parent .
%pom_xpath_remove pom:project/pom:profiles plexus-java

%build
mkdir -p lib
build-jar-repository -s lib qdox javax.inject plexus-containers/plexus-component-annotations objectweb-asm/asm org.eclipse.sisu.inject
pushd plexus-java
%{ant} -Dtest.skip=true package javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 plexus-java/target/plexus-java-%{version}.jar %{buildroot}%{_javadir}/%{name}/plexus-java.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} plexus-java/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/plexus-java.pom
%add_maven_depmap %{name}/plexus-java.pom %{name}/plexus-java.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/plexus-java
cp -pr plexus-java/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/plexus-java/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc
%license LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
