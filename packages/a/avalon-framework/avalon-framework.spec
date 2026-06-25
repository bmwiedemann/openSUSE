#
# spec file for package avalon-framework
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global base_name avalon-framework
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "api"
%global build_api 1
Name:           %{base_name}-api
%else
%global build_api 0
Name:           %{base_name}
BuildRequires:  %{base_name}-api
BuildRequires:  commons-logging
%endif
Version:        4.3
Release:        0
Summary:        Java components interfaces
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://avalon.apache.org/
Source0:        https://archive.apache.org/dist/excalibur/excalibur-framework/source/%{base_name}-api-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/excalibur/excalibur-framework/source/%{base_name}-impl-%{version}-src.tar.gz
Patch0:         0001-Port-build-script-to-Maven-3.patch
Patch1:         %{base_name}-manifest.patch
BuildRequires:  ant
BuildRequires:  avalon-logkit
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  reload4j
BuildArch:      noarch

%description
The Avalon framework consists of interfaces that define relationships
between commonly used application components, best-of-practice pattern
enforcements, and several lightweight convenience implementations of the
generic components.
What that means is that we define the central interface Component. We
also define the relationship (contract) a component has with peers,
ancestors and children.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
%if ! %{build_api}
Requires:       %{base_name}-api-javadoc
Provides:       %{name}-manual = %{version}-%{release}
Obsoletes:      %{name}-manual < %{version}-%{release}
%endif

%description javadoc
API documentation for %{name}.

%prep
%setup -q -cT -a 0 -a 1
%autopatch -p1

%build
%if %{build_api}
pushd %{base_name}-api-%{version}
  mkdir -p target/lib
  build-jar-repository -s target/lib avalon-logkit
  ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist
popd
%else
pushd %{base_name}-impl-%{version}
  mkdir -p target/lib
  build-jar-repository -s target/lib avalon-logkit reload4j commons-logging %{base_name}-api
  ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist
popd
%endif

%install
%if %{build_api}
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{base_name}-api-%{version}/dist/%{base_name}-api-%{version}.jar %{buildroot}%{_javadir}/%{base_name}-api.jar
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{base_name}-api-%{version}/project.xml %{buildroot}%{_mavenpomdir}/%{base_name}-api.pom
%add_maven_depmap %{base_name}-api.pom %{base_name}-api.jar -a org.apache.avalon.framework:avalon-framework-api
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{base_name}
cp -pr %{base_name}-api-%{version}/dist/docs/api %{buildroot}%{_javadocdir}/%{base_name}/api
%fdupes -s %{buildroot}%{_javadocdir}
%else
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{base_name}-impl-%{version}/dist/%{base_name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{base_name}-impl.jar
(cd %{buildroot}%{_javadir} && ln -s %{base_name}-impl.jar %{base_name}.jar)
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{base_name}-impl-%{version}/project.xml %{buildroot}%{_mavenpomdir}/%{base_name}-impl.pom
%add_maven_depmap %{base_name}-impl.pom %{base_name}-impl.jar -a "org.apache.avalon.framework:avalon-framework-impl","avalon-framework:avalon-framework"
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{base_name}
cp -pr %{base_name}-impl-%{version}/dist/docs/api %{buildroot}%{_javadocdir}/%{base_name}/impl
%fdupes -s %{buildroot}%{_javadocdir}
%endif

%files -f .mfiles
%if ! %{build_api}
%{_javadir}/%{base_name}.jar
%endif
%license avalon-framework-api-4.3/LICENSE.txt
%license avalon-framework-api-4.3/NOTICE.txt

%files javadoc
%{_javadocdir}/%{base_name}
%license avalon-framework-api-4.3/LICENSE.txt
%license avalon-framework-api-4.3/NOTICE.txt

%changelog
