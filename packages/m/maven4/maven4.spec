#
# spec file for package maven4
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


%global maven_version_suffix 4
%global base_name maven
%global file_version 4.0.0-rc-5
%global homedir %{_datadir}/%{base_name}%{?maven_version_suffix}
%global confdir %{_sysconfdir}/%{base_name}%{?maven_version_suffix}
Name:           %{base_name}%{?maven_version_suffix}
Version:        4.0.0~rc5
Release:        0
Summary:        Java project management and project comprehension tool
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Tools/Building
URL:            https://maven.apache.org/
Source0:        https://archive.apache.org/dist/%{base_name}/%{base_name}-4/%{file_version}/source/apache-%{base_name}-%{file_version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1
Source10:       apache-%{base_name}-build.tar.xz
Patch1:         0001-Adapt-mvn-script.patch
# Downstream-specific, avoids dependency on logback
Patch2:         0002-Invoke-logback-via-reflection.patch
Patch3:         0001-Fix-a-ConcurrentModificationException-11429.patch
Patch4:         0002-Fix-field-accessibility-leak-in-EnhancedCompositeBea.patch
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-logging
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  google-gson
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  jakarta-inject
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  jcl-over-slf4j2
BuildRequires:  jdom2
BuildRequires:  jline3
BuildRequires:  jline3-builtins
BuildRequires:  jline3-console
BuildRequires:  jline3-console-ui
BuildRequires:  jline3-jansi-core
BuildRequires:  jline3-native
BuildRequires:  jline3-reader
BuildRequires:  jline3-style
BuildRequires:  jline3-terminal
BuildRequires:  jline3-terminal-jni
BuildRequires:  maven-resolver2-api
BuildRequires:  maven-resolver2-connector-basic
BuildRequires:  maven-resolver2-impl
BuildRequires:  maven-resolver2-named-locks
BuildRequires:  maven-resolver2-spi
BuildRequires:  maven-resolver2-transport-apache
BuildRequires:  maven-resolver2-transport-file
BuildRequires:  maven-resolver2-transport-jdk
BuildRequires:  maven-resolver2-transport-wagon
BuildRequires:  maven-resolver2-util
BuildRequires:  maven-wagon-file
BuildRequires:  maven-wagon-http
BuildRequires:  maven-wagon-http-shared
BuildRequires:  maven-wagon-provider-api
BuildRequires:  modello
BuildRequires:  objectweb-asm
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-interactivity-api
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-sec-dispatcher4
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml4
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j2
BuildRequires:  stax2-api
BuildRequires:  unix2dos
BuildRequires:  woodstox-core
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xmvn-subst
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
#!BuildIgnore:  %{name}-bootstrap
#!BuildIgnore:  %{name}-lib
#!BuildIgnore:  plexus-sec-dispatcher
Requires:       java-headless >= 17
Requires:       %{name}-lib = %{version}-%{release}

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package lib
Summary:        Core part of Maven
Group:          Development/Tools/Building
# JAR symlinks in lib directory
Requires:       aopalliance
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-lang3
Requires:       apache-commons-logging
Requires:       atinject
Requires:       glassfish-annotation-api
Requires:       google-gson
Requires:       google-guice
Requires:       guava
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jakarta-inject
Requires:       jcl-over-slf4j2
Requires:       jline3-builtins
Requires:       jline3-console
Requires:       jline3-console-ui
Requires:       jline3-jansi-core
Requires:       jline3-native
Requires:       jline3-reader
Requires:       jline3-style
Requires:       jline3-terminal
Requires:       jline3-terminal-jni
Requires:       maven-resolver2-api
Requires:       maven-resolver2-connector-basic
Requires:       maven-resolver2-impl
Requires:       maven-resolver2-named-locks
Requires:       maven-resolver2-spi
Requires:       maven-resolver2-transport-apache
Requires:       maven-resolver2-transport-file
Requires:       maven-resolver2-transport-jdk
Requires:       maven-resolver2-transport-wagon
Requires:       maven-resolver2-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       objectweb-asm
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interactivity-api
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher4
Requires:       plexus-utils
Requires:       plexus-xml4
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j2
Requires:       stax2-api
Requires:       woodstox-core
Provides:       %{name}-bootstrap
Obsoletes:      %{name}-bootstrap

%description lib
Core part of Apache Maven that can be used as a library.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{base_name}-%{file_version} -a10

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%pom_remove_dep -r :junit-bom
%pom_remove_dep -r :mockito-bom
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin :bom-builder3 apache-maven

%pom_remove_dep :jline-terminal-ffm impl/maven-jline
%pom_remove_dep :jline-terminal-ffm apache-maven
%pom_remove_dep -r :logback-classic

%pom_disable_module maven-executor impl

find -name '*.java' -exec sed -i 's/\r//' {} +
find -name 'pom.xml' -exec sed -i 's/\r//' {} +

sed -i "s/@{maven_version_suffix}/%{?maven_version_suffix}/" apache-maven/src/assembly/maven/bin/mvn

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

#sed -i 's:\r::' apache-maven/src/conf/settings.xml

# Downloads dependency licenses from the Internet and aggregates them.
# We already ship the licenses in their respective packages.
rm apache-maven/src/main/appended-resources/META-INF/LICENSE.vm

# Disable plugins which are not useful for us
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
sed -i "
/buildNumber=/ d
/timestamp=/ d
" `find -name build.properties`
sed -i "s/version=.*/version=%{file_version}/" `find -name build.properties`
sed -i "s/distributionId=.*/distributionId=apache-maven/" `find -name build.properties`
sed -i "s/distributionShortName=.*/distributionShortName=Maven/" `find -name build.properties`
sed -i "s/distributionName=.*/distributionName=Apache\ Maven/" `find -name build.properties`

%{mvn_package} :apache-maven __noinstall
%{mvn_package} ::mdo: __noinstall

for i in \
  maven \
  maven-artifact \
  maven-builder-support \
  maven-compat \
  maven-core \
  maven-embedder \
  maven-model-builder \
  maven-model \
  maven-plugin-api \
  maven-repository-metadata \
  maven-resolver-provider \
  maven-settings-builder \
  maven-settings; do
    %{mvn_compat_version} :${i} 4 %{file_version}
done

%{mvn_file} :{*} %{base_name}/@1

%build

mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    atinject \
    commons-cli \
    guice/google-guice \
    jakarta-inject \
    jdom2/jdom2 \
    jline3/jansi-core \
    jline3/jline-builtins \
    jline3/jline-console \
    jline3/jline-console-ui \
    jline3/jline-reader \
    jline3/jline-terminal \
    maven-resolver/maven-resolver-api-2 \
    maven-resolver/maven-resolver-connector-basic-2 \
    maven-resolver/maven-resolver-impl-2 \
    maven-resolver/maven-resolver-named-locks-2 \
    maven-resolver/maven-resolver-spi-2 \
    maven-resolver/maven-resolver-transport-apache-2 \
    maven-resolver/maven-resolver-transport-file-2 \
    maven-resolver/maven-resolver-transport-jdk-2 \
    maven-resolver/maven-resolver-transport-wagon-2 \
    maven-resolver/maven-resolver-util-2 \
    maven-wagon/provider-api \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-classworlds \
    plexus-containers/plexus-component-annotations \
    plexus/interactivity-api \
    plexus/interpolation \
    plexus/sec-dispatcher-4 \
    plexus/utils \
    plexus/xml-4 \
    slf4j/api-2 \
    stax2-api \
    woodstox-core

ant package javadoc

%{mvn_artifact} pom.xml
%{mvn_artifact} api/pom.xml
%{mvn_artifact} compat/pom.xml
%{mvn_artifact} impl/pom.xml

mkdir -p target/site/apidocs
for i in \
  api/maven-api-annotations \
  api/maven-api-cli \
  api/maven-api-core \
  api/maven-api-di \
  api/maven-api-metadata \
  api/maven-api-model \
  api/maven-api-plugin \
  api/maven-api-settings \
  api/maven-api-spi \
  api/maven-api-toolchain \
  api/maven-api-xml \
  compat/maven-artifact \
  compat/maven-builder-support \
  compat/maven-compat \
  compat/maven-embedder \
  compat/maven-model \
  compat/maven-model-builder \
  compat/maven-plugin-api \
  compat/maven-repository-metadata \
  compat/maven-resolver-provider \
  compat/maven-settings \
  compat/maven-settings-builder \
  compat/maven-toolchain-builder \
  compat/maven-toolchain-model \
  impl/maven-cli \
  impl/maven-core \
  impl/maven-di \
  impl/maven-executor \
  impl/maven-impl \
  impl/maven-jline \
  impl/maven-logging \
  impl/maven-support \
  impl/maven-xml; do
  cp -r ${i}/target/site/apidocs target/site/apidocs/`basename ${i}`
  %{mvn_artifact} ${i}/pom.xml ${i}/target/`basename ${i}`-%{file_version}.jar
done

%install
%mvn_install

%fdupes %{buildroot}%{_javadocdir}

install -d -m 755 %{buildroot}%{homedir}/boot
install -d -m 755 %{buildroot}%{homedir}/conf
install -d -m 755 %{buildroot}%{confdir}
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions/

cp -a apache-maven/src/assembly/maven/{bin,conf,lib} %{buildroot}%{homedir}/
chmod +x %{buildroot}%{homedir}/bin/*
unix2dos %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf
chmod -x %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf

build-jar-repository -p %{buildroot}%{homedir}/lib \
    aopalliance \
    apache-commons-lang3 \
    apache-commons-logging \
    atinject \
    commons-cli \
    commons-codec \
    glassfish-annotation-api \
    google-gson/gson \
    guava/guava \
    guice/google-guice \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    jakarta-inject \
    jdom2/jdom2 \
    jline3/jansi-core \
    jline3/jline-builtins \
    jline3/jline-console \
    jline3/jline-console-ui \
    jline3/jline-native \
    jline3/jline-reader \
    jline3/jline-style \
    jline3/jline-terminal \
    jline3/jline-terminal-jni \
    maven-resolver/maven-resolver-api-2 \
    maven-resolver/maven-resolver-connector-basic-2 \
    maven-resolver/maven-resolver-impl-2 \
    maven-resolver/maven-resolver-named-locks-2 \
    maven-resolver/maven-resolver-spi-2 \
    maven-resolver/maven-resolver-transport-apache-2 \
    maven-resolver/maven-resolver-transport-file-2 \
    maven-resolver/maven-resolver-transport-jdk-2 \
    maven-resolver/maven-resolver-transport-wagon-2 \
    maven-resolver/maven-resolver-util-2 \
    maven-wagon/file \
    maven-wagon/http \
    maven-wagon/http-shared \
    maven-wagon/provider-api \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus-containers/plexus-component-annotations \
    plexus/interactivity-api \
    plexus/interpolation \
    plexus/sec-dispatcher-4 \
    plexus/utils \
    plexus/xml-4 \
    slf4j/api-2 \
    slf4j/jcl-over-slf4j-2 \
    stax2-api \
    woodstox-core

cp %{buildroot}%{_javadir}/%{base_name}/*.jar %{buildroot}%{homedir}/lib/

build-jar-repository -p %{buildroot}%{homedir}/boot \
    plexus-classworlds

xmvn-subst -R %{buildroot} -s %{buildroot}%{homedir}

install -p -m 644 %{SOURCE2} %{buildroot}%{homedir}/bin/
gzip -9 %{buildroot}%{homedir}/bin/mvn.1
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/mvn%{?maven_version_suffix}
mv %{buildroot}%{homedir}/bin/m2.conf %{buildroot}%{_sysconfdir}/m2%{?maven_version_suffix}.conf
ln -sf %{_sysconfdir}/m2%{?maven_version_suffix}.conf %{buildroot}%{homedir}/bin/m2.conf
mv %{buildroot}%{homedir}/conf/maven-system.properties %{buildroot}%{confdir}/
ln -sf %{confdir}/maven-system.properties %{buildroot}%{homedir}/conf/
mv %{buildroot}%{homedir}/conf/maven-user.properties %{buildroot}%{confdir}/
ln -sf %{confdir}/maven-user.properties %{buildroot}%{homedir}/conf/
mv %{buildroot}%{homedir}/conf/settings.xml %{buildroot}%{confdir}/
ln -sf %{confdir}/settings.xml %{buildroot}%{homedir}/conf/settings.xml
mv %{buildroot}%{homedir}/conf/toolchains.xml %{buildroot}%{confdir}/
ln -sf %{confdir}/toolchains.xml %{buildroot}%{homedir}/conf/settings.xml
mv %{buildroot}%{homedir}/conf/logging %{buildroot}%{confdir}/
ln -sf %{confdir}/logging %{buildroot}%{homedir}/conf

# Ghosts for alternatives
install -dm 0755 %{buildroot}%{_bindir}/
ln -sf %{homedir}/bin/mvn %{buildroot}%{_bindir}/mvn%{maven_version_suffix}
ln -sf %{homedir}/bin/mvnenc %{buildroot}%{_bindir}/mvnenc%{maven_version_suffix}
ln -sf %{homedir}/bin/mvnsh %{buildroot}%{_bindir}/mvnsh%{maven_version_suffix}
ln -sf %{homedir}/bin/mvnup %{buildroot}%{_bindir}/mvnup%{maven_version_suffix}
ln -sf %{homedir}/bin/mvnDebug %{buildroot}%{_bindir}/mvnDebug%{maven_version_suffix}

%files lib -f .mfiles
%license LICENSE NOTICE
%doc README.md
%{homedir}
%exclude %{homedir}/bin/mvn*
%dir %{confdir}
%dir %{confdir}/logging
%config(noreplace) %{_sysconfdir}/m2%{?maven_version_suffix}.conf
%config(noreplace) %{confdir}/maven-system.properties
%config(noreplace) %{confdir}/maven-user.properties
%config(noreplace) %{confdir}/settings.xml
%config(noreplace) %{confdir}/toolchains.xml
%config(noreplace) %{confdir}/logging/maven.logger.properties

%files
%{homedir}/bin/mvn*
%{_datadir}/bash-completion
%{_bindir}/mvn%{maven_version_suffix}
%{_bindir}/mvnenc%{maven_version_suffix}
%{_bindir}/mvnsh%{maven_version_suffix}
%{_bindir}/mvnup%{maven_version_suffix}
%{_bindir}/mvnDebug%{maven_version_suffix}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
