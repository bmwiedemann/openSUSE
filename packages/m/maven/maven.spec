#
# spec file for package maven
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


%global base_name maven
%global homedir %{_datadir}/%{base_name}%{?maven_version_suffix}
%global confdir %{_sysconfdir}/%{base_name}%{?maven_version_suffix}
Name:           %{base_name}%{?maven_version_suffix}
Version:        3.10.0
Release:        0
Summary:        Java project management and project comprehension tool
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Tools/Building
URL:            https://maven.apache.org/
Source0:        https://archive.apache.org/dist/%{base_name}/%{base_name}-3/%{version}/source/apache-%{base_name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1
Source10:       apache-%{base_name}-build.tar.xz
Source100:      pom_properties.py
Patch1:         0001-Adapt-mvn-script.patch
Patch2:         0002-Invoke-logback-via-reflection.patch
Patch3:         0003-Remove-dependency-on-powermock.patch
Patch4:         0004-Fix-build-with-qdox-2.0.1.patch
Patch5:         0005-Reproducible-maven.build.timestamp.patch
Patch6:         0006-Plexus-utils-4.x-Plexus-xml-3.x-and-javax.annotation.patch
Patch7:         jline-4.4.x.patch
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-logging
BuildRequires:  atinject
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  google-errorprone-annotations
BuildRequires:  google-gson
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  j2objc-annotations
BuildRequires:  jakarta-inject
BuildRequires:  jansi
BuildRequires:  javapackages-local
BuildRequires:  jcl-over-slf4j
BuildRequires:  jline3-jansi-core
BuildRequires:  jline3-native
BuildRequires:  jline3-terminal
BuildRequires:  jline3-terminal-jni
BuildRequires:  jspecify
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-connector-basic
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-named-locks
BuildRequires:  maven-resolver-spi
BuildRequires:  maven-resolver-transport-apache
BuildRequires:  maven-resolver-transport-file
BuildRequires:  maven-resolver-transport-wagon
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-utils
BuildRequires:  maven-wagon-file
BuildRequires:  maven-wagon-http
BuildRequires:  maven-wagon-http-shared
BuildRequires:  maven-wagon-provider-api
BuildRequires:  modello-ant-task
BuildRequires:  objectweb-asm
BuildRequires:  plexus-cipher >= 2.0
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-metadata-generator-ant
BuildRequires:  plexus-sec-dispatcher >= 2.0
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  slf4j-sources
BuildRequires:  unix2dos
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xmvn-subst
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
Requires:       %{name}-lib = %{version}-%{release}
Requires(post): aaa_base
Requires(postun): aaa_base
# maven-lib cannot be noarch because of the position of jline-native.jar
#BuildArch:      noarch

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        lib
Summary:        Core part of Maven
# Require full javapackages-tools since maven-script uses
# /usr/share/java-utils/java-functions
# XMvn does generate auto-requires, but explicit requires are still
# needed because some symlinked JARs are not present in Maven POMs or
# their dependency scope prevents them from being added automatically
# by XMvn.  It would be possible to explicitly specify only
# dependencies which are not generated automatically, but adding
# everything seems to be easier.
Group:          Development/Tools/Building
Requires:       aopalliance
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-logging
Requires:       atinject
Requires:       glassfish-annotation-api
Requires:       google-errorprone-annotations
Requires:       google-gson
Requires:       google-guice
Requires:       guava
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       j2objc-annotations
Requires:       jakarta-inject
Requires:       jcl-over-slf4j
Requires:       jline3-jansi-core
Requires:       jline3-native
Requires:       jline3-terminal
Requires:       jline3-terminal-jni
Requires:       jspecify
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-named-locks
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-apache
Requires:       maven-resolver-transport-file
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       objectweb-asm
Requires:       plexus-cipher
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       plexus-xml
Requires:       python3
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Obsoletes:      %{name}-bootstrap
Obsoletes:      %{name}-jansi
# If XMvn is part of the same RPM transaction then it should be
# installed first to avoid triggering rhbz#1014355.
OrderWithRequires: xmvn-minimal

%description    lib
Core part of Apache Maven that can be used as a library.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-maven-%{version} -a10

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%if %{?pkg_vcmp:%pkg_vcmp jline3-terminal >= 4.1}%{!?pkg_vcmp:0}
%patch -P 7 -p1
%endif

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

sed -i "s/@{maven_version_suffix}/%{?maven_version_suffix}/" apache-maven/src/bin/mvn

sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Downloads dependency licenses from the Internet and aggregates them.
# We already ship the licenses in their respective packages.
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

# Disable plugins which are not useful for us
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
sed -i "
/buildNumber=/ d
/timestamp=/ d
" `find -name build.properties`
sed -i "s/distributionId=.*/distributionId=apache-maven/" `find -name build.properties`
sed -i "s/distributionShortName=.*/distributionShortName=Maven/" `find -name build.properties`
sed -i "s/distributionName=.*/distributionName=Apache\ Maven/" `find -name build.properties`

%{mvn_package} :apache-maven __noinstall

%pom_remove_dep :jline-terminal-ffm maven-jline
%pom_remove_dep :jline-terminal-ffm apache-maven
%pom_remove_dep -r :logback-classic

%pom_xpath_remove pom:parent/pom:relativePath

%{mvn_alias} :maven-resolver-provider :maven-aether-provider

(cd maven-core && python3 %{SOURCE100} pom.xml >build.properties)

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    commons-cli \
    guice/google-guice \
    jakarta-inject \
    jline3/jansi-core \
    jline3/jline-terminal \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-connector-basic \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-named-locks \
    maven-resolver/maven-resolver-spi \
    maven-resolver/maven-resolver-transport-apache \
    maven-resolver/maven-resolver-transport-file \
    maven-resolver/maven-resolver-util \
    maven-wagon/provider-api \
    objectweb-asm/asm-commons \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-classworlds \
    plexus-containers/plexus-component-annotations \
    plexus/interpolation \
    plexus/plexus-cipher \
    plexus/plexus-sec-dispatcher \
    plexus/utils \
    plexus/xml \
    slf4j/api

ln -s $(build-classpath slf4j/slf4j-simple-sources) lib/

ant \
  -Dtest.skip=true \
  -Dproject.version=%{version} \
  package javadoc

%{mvn_artifact} pom.xml
mkdir -p target/site/apidocs
for i in \
    artifact \
    model \
    plugin-api \
    builder-support \
    model-builder \
    settings \
    settings-builder \
    repository-metadata \
    resolver-provider \
    core \
    jline \
    slf4j-provider \
    embedder \
    compat; do
  cp -r %{base_name}-${i}/target/site/apidocs target/site/apidocs/%{base_name}-${i}
  %{mvn_artifact} %{base_name}-${i}/pom.xml %{base_name}-${i}/target/%{base_name}-${i}-%{version}.jar
done

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}

install -dm 0755 %{buildroot}%{homedir}/boot
install -dm 0755 %{buildroot}%{confdir}
install -dm 0755 %{buildroot}%{_datadir}/bash-completion/completions/

cp -a apache-maven/src/{bin,conf,lib} %{buildroot}%{homedir}/
rm -rf %{buildroot}%{homedir}/lib/*-native/
chmod +x %{buildroot}%{homedir}/bin/*
unix2dos %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf
chmod -x %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf

# Transitive deps of wagon-http, missing because of unshading
build-jar-repository -p %{buildroot}%{homedir}/lib \
    aopalliance \
    atinject \
    commons-cli \
    commons-codec \
    commons-logging \
    glassfish-annotation-api \
    google-errorprone/annotations \
    google-gson/gson \
    guava/guava \
    guice/google-guice \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    j2objc-annotations \
    jakarta-inject \
    jline3/jansi-core \
    jline3/jline-native \
    jline3/jline-terminal \
    jline3/jline-terminal-jni \
    jspecify \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-connector-basic \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-named-locks \
    maven-resolver/maven-resolver-spi \
    maven-resolver/maven-resolver-transport-apache \
    maven-resolver/maven-resolver-transport-file \
    maven-resolver/maven-resolver-transport-wagon \
    maven-resolver/maven-resolver-util \
    maven-wagon/provider-api \
    maven-wagon/file \
    maven-wagon/http \
    maven-wagon/http-shared \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-containers/plexus-component-annotations \
    plexus/interpolation \
    plexus/plexus-cipher \
    plexus/plexus-sec-dispatcher \
    plexus/utils \
    plexus/xml \
    plexus-containers/plexus-component-annotations \
    slf4j/api \
    slf4j/jcl-over-slf4j

cp %{buildroot}%{_javadir}/%{name}/*.jar %{buildroot}%{homedir}/lib/

build-jar-repository -p %{buildroot}%{homedir}/boot \
    plexus-classworlds

xmvn-subst -R %{buildroot} -s %{buildroot}%{homedir}

install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/mvn%{?maven_version_suffix}
mv %{buildroot}%{homedir}/bin/m2.conf %{buildroot}%{_sysconfdir}/m2%{?maven_version_suffix}.conf
ln -sf %{_sysconfdir}/m2%{?maven_version_suffix}.conf %{buildroot}%{homedir}/bin/m2.conf
mv %{buildroot}%{homedir}/conf/settings.xml %{buildroot}%{confdir}/
ln -sf %{confdir}/settings.xml %{buildroot}%{homedir}/conf/settings.xml
mv %{buildroot}%{homedir}/conf/logging %{buildroot}%{confdir}/
ln -sf %{confdir}/logging %{buildroot}%{homedir}/conf

install -d -m 0755 %{buildroot}%{_bindir}
ln -sf %{homedir}/bin/mvn %{buildroot}%{_bindir}/
ln -sf %{homedir}/bin/mvnDebug %{buildroot}%{_bindir}/
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_datadir}/bash-completion
%{_mandir}/man1/mvn.1%{?ext_man}

%files lib -f .mfiles
%doc README.md
%license LICENSE NOTICE
%{homedir}
%dir %{confdir}
%dir %{confdir}/logging
%config(noreplace) %{_sysconfdir}/m2%{?maven_version_suffix}.conf
%config(noreplace) %{confdir}/settings.xml
%config(noreplace) %{confdir}/logging/simplelogger.properties

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
