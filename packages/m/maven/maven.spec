#
# spec file for package maven
#
# Copyright (c) 2024 SUSE LLC
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


%global bundled_slf4j_version 1.7.25
%global homedir %{_datadir}/%{name}%{?maven_version_suffix}
%global confdir %{_sysconfdir}/%{name}%{?maven_version_suffix}
Name:           maven
Version:        3.9.8
Release:        0
Summary:        Java project management and project comprehension tool
# maven itself is ASL 2.0
# bundled slf4j is MIT
License:        Apache-2.0 AND MIT
Group:          Development/Tools/Building
URL:            https://maven.apache.org/
Source0:        http://archive.apache.org/dist/%{name}/%{name}-3/%{version}/source/apache-%{name}-%{version}-src.tar.gz
Source1:        maven-bash-completion
Source2:        mvn.1
Source10:       apache-%{name}-%{version}-build.tar.xz
Patch1:         0001-Adapt-mvn-script.patch
# Downstream-specific, avoids dependency on logback
Patch2:         0002-Invoke-logback-via-reflection.patch
Patch3:         0003-Remove-dependency-on-powermock.patch
Patch4:         0004-Fix-build-with-qdox-2.0.1.patch
Patch5:         0005-Reproducible-maven.build.timestamp.patch
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-logging
BuildRequires:  atinject
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  google-guice
BuildRequires:  guava
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  jakarta-inject
BuildRequires:  jansi
BuildRequires:  javapackages-local
BuildRequires:  jcl-over-slf4j
BuildRequires:  jdom2
BuildRequires:  maven-resolver-api >= 1.8.1
BuildRequires:  maven-resolver-connector-basic
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-named-locks
BuildRequires:  maven-resolver-spi
BuildRequires:  maven-resolver-transport-file
BuildRequires:  maven-resolver-transport-http
BuildRequires:  maven-resolver-transport-wagon
BuildRequires:  maven-resolver-util
BuildRequires:  maven-shared-utils
BuildRequires:  maven-wagon-file
BuildRequires:  maven-wagon-http
BuildRequires:  maven-wagon-http-shared
BuildRequires:  maven-wagon-provider-api
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm
BuildRequires:  plexus-cipher >= 2.0
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-cli
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-sec-dispatcher >= 2.0
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  qdox
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  slf4j-sources
BuildRequires:  unix2dos
BuildRequires:  xbean
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  xmvn-subst
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
Requires:       %{name}-lib = %{version}-%{release}
Requires(post): aaa_base
Requires(postun): aaa_base
# maven-lib cannot be noarch because of the position of jansi.jar
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
Requires:       google-guice
Requires:       guava
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jakarta-inject
Requires:       jansi
Requires:       javapackages-tools
Requires:       jcl-over-slf4j
Requires:       junit
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-named-locks
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-file
Requires:       maven-resolver-transport-http
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-shared-utils
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       objectweb-asm
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       plexus-xml
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
# Maven upstream uses patched version of SLF4J.  They unpack
# slf4j-simple-sources.jar, apply non-upstreamable, Maven-specific
# patch (using a script written in Groovy), compile and package as
# maven-slf4j-provider.jar, together with Maven-specific additions.
Provides:       bundled(slf4j) = %{bundled_slf4j_version}
# This package might be installed on a system, since it used to be
# produced by the binary maven repackaging in some repositories.
# This Obsoletes will allow a clean upgrade.
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
%setup -q -n apache-%{name}-%{version} -a10

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

# not really used during build, but a precaution
find -name '*.jar' -not -path '*/test/*' -delete
find -name '*.class' -delete
find -name '*.bat' -delete

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
sed -i "s/version=.*/version=%{version}/" `find -name build.properties`
sed -i "s/distributionId=.*/distributionId=apache-maven/" `find -name build.properties`
sed -i "s/distributionShortName=.*/distributionShortName=Maven/" `find -name build.properties`
sed -i "s/distributionName=.*/distributionName=Apache\ Maven/" `find -name build.properties`

%{mvn_package} :apache-maven __noinstall

%pom_remove_dep -r :logback-classic

%pom_xpath_remove pom:parent/pom:relativePath

for i in maven-compat maven-core maven-embedder maven-model maven-model-builder maven-plugin-api maven-resolver-provider maven-settings-builder
do
  %pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 $i
done

%{mvn_alias} :maven-resolver-provider :maven-aether-provider

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    commons-cli \
    glassfish-annotation-api \
    guice/google-guice \
    jakarta-inject \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-named-locks \
    maven-resolver/maven-resolver-spi \
    maven-resolver/maven-resolver-util \
    maven-shared-utils/maven-shared-utils \
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
    slf4j/api \
    slf4j/simple
ln -s $(build-classpath slf4j/slf4j-simple-sources) lib/
%{ant} \
  -Dtest.skip=true \
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
    slf4j-provider \
    embedder \
    compat; do
  cp -r %{name}-${i}/target/site/apidocs target/site/apidocs/%{name}-${i}
  %{mvn_artifact} %{name}-${i}/pom.xml %{name}-${i}/target/%{name}-${i}-%{version}.jar
done

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}

install -d -m 755 %{buildroot}%{homedir}/boot
install -d -m 755 %{buildroot}%{confdir}
install -d -m 755 %{buildroot}%{_datadir}/bash-completion/completions/

cp -a apache-maven/src/{bin,conf,lib} %{buildroot}%{homedir}/
chmod +x %{buildroot}%{homedir}/bin/*
unix2dos %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf
chmod -x %{buildroot}%{homedir}/bin/*.cmd %{buildroot}%{homedir}/bin/*.conf

# Transitive deps of wagon-http, missing because of unshading
build-jar-repository -p %{buildroot}%{homedir}/lib \
    aopalliance \
    atinject \
    commons-cli \
    commons-codec \
    glassfish-annotation-api \
    guava/guava \
    guice/google-guice \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    jakarta-inject \
    jansi/jansi \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-connector-basic \
    maven-resolver/maven-resolver-impl \
    maven-resolver/maven-resolver-named-locks \
    maven-resolver/maven-resolver-spi \
    maven-resolver/maven-resolver-transport-file \
    maven-resolver/maven-resolver-transport-http \
    maven-resolver/maven-resolver-transport-wagon \
    maven-resolver/maven-resolver-util \
    maven-shared-utils/maven-shared-utils \
    maven-wagon/file \
    maven-wagon/http \
    maven-wagon/http-shared \
    maven-wagon/provider-api \
    org.eclipse.sisu.inject \
    org.eclipse.sisu.plexus \
    plexus/plexus-cipher \
    plexus/interpolation \
    plexus/plexus-sec-dispatcher \
    plexus/utils \
    plexus/xml \
    plexus-containers/plexus-component-annotations \
    slf4j/api \
    slf4j/jcl-over-slf4j

cp %{buildroot}%{_javadir}/%{name}/*.jar %{buildroot}%{homedir}/lib/

ln -sf %{_libdir}/jansi/libjansi.so %{buildroot}%{homedir}/lib/jansi-native/

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
install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

%files lib -f .mfiles
%doc README.md
%license LICENSE NOTICE
%{homedir}
%dir %{confdir}
%dir %{confdir}/logging
%config(noreplace) %{_sysconfdir}/m2%{?maven_version_suffix}.conf
%config(noreplace) %{confdir}/settings.xml
%config(noreplace) %{confdir}/logging/simplelogger.properties

%files
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_datadir}/bash-completion
%{_mandir}/man1/mvn.1%{?ext_man}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
