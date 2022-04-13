#
# spec file for package reload4j
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


%bcond_with tests
Name:           reload4j
Version:        1.2.20
Release:        0
Summary:        Revival of EOLed log4j 1.x
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://reload4j.qos.ch/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         %{name}-java1.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  geronimo-jms-1_1-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-local
Obsoletes:      chainsaw < 2.1
Obsoletes:      log4j < 1.3
Obsoletes:      log4j-mini < 1.3
Obsoletes:      log4j12 < %{version}
Obsoletes:      log4j12-mini < %{version}
Obsoletes:      logfactor5 < %{version}
Provides:       log4j12 = %{version}
Provides:       log4j12-mini = %{version}
Provides:       mvn(log4j:log4j:1.2.12) = %{version}
Provides:       mvn(log4j:log4j:1.2.14) = %{version}
Provides:       mvn(log4j:log4j:1.2.16) = %{version}
Provides:       mvn(log4j:log4j:1.2.17) = %{version}
Provides:       mvn(log4j:log4j:12) = %{version}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  geronimo-jaf-1_0_2-api
BuildRequires:  h2database
%endif

%description
The reload4j project is a fork of Apache log4j version 1.2.17
in order to fix most pressing security issues. It is intended
as a drop-in replacement for log4j version 1.2.17; replacement
of log4j.jar with reload4j.jar in a build without needing to
make changes to source code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Obsoletes:      log4j12-javadoc < %{version}
Obsoletes:      log4j12-manual < %{version}
Provides:       log4j12-javadoc = %{version}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} build.xml
mkdir -p lib

%build
build-jar-repository -s lib javamail geronimo-jms-1.1-api
%if %{with tests}
build-jar-repository -s lib geronimo-jaf-1.0.2-api h2database
%endif

%{ant} \
%if %{without tests}
        -Dtest.skip=true \
%endif
        package javadoc

%install
# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -a target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
mkdir -p %{buildroot}%{_javadir}/log4j12
for i in log4j-1.2.12 log4j-1.2.13 log4j-1.2.14 log4j-1.2.15 log4j-1.2.16 log4j-1.2.17 log4j-12; do
  ln -sf ../%{name}/%{name}.jar %{buildroot}%{_javadir}/log4j12/${i}.jar
done

#pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar -a log4j:log4j

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/log4j12
%license LICENSE
%doc NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
