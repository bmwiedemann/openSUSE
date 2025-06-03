#
# spec file for package plexus-sec-dispatcher
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


Name:           plexus-sec-dispatcher
Version:        2.0
Release:        0
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{name}
Source0:        https://github.com/codehaus-plexus/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm
BuildRequires:  plexus-cipher
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildArch:      noarch

%description
Plexus Security Dispatcher Component

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} .
cp %{SOURCE100} build.xml

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0

%build
mkdir -p lib
build-jar-repository -s lib \
    plexus/utils \
    plexus/xml \
    plexus/plexus-cipher \
    org.eclipse.sisu.inject \
    objectweb-asm/asm \
    javax.inject
%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/%{name}.pom
%add_maven_depmap plexus/%{name}.pom plexus/%{name}.jar -a org.sonatype.plexus:%{name}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc
%license LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
