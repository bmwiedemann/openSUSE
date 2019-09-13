#
# spec file for package avalon-framework
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           avalon-framework
Version:        4.3
Release:        0
Summary:        Java components interfaces
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://avalon.apache.org/
Source0:        http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-api-%{version}-src.tar.gz
Source1:        http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-impl-%{version}-src.tar.gz
Patch0:         0001-Port-build-script-to-Maven-3.patch
Patch1:         %{name}-manifest.patch
BuildRequires:  ant
BuildRequires:  avalon-logkit
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  log4j
Requires:       mvn(avalon-logkit:avalon-logkit)
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
Provides:       %{name}-manual = %{version}-%{release}
Obsoletes:      %{name}-manual < %{version}-%{release}

%description javadoc
API documentation for %{name}.

%prep
%setup -qcT -a 0 -a 1
%patch0 -p1
%patch1 -p1

%build
pushd %{name}-api-%{version}
  mkdir -p target/lib
  build-jar-repository -s target/lib avalon-logkit
  %ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist
popd
pushd %{name}-impl-%{version}
  mkdir -p target/lib
  build-jar-repository -s target/lib avalon-logkit log4j commons-logging
  cp ../%{name}-api-%{version}/target/*.jar target/lib/
  %ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}-api-%{version}/dist/%{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -pm 0644 %{name}-impl-%{version}/dist/%{name}-impl-%{version}.jar %{buildroot}%{_javadir}/%{name}-impl.jar
(cd %{buildroot}%{_javadir} && ln -s %{name}-impl.jar %{name}.jar)
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{name}-api-%{version}/project.xml %{buildroot}%{_mavenpomdir}/%{name}-api.pom
%add_maven_depmap %{name}-api.pom %{name}-api.jar -a org.apache.avalon.framework:avalon-framework-api
install -pm 0644 %{name}-impl-%{version}/project.xml %{buildroot}%{_mavenpomdir}/%{name}-impl.pom
%add_maven_depmap %{name}-impl.pom %{name}-impl.jar -a org.apache.avalon.framework:avalon-framework-impl
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr %{name}-api-%{version}/dist/docs/api %{buildroot}%{_javadocdir}/%{name}/api
cp -pr %{name}-impl-%{version}/dist/docs/api %{buildroot}%{_javadocdir}/%{name}/impl
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}.jar
%license avalon-framework-api-4.3/LICENSE.txt
%license avalon-framework-api-4.3/NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%license avalon-framework-api-4.3/LICENSE.txt
%license avalon-framework-api-4.3/NOTICE.txt

%changelog
