#
# spec file for package slf4j
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           slf4j
Version:        2.0.18
Release:        0
Summary:        Simple Logging Facade for Java
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://www.slf4j.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  ant >= 1.6.5
BuildRequires:  cal10n
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  javassist >= 3.4
BuildRequires:  reload4j
Obsoletes:      %{name}2
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

%package bom
Summary:        SLF4J BOM
Group:          Development/Libraries/Java

%description bom
SLF4J project BOM

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Obsoletes:      %{name}2-javadoc

%description javadoc
API documentation for %{name}.

%package jdk14
Summary:        SLF4J JDK14 Binding
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-jdk14

%description jdk14
SLF4J JDK14 Binding.

%package jdk-platform-logging
Summary:        SLF4J Platform Logging Binding
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-jdk-platform-logging

%description jdk-platform-logging
SLF4J Platform Logging Binding.

%package parent
Summary:        SLF4J Parent POM
Group:          Development/Libraries/Java

%description parent
SLF4J project parent pom.xml file

%package reload4j
Summary:        SLF4J LOG4J-12 Binding
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-reload4j

%description reload4j
SLF4J LOG4J-12 Binding.

%package ext
Summary:        SLF4J Extensions Module
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-ext

%description ext
Extensions to the SLF4J API.

%package -n jcl-over-%{name}
Summary:        JCL 1.1.1 implemented over SLF4J
Group:          Development/Libraries/Java
Obsoletes:      jcl-over-%{name}2

%description -n jcl-over-%{name}
JCL 1.1.1 implemented over SLF4J.

%package -n jul-to-%{name}
Summary:        JUL to SLF4J bridge
Group:          Development/Libraries/Java
Obsoletes:      jul-to-%{name}2

%description -n jul-to-%{name}
JUL to SLF4J bridge.

%package -n log4j-over-%{name}
Summary:        Log4j implemented over SLF4J
Group:          Development/Libraries/Java
Obsoletes:      log4j-over-%{name}2

%description -n log4j-over-%{name}
Log4j implemented over SLF4J.

%package migrator
Summary:        SLF4J Migrator
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-migrator

%description migrator
SLF4J Migrator.

%package sources
Summary:        SLF4J Source JARs
Group:          Development/Libraries/Java
Obsoletes:      %{name}2-sources

%description sources
SLF4J Source JARs.

%prep
%setup -q -a1
cp %{SOURCE2} LICENSE-2.0.txt

%build
mkdir -p lib
build-jar-repository -s lib cal10n/cal10n-api javassist reload4j/reload4j

ant package javadoc

# Sources
for i in api ext jdk14 jdk-platform-logging migrator nop reload4j simple; do
  mkdir -p %{name}-${i}/target
  jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --file=%{name}-${i}/target/%{name}-${i}-%{version}-sources.jar -C %{name}-${i}/src/main/java .
  if [ -d %{name}-${i}/src/main/resources ]; then
    jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
      --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
      --update --file=%{name}-${i}/target/%{name}-${i}-%{version}-sources.jar -C %{name}-${i}/src/main/resources .
  fi
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  mkdir -p ${i}/target
  jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --file=${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/java .
  if [ -d ${i}/src/main/resources ]; then
    jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
      --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
      --update --file=${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/resources .
  fi
done

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}

for i in api ext jdk14 jdk-platform-logging migrator nop reload4j simple; do
  install -m 644 slf4j-${i}/target/slf4j-${i}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/${i}.jar
  ln -sf ${i}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-${i}-sources.jar
  %add_maven_depmap org.slf4j:%{name}-${i}:jar:sources:%{version} %{name}/%{name}-${i}-sources.jar -f sources
  cp -pr slf4j-${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/slf4j-${i}
done

# Compatibility symlink
ln -sf reload4j.jar %{buildroot}%{_javadir}/%{name}/log4j12.jar
ln -sf reload4j.jar %{buildroot}%{_javadir}/%{name}/%{name}-log4j12.jar

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  install -m 644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  install -pm 0644 ${i}/target/${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{name}/${i}-sources.jar
  %add_maven_depmap org.slf4j:${i}:jar:sources:%{version} %{name}/${i}-sources.jar -f sources
  cp -pr ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}

%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/bom.pom
%add_maven_depmap %{name}/bom.pom -f bom
%{mvn_install_pom} parent/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/parent.pom
%add_maven_depmap %{name}/parent.pom -f parent

for i in api ext jdk14 jdk-platform-logging migrator nop reload4j simple; do
  %{mvn_install_pom} slf4j-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
done

for i in api nop simple; do
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
done

for i in ext jdk14 jdk-platform-logging migrator jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
done
%add_maven_depmap %{name}/reload4j.pom %{name}/reload4j.jar -f reload4j -a org.slf4j:slf4j-log4j12

%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{name}/%{name}-api.jar
%{_javadir}/%{name}/%{name}-nop.jar
%{_javadir}/%{name}/%{name}-simple.jar
%license LICENSE.txt LICENSE-2.0.txt

%files bom -f .mfiles-bom

%files parent -f .mfiles-parent

%files jdk14 -f .mfiles-jdk14
%{_javadir}/%{name}/%{name}-jdk14.jar

%files reload4j -f .mfiles-reload4j
%{_javadir}/%{name}/%{name}-reload4j.jar
%{_javadir}/%{name}/*log4j12.jar

%files ext -f .mfiles-ext
%{_javadir}/%{name}/%{name}-ext.jar

%files -n jcl-over-%{name} -f .mfiles-jcl-over-%{name}

%files -n log4j-over-%{name} -f .mfiles-log4j-over-%{name}

%files -n jul-to-%{name} -f .mfiles-jul-to-%{name}

%files jdk-platform-logging -f .mfiles-jdk-platform-logging
%exclude %{_javadir}/%{name}/%{name}-jdk-platform-logging.jar

%files migrator -f .mfiles-migrator
%exclude %{_javadir}/%{name}/%{name}-migrator.jar

%files sources -f .mfiles-sources

%files javadoc
%{_javadocdir}/%{name}

%changelog
