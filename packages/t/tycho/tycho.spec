#
# spec file for package tycho
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
# Release tags or git SHAs
%global git_tag tycho-%{version}
%global fp_p2_git_tag 290f67a4c717599b2f5166ea89aa5365571314b1
%global fp_p2_version 0.0.1
%global fp_p2_snap -SNAPSHOT
%define __requires_exclude osgi*
# Allow conditionally building without Junit 5 support
%bcond_without junit5
%if %{with bootstrap}
Name:           tycho-bootstrap
%else
Name:           tycho
%endif
Version:        1.2.0
Release:        0
Summary:        Plugins and extensions for building Eclipse plugins and OSGI bundles with Maven
# license file is missing but all files having some licensing information are ASL 2.0
License:        Apache-2.0 AND EPL-1.0
Group:          Development/Libraries/Java
URL:            https://eclipse.org/tycho
# Tycho project source
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.git/snapshot/org.eclipse.tycho-%{git_tag}.tar.xz
# Eclipse Plugin Project supporting filesystem as p2 repository
Source1:        https://github.com/rgrunber/fedoraproject-p2/archive/%{fp_p2_git_tag}/fedoraproject-p2-%{fp_p2_git_tag}.tar.gz
# this is a workaround for maven-plugin-plugin changes that happened after
# version 2.4.3 (impossible to have empty mojo created as aggregate). This
# should be fixed upstream properly
Source2:        EmptyMojo.java
Source3:        tycho-scripts.sh
Source4:        tycho-bootstrap.sh
Source5:        tycho-debundle.sh
# Script that can be used to install or simulate installation of P2
# artifacts. It is used in OSGi requires generation.
Source6:        p2-install.sh
Patch0:         tycho-fix-build.patch
# Submitted upstream: https://bugs.eclipse.org/bugs/show_bug.cgi?id=535564
Patch1:         tycho-maven-archiver-3.0.1.patch
Patch2:         tycho-use-custom-resolver.patch
Patch3:         tycho-maven-delegation.patch
# Changes needed for building against latest surefire
# Submitted upstream: https://bugs.eclipse.org/bugs/show_bug.cgi?id=537419
Patch4:         build-against-surefire-2.21.patch
Patch5:         build-against-surefire-2.22.patch
# Submitted upstream: https://bugs.eclipse.org/bugs/show_bug.cgi?id=537963
Patch6:         use-java8-for-default-ee.patch
# Build against org.apache.maven.surefire:surefire-junit-platform instead of
# against org.junit.platform:junit-platform-surefire-provider
Patch7:         port-to-surefire-junit-platform.patch
Patch100:       fedoraproject-p2-bootstrap-fix.patch
BuildRequires:  bash
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(de.pdark:decentxml)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)
BuildRequires:  mvn(org.apache.maven.surefire:maven-surefire-common)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-api)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-booter)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-logger-api)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.eclipse.tycho:org.eclipse.jdt.compiler.apt)
BuildRequires:  mvn(org.eclipse.tycho:org.eclipse.jdt.core)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-core)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-install)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-parent:pom:)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildRequires:  mvn(org.ow2.asm:asm-debug-all)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildConflicts: java-devel >= 9
Requires:       ecj >= 4.7.3a-1
# maven-clean-plugin is bound to "initialize" Maven phase for
# "eclipse-repository" projects
Requires:       maven-clean-plugin
Requires:       maven-local
Requires:       xmvn-minimal >= 3
BuildArch:      noarch
# Prebuilt Eclipse bundles needed to build Tycho when Eclipse is not present
# or when the Eclipse that is present is not compatible
%if %{with bootstrap}
Source10:       eclipse-bootstrap-photon.tar.xz
%endif
%if %{without bootstrap}
# Ordinarily Tycho additionally requires itself and Eclipse to build
BuildRequires:  %{name}-bootstrap
BuildRequires:  eclipse-platform-bootstrap >= 4.8.0
Requires:       eclipse-platform >= 4.8.0
Obsoletes:      %{name}-bootstrap
%else
# For bootstrapping, we just need the dependencies of the Eclipse bundles we use
BuildRequires:  osgi(com.ibm.icu)
BuildRequires:  osgi(javax.servlet-api)
BuildRequires:  osgi(javax.servlet.jsp)
BuildRequires:  osgi(org.apache.batik.css)
BuildRequires:  osgi(org.apache.commons.jxpath)
BuildRequires:  osgi(org.apache.felix.scr)
BuildRequires:  osgi(org.sat4j.core) >= 2.3.5
BuildRequires:  osgi(org.sat4j.pb) >= 2.3.5
BuildRequires:  osgi(org.w3c.css.sac)
%endif
%if %{with junit5}
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif

%description
Tycho is a set of Maven plugins and extensions for building Eclipse
plugins and OSGI bundles with Maven. Eclipse plugins and OSGI bundles
have their own metadata for expressing dependencies, source folder
locations, etc. that are normally found in a Maven POM. Tycho uses
native metadata for Eclipse plugins and OSGi bundles and uses the POM
to configure and drive the build. Tycho supports bundles, fragments,
features, update site projects and RCP applications. Tycho also knows
how to run JUnit test plugins using OSGi runtime and there is also
support for sharing build results using Maven artifact repositories.

Tycho plugins introduce new packaging types and the corresponding
lifecycle bindings that allow Maven to use OSGi and Eclipse metadata
during a Maven build. OSGi rules are used to resolve project
dependencies and package visibility restrictions are honored by the
OSGi-aware JDT-based compiler plugin. Tycho will use OSGi metadata and
OSGi rules to calculate project dependencies dynamically and injects
them into the Maven project model at build time. Tycho supports all
attributes supported by the Eclipse OSGi resolver (Require-Bundle,
Import-Package, Eclipse-GenericRequire, etc). Tycho will use proper
classpath access rules during compilation. Tycho supports all project
types supported by PDE and will use PDE/JDT project metadata where
possible. One important design goal in Tycho is to make sure there is
no duplication of metadata between POM and OSGi metadata.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n org.eclipse.tycho-%{git_tag} -a 1
mv fedoraproject-p2-%{fp_p2_git_tag} fedoraproject-p2

%patch0 -p1
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6 -p1
%patch7 -p1
%patch100

# Unneeded for RPM builds
%pom_remove_plugin :maven-site-plugin

%if %{without junit5}
%pom_disable_module org.eclipse.tycho.surefire.junit5 tycho-surefire
%pom_remove_dep ":org.eclipse.tycho.surefire.junit5" tycho-surefire/tycho-surefire-plugin
%endif

# Switch for "tycho" platform deps
%pom_change_dep org.eclipse.jdt: org.eclipse.tycho: . tycho-compiler-jdt

# Move from org.sonatype.aether to org.eclipse.aether
find . -name "*.java" | xargs sed -i 's/org.sonatype.aether/org.eclipse.aether/g'
find . -name "*.java" | xargs sed -i 's/org.eclipse.aether.util.DefaultRepositorySystemSession/org.eclipse.aether.DefaultRepositorySystemSession/g'
sed -i 's/public int getPriority/public float getPriority/g' tycho-core/src/main/java/org/eclipse/tycho/core/p2/P2RepositoryConnectorFactory.java

# place empty mojo in place
mkdir -p tycho-maven-plugin/src/main/java/org/fedoraproject
pushd tycho-maven-plugin/src/main/java/org/fedoraproject
cp %{SOURCE2} .
popd

# These units cannot be found during a regular build
sed -i '/^<unit id=.*$/d' tycho-bundles/tycho-bundles-target/tycho-bundles-target.target

# we don't have org.apache.commons:commons-compress:jar:sources
%pom_xpath_remove "pom:dependency[pom:classifier='sources' and pom:artifactId='commons-compress']" tycho-p2/tycho-p2-director-plugin

# Previously, JUnit would re-export Hamcrest
# Now modules using org.hamcrest.core must state the requirement explicitly
for mod in tycho-bundles/org.eclipse.tycho.{p2.{maven.repository.tests,resolver.impl.test,tools.tests},test.utils,core.shared.tests}; do
  sed -i 's/^Require-Bundle://
          /org\.junit/ i Require-Bundle: org.hamcrest.core,' \
          $mod/META-INF/MANIFEST.MF
done

# Fix bundle names
sed -i -e 's/org\.hamcrest/org.hamcrest.core/' tycho-bundles/pom.xml
sed -i -e 's/org\.mockito/org.mockito.mockito-core/' \
  tycho-bundles/org.eclipse.tycho.p2.tools.tests/META-INF/MANIFEST.MF \
  tycho-bundles/org.eclipse.tycho.p2.maven.repository.tests/META-INF/MANIFEST.MF \
  tycho-bundles/org.eclipse.tycho.p2.resolver.shared.tests/META-INF/MANIFEST.MF

# Bootstrap Build
%if %{with bootstrap}

# Don't build tests when bootstrapping
for b in core.shared.tests p2.resolver.impl.test p2.resolver.shared.tests p2.maven.repository.tests p2.tools.tests test.utils ; do
  %pom_disable_module org.eclipse.tycho.$b tycho-bundles
done
%pom_disable_module org.fedoraproject.p2.tests fedoraproject-p2
%pom_remove_dep -r :::test

# Unpack a compatible version of Eclipse we can use to build against
tar -xf %{SOURCE10}
# Install OSGi bundles into local repo to override any incompatible system version
# that may be already installed
pushd bootstrap
for f in usr/lib/eclipse/plugins/org.eclipse.osgi.compatibility.state_*.jar \
         usr/lib/eclipse/plugins/org.eclipse.osgi_*.jar ; do
  xmvn -o install:install-file -Dfile=$f -Dpackaging=jar -DgroupId=org.eclipse.tycho -Dmaven.repo.local=$(pwd)/../.m2 \
    -DartifactId=$(echo $(basename $f) | cut -d_ -f1) -Dversion=$(echo "${f%.jar}" | cut -d_ -f2)
done
popd

# Perform the 'minimal' (bootstrap) build of Tycho
cp %{SOURCE3} %{SOURCE4} .
bash tycho-bootstrap.sh %{version}

# Non-Bootstrap Build
%else

# Set some temporary build version so that the bootstrapped build has
# a different version from the nonbootstrapped. Otherwise there will
# be cyclic dependencies.

sysVer=`grep -C 1 "<artifactId>tycho</artifactId>" %{_mavenpomdir}/tycho/tycho.pom | grep "version" | sed 's/.*>\(.*\)<.*/\1/'`
mkdir boot
sed -e 's/ns[0-9]://g' %{_datadir}/maven-metadata/tycho-bootstrap.xml > boot/tycho-metadata.xml

# Copy Tycho POMs from system repo and set their versions to %%{version}-SNAPSHOT.
for pom in $(grep 'pom</path>' boot/tycho-metadata.xml | sed 's|.*>\(.*\)<.*|\1|'); do
    sed -e "s/>$sysVer/>%{version}-SNAPSHOT/g" -e "s/%{fp_p2_version}%{fp_p2_snap}/%{fp_p2_version}/" <$pom >boot/$(basename $pom)
done

# Update Maven lifecycle mappings for Tycho packaging types provided by tycho-maven-plugin.
cp -p $(build-classpath tycho/tycho-maven-plugin) boot/tycho-maven-plugin.jar
jar xf boot/tycho-maven-plugin.jar META-INF/plexus/components.xml
sed -i s/$sysVer/%{version}-SNAPSHOT/ META-INF/plexus/components.xml
jar uf boot/tycho-maven-plugin.jar META-INF/plexus/components.xml

# Create XMvn metadata for the new JARs and POMs by customizing system Tycho metadata.
sed -i '
  s|>/[^<]*/\([^/]*\.pom\)</path>|>'$PWD'/boot/\1</path>|
  s|>'$sysVer'</version>|>%{version}-SNAPSHOT</version><compatVersions><version>%{version}-SNAPSHOT</version></compatVersions>|
  s|>'%{fp_p2_version}%{fp_p2_snap}'</version>|>%{fp_p2_version}</version><compatVersions><version>%{fp_p2_version}</version></compatVersions>|
  s|%{_javadir}/tycho/tycho-maven-plugin.jar|'$PWD'/boot/tycho-maven-plugin.jar|
' boot/tycho-metadata.xml
%{mvn_config} resolverSettings/metadataRepositories/repository $PWD/boot/tycho-metadata.xml
%endif

# Avoid duplicate execution of clean when generating javadocs, see ebz#399756
%pom_add_plugin :maven-clean-plugin tycho-bundles/tycho-standalone-p2-director "
<executions>
  <execution>
    <id>default-clean-1</id>
    <phase>initialize</phase>
    <configuration>
      <skip>true</skip>
    </configuration>
  </execution>
</executions>"

# Add fp-p2 to main build
%pom_xpath_inject "pom:modules" "<module>fedoraproject-p2</module>"

%mvn_file :{*} tycho/@1

%build
%if %{with bootstrap}
%global no_javadoc "-j"
%else
%global no_javadoc %{nil}
%endif
%{mvn_build} %{no_javadoc} -f -- \
  -Dtycho-version=%{version}-SNAPSHOT -DtychoBootstrapVersion=%{version}-SNAPSHOT \
  -Dmaven.repo.local=$(pwd)/.m2 -Dfedora.p2.repos=$(pwd)/bootstrap

%{mvn_artifact} fedoraproject-p2/org.fedoraproject.p2/pom.xml

# Relying on xmvn p2 plugin being present would be a circular dep
# So install as if all artifacts are normal jar files
sed -i -e 's|type>eclipse.*<|type>jar<|' .xmvn-reactor

# Don't package target platform definition files
%{mvn_package} "::target::" __noinstall
# Don't package fp-p2 tests
%{mvn_package} ":org.fedoraproject.p2.tests" __noinstall

%install
# Get debundling scripts
cp %{SOURCE3} %{SOURCE5} .

%if ! %{with bootstrap}
# Debundle p2 runtime
bash tycho-debundle.sh $(pwd)/tycho-bundles/tycho-bundles-external \
  $(pwd)/tycho-bundles/tycho-bundles-external/target/tycho-bundles-external-manifest.txt

# Debundle standalone p2 director
bash tycho-debundle.sh $(pwd)/tycho-bundles/tycho-standalone-p2-director
%endif

%if %{with bootstrap}
# Install our own copy of OSGi runtime when bootstrapping to avoid external dep on Eclipse
for b in org.eclipse.osgi \
         org.eclipse.osgi.compatibility.state ; do
  osgiJarPath=$(find .m2/org/eclipse/tycho/$b/*/ -name "*.jar")
  osgiPomPath=$(find .m2/org/eclipse/tycho/$b/*/ -name "*.pom")
  %{mvn_artifact} $osgiPomPath $osgiJarPath
  %{mvn_alias} "org.eclipse.tycho:$b" "org.eclipse.osgi:$b"
done
%endif

%mvn_install

%if ! %{with bootstrap}
install -pm 644 tycho-bundles/tycho-bundles-external/target/tycho-bundles-external-manifest.txt %{buildroot}%{_javadir}/tycho
%add_maven_depmap org.eclipse.tycho:tycho-bundles-external:txt:manifest:%{version} tycho/tycho-bundles-external-manifest.txt
%endif

%if %{with bootstrap}
# Misc other bundles needed for bootstrapping
for bnd in \
  core.contenttype \
  core.expressions \
  core.filesystem \
  core.jobs \
  core.net \
  core.resources \
  core.runtime \
  equinox.app \
  equinox.common \
  equinox.concurrent \
  equinox.preferences \
  equinox.registry \
  equinox.security ; do
bndJarPath=$(find bootstrap -name "org.eclipse.${bnd}_*.jar")
install -m 644 -T $bndJarPath %{buildroot}%{_javadir}/tycho/$bnd.jar
done
%endif

# For some reason fp-p2 is treated as a compat version, this prevents that
# TODO: figure out why
sed -i '/<resolvedVersion>/d' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml

# p2-install script
install -dm 755 %{buildroot}%{_javadir}-utils/
install -pm 755 %{SOURCE6} %{buildroot}%{_javadir}-utils/

# Symlink XMvn P2 plugin with all dependencies so that it can be loaded by XMvn
xmvn_libdir=$(realpath $(dirname $(readlink -f $(which xmvn)))/../lib)
install -dm 755 %{buildroot}${xmvn_libdir}/installer/
%if %{with bootstrap}
ln -s %{_javadir}/tycho/org.eclipse.osgi.jar %{buildroot}${xmvn_libdir}/installer/
%else
ln -s %{_javadir}/eclipse/osgi.jar %{buildroot}${xmvn_libdir}/installer/
%endif
ln -s %{_javadir}/tycho/xmvn-p2-installer-plugin.jar %{buildroot}${xmvn_libdir}/installer/
ln -s %{_javadir}/tycho/org.fedoraproject.p2.jar %{buildroot}${xmvn_libdir}/installer/

%files -f .mfiles
%if %{with bootstrap}
%{_javadir}/tycho/core.*.jar
%{_javadir}/tycho/equinox.*.jar
%endif
%{_datadir}/xmvn/lib/installer
%{_javadir}-utils/p2-install.sh
%doc README.md

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%endif

%changelog
