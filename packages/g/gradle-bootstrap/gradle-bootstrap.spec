#
# spec file for package gradle-bootstrap
#
# Copyright (c) 2019 SUSE LLC.
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


%global short_name gradle
%global gradle_version 4.4.1
%global groovy_version 2.4.8
%global gpars_version 1.2.1
Name:           %{short_name}-bootstrap
Version:        %{gradle_version}
Release:        0
Summary:        Bootstrap version of Gradle build automation tool
# Some examples and integration tests are under GNU LGPL and Boost
# Software License, but are not used to create binary package.
License:        Apache-2.0
URL:            https://www.gradle.org/
# Tarball of %{_datadir}/gradle directory from our own gradle package built from sources with all the symlinks dereferenced
Source0:        %{short_name}-%{gradle_version}-built.tar.xz
Source1:        gradle-launcher.sh.in
Source2:        gradle-man.txt
# Pom file from our own groovy package built from sources
Source100:      groovy-all.pom
Source200:      http://central.maven.org/maven2/org/codehaus/gpars/gpars/%{gpars_version}/gpars-%{gpars_version}.pom
# Our own built gpars.jar
Source201:      gpars.jar

BuildRequires:  ant
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-ivy
BuildRequires:  aqute-bndlib
BuildRequires:  asciidoc
BuildRequires:  atinject
BuildRequires:  aws-sdk-java-core
BuildRequires:  aws-sdk-java-kms
BuildRequires:  aws-sdk-java-s3
BuildRequires:  base64coder
BuildRequires:  bash
BuildRequires:  beust-jcommander
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
BuildRequires:  bsh2
BuildRequires:  ecj
BuildRequires:  glassfish-servlet-api
BuildRequires:  google-gson
BuildRequires:  google-guice
BuildRequires:  guava20
BuildRequires:  hawtjni-runtime
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  jackson-annotations
BuildRequires:  jackson-core
BuildRequires:  jackson-databind
BuildRequires:  jansi
BuildRequires:  jansi-native
BuildRequires:  jatl
BuildRequires:  javapackages-local
BuildRequires:  jcifs
BuildRequires:  jcip-annotations
BuildRequires:  jcl-over-slf4j
BuildRequires:  jetty-server
BuildRequires:  jetty-util
BuildRequires:  jgit
BuildRequires:  joda-time
BuildRequires:  jsch
BuildRequires:  jsr-305
BuildRequires:  jul-to-slf4j
BuildRequires:  junit
BuildRequires:  kryo
BuildRequires:  log4j-over-slf4j
BuildRequires:  maven-lib
BuildRequires:  maven-resolver-api
BuildRequires:  maven-resolver-connector-basic
BuildRequires:  maven-resolver-impl
BuildRequires:  maven-resolver-spi
BuildRequires:  maven-resolver-transport-wagon
BuildRequires:  maven-resolver-util
BuildRequires:  maven-wagon-file
BuildRequires:  maven-wagon-http
BuildRequires:  maven-wagon-http-shared
BuildRequires:  maven-wagon-provider-api
BuildRequires:  minlog
BuildRequires:  native-platform
BuildRequires:  nekohtml
BuildRequires:  objectweb-asm
BuildRequires:  objenesis
BuildRequires:  plexus-cipher
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-sec-dispatcher
BuildRequires:  plexus-utils
BuildRequires:  reflectasm
BuildRequires:  rhino
BuildRequires:  sisu-inject
BuildRequires:  sisu-plexus
BuildRequires:  slf4j
BuildRequires:  snakeyaml
BuildRequires:  tesla-polyglot-common
BuildRequires:  testng
BuildRequires:  xbean
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  xmlto
BuildRequires:  xmvn-install
BuildRequires:  xmvn-subst
BuildRequires:  mvn(org.codehaus.jcsp:jcsp)
BuildRequires:  mvn(org.codehaus.jsr166-mirror:extra166y)
BuildRequires:  mvn(org.jboss.netty:netty:3)
BuildRequires:  mvn(org.multiverse:multiverse-core)

Requires:       ant
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-lang3
Requires:       apache-ivy
Requires:       aqute-bndlib
Requires:       atinject
Requires:       aws-sdk-java-core
Requires:       aws-sdk-java-kms
Requires:       aws-sdk-java-s3
Requires:       base64coder
Requires:       bash
Requires:       beust-jcommander
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bsh2
Requires:       ecj
Requires:       glassfish-servlet-api
Requires:       google-gson
Requires:       google-guice
Requires:       guava20
Requires:       hawtjni-runtime
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jackson-annotations
Requires:       jackson-core
Requires:       jackson-databind
Requires:       jansi
Requires:       jansi-native
Requires:       jatl
Requires:       javapackages-tools
Requires:       jcifs
Requires:       jcip-annotations
Requires:       jcl-over-slf4j
Requires:       jetty-server
Requires:       jetty-util
Requires:       jgit
Requires:       joda-time
Requires:       jsch
Requires:       jsr-305
Requires:       jul-to-slf4j
Requires:       junit
Requires:       kryo
Requires:       log4j-over-slf4j
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       minlog
Requires:       native-platform
Requires:       nekohtml
Requires:       objectweb-asm
Requires:       objenesis
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       reflectasm
Requires:       rhino
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       tesla-polyglot-common
Requires:       testng
Requires:       xbean
Requires:       xerces-j2
Requires:       xml-commons-apis
Requires:       mvn(org.codehaus.groovy:groovy-all)
Recommends:     java-devel
Provides:       %{short_name} = %{gradle_version}

%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

This package is useful only for bootstrapping a repository that does
not have yet gradle, groovy and gpars built.

%package -n groovy-bootstrap
Version:        %{groovy_version}
Release:        0
Summary:        Bootstrap version of groovy-all JAR
License:        Apache-2.0
BuildArch:      noarch

%description -n groovy-bootstrap
Bootstrap version of the groovy-all.jar needed by xmvn-connector-gradle

This package is useful only for bootstrapping a repository that does
not have yet gradle, groovy and gpars built.


%package -n gpars-bootstrap
Version:        %{gpars_version}
Release:        0
Summary:        Bootstrap version of Groovy Parallel Systems
License:        Apache-2.0 AND SUSE-Public-Domain
BuildArch:      noarch

%description -n gpars-bootstrap
The GPars framework offers Java developers intuitive and safe ways to
handle Java or Groovy tasks concurrently. Leveraging the enormous
flexibility of the Groovy programming language and building on proven
Java technologies, we aim to make concurrent programming for
multi-core hardware intuitive, robust and enjoyable.

GPars is a multi-paradigm concurrency framework, offering several
mutually cooperating high-level concurrency abstractions, such as
Dataflow operators, Promises, CSP, Actors, Asynchronous Functions,
Agents and Parallel Collections.

This package is useful only for bootstrapping a repository that does
not have yet gradle, groovy and gpars built.

%prep
%setup -q -c -n %{short_name}-%{gradle_version}
cp %{SOURCE200} gpars-pom.xml

%pom_change_dep org.jboss.netty:netty:: ::3: gpars-pom.xml
%pom_change_dep :jsr166y:: :extra166y:: gpars-pom.xml

%build
# manpage build
mkdir man
asciidoc -b docbook -d manpage -o man/%{short_name}.xml %{SOURCE2}
xmlto man man/%{short_name}.xml -o man

%install
install -d -m 755 %{buildroot}%{_javadir}/%{short_name}/
ln -sf %{_bindir}/%{short_name} ./bin/%{short_name}

install -dm 0755 %{buildroot}%{_datadir}/%{short_name}
cp -r bin lib init.d %{buildroot}%{_datadir}/%{short_name}
# Launcher with dependencies needs to be in _javadir
# Dependencies of xmvn-connector-gradle need to have Maven metadata
for mod in launcher base-services core core-api resources \
        logging base-services-groovy model-core; do
    %{mvn_file} ":{gradle-$mod}" %{short_name}/@1
    %{mvn_artifact} org.gradle:gradle-$mod:%{gradle_version} ./lib/gradle-$mod-%{gradle_version}.jar
done
# this one is in lib/plugins
%{mvn_file} ":{gradle-dependency-management}" %{short_name}/@1
%{mvn_artifact} org.gradle:gradle-dependency-management:%{gradle_version} ./lib/plugins/gradle-dependency-management-%{gradle_version}.jar

# Temporary stuff
%{mvn_package} :groovy-{*} groovy
%{mvn_file} org.codehaus.groovy:groovy-{*} groovy/groovy-@1
%{mvn_artifact} %{SOURCE100} ./lib/groovy-all.jar

%{mvn_package} :gpars{*} gpars
%{mvn_file} :gpars{*} gpars/gpars@1
%{mvn_artifact} gpars-pom.xml %{SOURCE201}

%mvn_install

install -d -m 755 %{buildroot}%{_bindir}/
cat %{SOURCE1} | sed "s#@BASH@#$(which bash)#g" >gradle.sh
chmod +x gradle.sh
install -p -m 755 gradle.sh %{buildroot}%{_bindir}/%{short_name}

install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/%{short_name}.1 %{buildroot}%{_mandir}/man1/%{short_name}.1

xmvn-subst $(find %{buildroot}%{_datadir}/%{short_name} -type f -name \*.jar)
xmvn-subst -R %{buildroot} $(find %{buildroot}%{_datadir}/%{short_name} -type f -name \*.jar)

%files -f .mfiles
%{_bindir}/%{short_name}
%{_datadir}/%{short_name}
%{_mandir}/man1/%{short_name}.1%{?ext_man}

%files -n groovy-bootstrap -f .mfiles-groovy

%files -n gpars-bootstrap -f .mfiles-gpars

%changelog
