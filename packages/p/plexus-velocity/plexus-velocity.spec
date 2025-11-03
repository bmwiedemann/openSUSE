#
# spec file for package plexus-velocity
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


Name:           plexus-velocity
Version:        2.3.0
Release:        0
Summary:        Plexus Velocity Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://codehaus-plexus.github.io/plexus-velocity/
Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  ant
BuildRequires:  apache-commons-collections
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  velocity-engine-core
BuildArch:      noarch

%description
This package provides Plexus Velocity component - a wrapper for
Apache Velocity template engine, which allows easy use of Velocity
by applications built on top of Plexus container.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.jar' -delete

cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} LICENSE

mkdir -p lib
build-jar-repository -s lib \
    atinject \
    commons-collections \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    velocity-engine/velocity-engine-core

%build
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
