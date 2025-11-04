#
# spec file for package plexus-testing
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


%bcond_with tests
Name:           plexus-testing
Version:        2.0.1
Release:        0
Summary:        Plexus Testing
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-testing
Source0:        %{name}-%{version}.tar.xz
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apiguardian
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit5
BuildRequires:  sisu-plexus
BuildRequires:  xz
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit5
BuildRequires:  atinject
BuildRequires:  guava
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-utils
BuildRequires:  sisu-inject
%endif

%description
Library to help testing plexus components

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
cp -p %{SOURCE100} build.xml

mkdir -p lib
build-jar-repository -s lib \
%if %{with tests}
    atinject \
    guava/guava \
    junit5/junit-jupiter-engine \
    org.eclipse.sisu.inject \
    plexus-classworlds \
    plexus-containers/plexus-component-annotations \
    plexus/utils \
%endif
    apiguardian/apiguardian-api \
    guice/google-guice \
    junit5/junit-jupiter-api \
    org.eclipse.sisu.plexus \

%build
ant \
%if %{without tests}
  -Dtest.skip=true \
%endif
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/testing.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/testing.pom
%add_maven_depmap plexus/testing.pom plexus/testing.jar
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
