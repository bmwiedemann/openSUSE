#
# spec file for package slf4j2
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2000-2009, JPackage Project
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


%global base_name slf4j
%global version_suffix 2
Name:           %{base_name}%{version_suffix}
Version:        2.0.17
Release:        0
Summary:        Simple Logging Facade for Java
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://www.slf4j.org/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  ant >= 1.6.5
BuildRequires:  cal10n
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  javassist >= 3.4
BuildRequires:  reload4j
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%package jdk14
Summary:        SLF4J JDK14 Binding
Group:          Development/Libraries/Java

%description jdk14
SLF4J JDK14 Binding.

%package jdk-platform-logging
Summary:        SLF4J Platform Logging Binding
Group:          Development/Libraries/Java

%description jdk-platform-logging
SLF4J Platform Logging Binding.

%package reload4j
Summary:        SLF4J LOG4J-12 Binding
Group:          Development/Libraries/Java

%description reload4j
SLF4J LOG4J-12 Binding.

%package ext
Summary:        SLF4J Extensions Module
Group:          Development/Libraries/Java

%description ext
Extensions to the SLF4J API.

%package -n jcl-over-%{name}
Summary:        JCL 1.1.1 implemented over SLF4J
Group:          Development/Libraries/Java

%description -n jcl-over-%{name}
JCL 1.1.1 implemented over SLF4J.

%package -n jul-to-%{name}
Summary:        JUL to SLF4J bridge
Group:          Development/Libraries/Java

%description -n jul-to-%{name}
JUL to SLF4J bridge.

%package -n log4j-over-%{name}
Summary:        Log4j implemented over SLF4J
Group:          Development/Libraries/Java

%description -n log4j-over-%{name}
Log4j implemented over SLF4J.

%package migrator
Summary:        SLF4J Migrator
Group:          Development/Libraries/Java

%description migrator
SLF4J Migrator.

%prep
%setup -q -n %{base_name}-%{version} -a1
install -p -m 0644 %{SOURCE2} LICENSE-2.0.txt

%build
mkdir -p lib
build-jar-repository -s lib cal10n/cal10n-api javassist reload4j/reload4j

ant package javadoc

%install
install -d -m 0755 target/site/apidocs

for i in api ext jdk14 jdk-platform-logging migrator nop reload4j simple; do
  %{mvn_artifact} %{base_name}-${i}/pom.xml %{base_name}-${i}/target/%{base_name}-${i}-%{version}.jar
  cp -pr %{base_name}-${i}/target/site/apidocs target/site/apidocs/%{base_name}-${i}
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %{mvn_artifact} ${i}/pom.xml ${i}/target/${i}-%{version}.jar
  cp -pr ${i}/target/site/apidocs target/site/apidocs/${i}
done

%{mvn_compat_version} : %{version_suffix} %{version}

%{mvn_file} ':%{base_name}-{*}' %{base_name}/%{base_name}-@1 %{base_name}/@1

%{mvn_package} :::sources: __noinstall
%{mvn_package} :%{base_name}-bom __noinstall
%{mvn_package} :%{base_name}-parent __noinstall
%{mvn_package} :%{base_name}-site __noinstall
%{mvn_package} :%{base_name}-api
%{mvn_package} :%{base_name}-simple
%{mvn_package} :%{base_name}-nop
%{mvn_package} :%{base_name}-{*} @1
%{mvn_package} :{*} @1

%mvn_install

%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt LICENSE-2.0.txt

%files jdk14 -f .mfiles-jdk14

%files reload4j -f .mfiles-reload4j

%files ext -f .mfiles-ext

%files -n jcl-over-%{name} -f .mfiles-jcl-over-%{base_name}

%files -n log4j-over-%{name} -f .mfiles-log4j-over-%{base_name}

%files -n jul-to-%{name} -f .mfiles-jul-to-%{base_name}

%files jdk-platform-logging -f .mfiles-jdk-platform-logging

%files migrator -f .mfiles-migrator

%files javadoc -f .mfiles-javadoc

%changelog
