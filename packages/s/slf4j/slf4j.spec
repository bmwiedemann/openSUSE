#
# spec file for package slf4j
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.7.36
Release:        0
Summary:        Simple Logging Facade for Java
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://www.slf4j.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        build.xml.tar.xz
Patch1:         build-remove-slf4j_api-binder.patch
Patch2:         slf4j-commons-lang3.patch
Patch3:         slf4j-reload4j-bundlename.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-logging
BuildRequires:  cal10n
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  javapackages-local
BuildRequires:  javassist >= 3.4
BuildRequires:  reload4j
Requires:       cal10n
Requires:       java
# this is ugly hack, which creates package which requires the same,
# however slf4j is not splitted between -api and -impl, but pom files are modeled as it was
Provides:       osgi(slf4j.api)
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

%package manual
Summary:        Documents for %{name}
Group:          Documentation/Other

%description manual
Manual for %{name}.

%package jdk14
Summary:        SLF4J JDK14 Binding
Group:          Development/Libraries/Java
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description jdk14
SLF4J JDK14 Binding.

%package reload4j
Summary:        SLF4J LOG4J-12 Binding
Group:          Development/Libraries/Java
Requires:       mvn(ch.qos.reload4j:reload4j)
Requires:       mvn(org.slf4j:slf4j-api) = %{version}
Provides:       %{name}-log4j12 = %{version}
Obsoletes:      %{name}-log4j12 < %{version}

%description reload4j
SLF4J LOG4J-12 Binding.

%package jcl
Summary:        SLF4J JCL Binding
Group:          Development/Libraries/Java
Requires:       mvn(commons-logging:commons-logging)
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description jcl
SLF4J JCL Binding.

%package ext
Summary:        SLF4J Extensions Module
Group:          Development/Libraries/Java
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description ext
Extensions to the SLF4J API.

%package -n jcl-over-slf4j
Summary:        JCL 1.1.1 implemented over SLF4J
Group:          Development/Libraries/Java
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description -n jcl-over-slf4j
JCL 1.1.1 implemented over SLF4J.

%package -n log4j-over-slf4j
Summary:        Log4j implemented over SLF4J
Group:          Development/Libraries/Java
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description -n log4j-over-slf4j
Log4j implemented over SLF4J.

%package -n jul-to-slf4j
Summary:        JUL to SLF4J bridge
Group:          Development/Libraries/Java
Requires:       mvn(org.slf4j:slf4j-api) = %{version}

%description -n jul-to-slf4j
JUL to SLF4J bridge.

%package sources
Summary:        SLF4J Source JARs
Group:          Development/Libraries/Java

%description sources
SLF4J Source JARs.

%prep
%setup -q -a2
%patch1 -p1
%patch2 -p1
%patch3 -p1
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} APACHE-LICENSE

sed -i -e "s|ant<|org.apache.ant<|g" integration/pom.xml

sed -i -e "s|\${reload4j.version}|1\.2\.19|g" \
	log4j-over-slf4j/src/main/resources/META-INF/MANIFEST.MF

%{_bindir}/find -name "*.css" -o -name "*.js" -o -name "*.txt" | \
    %{_bindir}/xargs -t perl -pi -e 's/\r$//g'

# Unexpanded variable in the manifests
for i in */src/main/resources/META-INF/MANIFEST.MF; do
  echo "" >> ${i}
  echo "Bundle-Version: %{version}" >> ${i}
  sed -i '/^$/d' ${i}
  perl -pi -e 's#\$\{parsedVersion\.osgiVersion\}#%{version}#g' ${i}
  perl -pi -e 's#\$\{slf4j\.api\.minimum\.compatible\.version\}#1\.6\.0#g' ${i}
done

# The general pattern is that the API package exports API classes and does
# # not require impl classes. slf4j was breaking that causing "A cycle was
# # detected when generating the classpath slf4j.api, slf4j.nop, slf4j.api."
# # The API bundle requires impl package, so to avoid cyclic dependencies
# # during build time, it is necessary to mark the imported package as an
# # optional one.
# # Reported upstream: http://bugzilla.slf4j.org/show_bug.cgi?id=283
sed -i "/Import-Package/s/$/;resolution:=optional/" slf4j-api/src/main/resources/META-INF/MANIFEST.MF

%pom_change_dep -r -f ::::: :::::

%build
export CLASSPATH=$(build-classpath reload4j \
                   commons-logging \
                   commons-lang3 \
                   javassist-3.14.0 \
                   cal10n)
export CLASSPATH=$CLASSPATH:$(pwd)/slf4j-api/target/slf4j-api-%{version}.jar
export MAVEN_REPO_LOCAL=$(pwd)/.m2
ant -Dmaven2.jpp.mode=true \
    -Dmaven.test.skip=true \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    package javadoc \

# Sources
for i in api ext jcl jdk14 reload4j nop simple; do
  mkdir -p %{name}-${i}/target
  jar cf %{name}-${i}/target/%{name}-${i}-%{version}-sources.jar -C %{name}-${i}/src/main/java .
  jar uf %{name}-${i}/target/%{name}-${i}-%{version}-sources.jar -C %{name}-${i}/src/main/resources .
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  mkdir -p ${i}/target
  jar cf ${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/java .
  jar uf ${i}/target/${i}-%{version}-sources.jar -C ${i}/src/main/resources .
done

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}

for i in api ext jcl jdk14 reload4j nop simple; do
  install -m 644 slf4j-${i}/target/slf4j-${i}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/${i}.jar
  ln -sf ${i}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${i}.jar
done

# Compatibility symlink
ln -sf reload4j.jar %{buildroot}%{_javadir}/%{name}/log4j12.jar
ln -sf reload4j.jar %{buildroot}%{_javadir}/%{name}/%{name}-log4j12.jar

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  install -m 644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
done

for i in api ext jcl jdk14 reload4j nop simple; do
  install -pm 0644 %{name}-${i}/target/%{name}-${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-${i}-sources.jar
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  install -pm 0644 ${i}/target/${i}-%{version}-sources.jar \
    %{buildroot}%{_javadir}/%{name}/${i}-sources.jar
done

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}

for i in api ext jcl jdk14 reload4j nop simple; do
  %pom_remove_parent slf4j-${i}
  %pom_xpath_inject "pom:project" "
    <groupId>org.slf4j</groupId>
    <version>%{version}</version>" slf4j-${i}
  install -pm 644 slf4j-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
done

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %pom_remove_parent ${i}
  %pom_xpath_inject "pom:project" "
    <groupId>org.slf4j</groupId>
    <version>%{version}</version>" ${i}
  install -pm 644 ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
done

for i in api nop simple; do
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
done

for i in ext jcl jdk14 jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
done

%add_maven_depmap %{name}/reload4j.pom %{name}/reload4j.jar -f reload4j  -a org.slf4j:%{name}-log4j12

for i in api ext jcl jdk14 reload4j nop simple; do
  %add_maven_depmap org.slf4j:%{name}-${i}:jar:sources:%{version} %{name}/%{name}-${i}-sources.jar -f sources
done

%add_maven_depmap org.slf4j:%{name}-log4j12:jar:sources:%{version} %{name}/%{name}-reload4j-sources.jar -f sources

for i in jcl-over-slf4j jul-to-slf4j log4j-over-slf4j; do
  %add_maven_depmap org.slf4j:${i}:jar:sources:%{version} %{name}/${i}-sources.jar -f sources
done

# manual
install -d -m 0755 %{buildroot}%{_docdir}/%{name}-%{version}
rm -f target/site/.htaccess
cp -pr target/site %{buildroot}%{_docdir}/%{name}-%{version}/
install -m 644 LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}/

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site

%files -f .mfiles
%dir %{_docdir}/%{name}-%{version}
%license %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}/%{name}-api.jar
%{_javadir}/%{name}/%{name}-nop.jar
%{_javadir}/%{name}/%{name}-simple.jar

%files jdk14 -f .mfiles-jdk14
%{_javadir}/%{name}/%{name}-jdk14.jar

%files reload4j -f .mfiles-reload4j
%{_javadir}/%{name}/%{name}-reload4j.jar
%{_javadir}/%{name}/*log4j12.jar

%files jcl -f .mfiles-jcl
%{_javadir}/%{name}/%{name}-jcl.jar

%files ext -f .mfiles-ext
%{_javadir}/%{name}/%{name}-ext.jar

%files -n jcl-over-slf4j -f .mfiles-jcl-over-slf4j

%files -n log4j-over-slf4j -f .mfiles-log4j-over-slf4j

%files -n jul-to-slf4j -f .mfiles-jul-to-slf4j

%files sources -f .mfiles-sources

%files javadoc
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}/site

%changelog
