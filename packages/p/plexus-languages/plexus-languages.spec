#
# spec file for package plexus-languages
#
# Copyright (c) 2021 SUSE LLC
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


Name:           plexus-languages
Version:        1.0.3
Release:        0
Summary:        Plexus Languages
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-languages
# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh
Source100:      plexus-java-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
BuildRequires:  objectweb-asm
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  qdox >= 2
BuildRequires:  sisu-inject
Requires:       java >= 1.7
Requires:       mvn(com.thoughtworks.qdox:qdox)
Requires:       mvn(org.ow2.asm:asm)
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
%setup -q -n %{name}-%{name}-%{version}

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
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom
install -pm 0644 plexus-java/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/plexus-java.pom
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
