#
# spec file for package eclipse-ecf
#
# Copyright (c) 2020 SUSE LLC
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
%global _eclipsedir %{_libdir}/eclipse
# This exclude breaks the cyclic dependency on the platform to aide in
# bootstrapping
%global __requires_exclude .*org\.eclipse\.equinox.*
%global git_tag 10bfc24f030d889e7dfa36e3a77034ae2786c368
# Set this flag to avoid building additional providers when their
# dependencies are not available
%bcond_with providers
Version:        3.14.7
Release:        0
Summary:        Eclipse Communication Framework (ECF) Eclipse plug-in
# Note: The jive/smack provider is apache licensed
License:        EPL-1.0 AND Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/ecf/
Source0:        https://git.eclipse.org/c/ecf/org.eclipse.ecf.git/snapshot/org.eclipse.ecf-%{git_tag}.tar.xz
# Change how feature deps are specified, to avoid embedding versions
Patch0:         eclipse-ecf-feature-deps.patch
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-logging
BuildRequires:  eclipse-license
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  maven-plugin-build-helper
BuildRequires:  osgi-annotation
BuildRequires:  tycho-extras
BuildRequires:  xpp3-minimal
BuildConflicts: java-devel >= 9
%if %{with bootstrap}
Name:           eclipse-ecf-bootstrap
%else
Name:           eclipse-ecf
%endif
%if %{without bootstrap}
BuildRequires:  eclipse-ecf-core-bootstrap
BuildRequires:  eclipse-emf-core
BuildRequires:  eclipse-emf-runtime
BuildRequires:  eclipse-pde-bootstrap
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  jgit
BuildRequires:  tycho
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: log4j
%if %{with providers}
BuildRequires:  dnsjava
BuildRequires:  irclib
%endif
%else
BuildRequires:  tycho-bootstrap
#!BuildIgnore:  tycho
%endif

%description
ECF is a set of frameworks for building communications into applications and
services. It provides a lightweight, modular, transport-independent, fully
compliant implementation of the OSGi Remote Services standard.

%if %{with bootstrap}
%package   -n eclipse-ecf-core-bootstrap
%else
%package   core
Obsoletes:      eclipse-ecf-core-bootstrap
%endif
Summary:        Eclipse ECF Core
Group:          Development/Libraries/Java
Requires:       httpcomponents-client
Requires:       httpcomponents-core

%if %{with bootstrap}
%description -n eclipse-ecf-core-bootstrap
%else
%description core
%endif
ECF bundles required by eclipse-platform.

%if %{without bootstrap}
%package   runtime
Summary:        Eclipse Communication Framework (ECF) Eclipse plug-in
Group:          Development/Libraries/Java
BuildArch:      noarch

%description runtime
ECF is a set of frameworks for building communications into applications and
services. It provides a lightweight, modular, transport-independent, fully
compliant implementation of the OSGi Remote Services standard.

%package   sdk
Summary:        Eclipse ECF SDK
Group:          Development/Libraries/Java
BuildArch:      noarch

%description sdk
Documentation and developer resources for the Eclipse Communication Framework
(ECF) plug-in.
%endif

%prep
%setup -q -n org.eclipse.ecf-%{git_tag}

find . -type f -name "*.jar" -exec rm {} \;
find . -type f -name "*.class" -exec rm {} \;

%patch0 -p1

# Correction for content of runtime package
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.presence']" releng/features/org.eclipse.ecf.core/feature.xml

# Don't build examples or tests
sed -i -e '/<module>examples/d' -e '/<module>tests/d' pom.xml
%pom_disable_module releng/features/org.eclipse.ecf.tests.feature
%pom_disable_module releng/features/org.eclipse.ecf.eventadmin.examples.feature
%pom_disable_module releng/features/org.eclipse.ecf.remoteservice.examples.feature
%pom_disable_module releng/features/org.eclipse.ecf.remoteservice.sdk.examples.feature
%pom_xpath_remove "feature/requires/import[@feature='org.eclipse.ecf.remoteservice.sdk.examples.feature']" releng/features/org.eclipse.ecf.core/feature.xml
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.example.clients']" releng/features/org.eclipse.ecf.core/feature.xml
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.example.collab']" releng/features/org.eclipse.ecf.core/feature.xml

# Don't use target platform or jgit packaging bits
%pom_xpath_remove "pom:target"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:dependencies"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:sourceReferences"
%pom_xpath_remove "pom:plugin[pom:artifactId='tycho-packaging-plugin']/pom:configuration/pom:timestampProvider"
%pom_disable_module releng/org.eclipse.ecf.releng.repository

# Remove unnecesary dep on json
%pom_xpath_remove "feature/requires/import[@plugin='org.json']" releng/features/org.eclipse.ecf.remoteservice.rest.feature/feature.xml

# Using latest zookeeper requires non-trivial port
%pom_disable_module releng/features/org.eclipse.ecf.discovery.zookeeper.feature
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.zookeeper
%pom_xpath_remove "feature/includes[@id='org.eclipse.ecf.discovery.zookeeper.feature']" releng/features/org.eclipse.ecf.remoteservice.sdk.feature/feature.xml

# Using latest rome requires non-trivial port
%pom_disable_module releng/features/org.eclipse.ecf.remoteservice.rest.synd.feature
%pom_disable_module framework/bundles/org.eclipse.ecf.remoteservice.rest.synd

# Disable SLP provider, rhbz#1416706
%pom_disable_module releng/features/org.eclipse.ecf.discovery.slp.feature
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.jslp
%pom_disable_module protocols/bundles/ch.ethz.iks.slp
%pom_xpath_remove "feature/includes[@id='org.eclipse.ecf.discovery.slp.feature']" releng/features/org.eclipse.ecf.remoteservice.sdk.feature/feature.xml

# Misc other providers
%if %{without providers}
%pom_disable_module releng/features/org.eclipse.ecf.discovery.dnssd.feature
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.dnssd
%pom_disable_module protocols/bundles/org.jivesoftware.smack
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.xmpp.datashare
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.xmpp
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.xmpp.remoteservice
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.xmpp.ui
%pom_disable_module releng/features/org.eclipse.ecf.xmpp.feature
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.provider.xmpp.ui']" releng/features/org.eclipse.ecf.core/feature.xml
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.irc
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.irc.ui
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.provider.irc']" releng/features/org.eclipse.ecf.core/feature.xml
%pom_xpath_remove "feature/plugin[@id='org.eclipse.ecf.provider.irc.ui']" releng/features/org.eclipse.ecf.core/feature.xml
%endif

# Don't build bundles that are not relevant to our platform
%pom_disable_module providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient45.win32
%pom_xpath_remove "feature/plugin[@os='win32']" releng/features/org.eclipse.ecf.filetransfer.httpclient45.feature/feature.xml

# Use system libs
ln -s $(build-classpath osgi-annotation) osgi/bundles/org.eclipse.osgi.services.remoteserviceadmin/osgi/osgi.annotation.jar
%if %{with providers}
ln -s $(build-classpath xpp3-minimal) protocols/bundles/org.jivesoftware.smack/jars/xpp.jar
echo "Eclipse-BundleShape: dir" >> protocols/bundles/org.jivesoftware.smack/META-INF/MANIFEST.MF
ln -s $(build-classpath irclib) providers/bundles/org.eclipse.ecf.provider.irc/lib/irclib.jar
echo "Eclipse-BundleShape: dir" >> providers/bundles/org.eclipse.ecf.provider.irc/META-INF/MANIFEST.MF
%endif

%if %{with bootstrap}
# Only build core modules when bootstrapping
%pom_xpath_replace "pom:modules" "<modules>
<module>releng/features/org.eclipse.ecf.core.feature</module>
<module>releng/features/org.eclipse.ecf.core.ssl.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.httpclient4.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.httpclient4.ssl.feature</module>
<module>releng/features/org.eclipse.ecf.filetransfer.ssl.feature</module>
<module>framework/bundles/org.eclipse.ecf</module>
<module>framework/bundles/org.eclipse.ecf.identity</module>
<module>framework/bundles/org.eclipse.ecf.filetransfer</module>
<module>framework/bundles/org.eclipse.ecf.ssl</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient4</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient4.ssl</module>
<module>providers/bundles/org.eclipse.ecf.provider.filetransfer.ssl</module>
</modules>"
%endif

# TODO: Figure out why this is necessary....
sed -i -e '/Require-Bundle:/a\ org.eclipse.osgi.services,' framework/bundles/org.eclipse.ecf.console/META-INF/MANIFEST.MF

# Don't install poms
%{mvn_package} "::{pom,target}::" __noinstall

%if %{with bootstrap}
%{mvn_package} "::jar:{sources,sources-feature}:" __noinstall
%else
%{mvn_package} "::jar:{sources,sources-feature}:" sdk
%endif
%{mvn_package} ":org.eclipse.ecf.{core,sdk}" sdk
%{mvn_package} ":org.eclipse.ecf.docshare*" sdk
for p in $(grep '<plugin' releng/features/org.eclipse.ecf.core/feature.xml | sed -e 's/.*id="\(.*\)" d.*/\1/') ; do
%{mvn_package} ":$p" sdk
done
%{mvn_package} ":*.ui" sdk
%{mvn_package} ":*.ui.*" sdk
%{mvn_package} ":org.eclipse.ecf.remoteservice.sdk.*" sdk
%{mvn_package} ":org.eclipse.ecf.core.{,ssl.}feature"
%{mvn_package} ":org.eclipse.ecf.filetransfer.{,httpclient4.}{,ssl.}feature"
%{mvn_package} ":org.eclipse.ecf{,.identity,.ssl,.filetransfer}"
%{mvn_package} ":org.eclipse.ecf.provider.filetransfer*"
%{mvn_package} ":" runtime

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%%y %{SOURCE0})" +v%%Y%%m%%d-%%H%%M)
%{mvn_build} -j -f -- -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

# Move to libdir due to being part of core platform
install -d -m 755 %{buildroot}%{_eclipsedir}
mv %{buildroot}%{_datadir}/eclipse/droplets/ecf/{plugins,features} %{buildroot}%{_eclipsedir}
rm -r %{buildroot}%{_datadir}/eclipse/droplets/ecf

# Fixup metadata
sed -i -e 's|%{_datadir}/eclipse/droplets/ecf|%{_eclipsedir}|' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml
sed -i -e 's|%{_datadir}/eclipse/droplets/ecf/features/|%{_eclipsedir}/features/|' \
       -e 's|%{_datadir}/eclipse/droplets/ecf/plugins/|%{_eclipsedir}/plugins/|' .mfiles
sed -i -e '/droplets/d' .mfiles

# Remove any symlinks that might be created during bootstrapping due to missing platform bundles
for del in $( (cd %{buildroot}%{_eclipsedir}/plugins && ls | grep -v -e '^org\.eclipse\.ecf' ) ) ; do
rm %{buildroot}%{_eclipsedir}/plugins/$del
sed -i -e "/$del/d" .mfiles
done

# Symlink jars into javadir
install -d -m 755 %{buildroot}%{_javadir}/eclipse
location=%{_eclipsedir}/plugins
while [ "$location" != "/" ] ; do
    location=$(dirname $location)
    updir="$updir../"
done
pushd %{buildroot}%{_javadir}/eclipse
for J in ecf{,.identity,.ssl,.filetransfer,.provider.filetransfer{,.ssl,.httpclient4{,.ssl}}}  ; do
    DIR=$updir%{_eclipsedir}/plugins
    [ -e "`ls $DIR/org.eclipse.${J}_*.jar`" ] && ln -s $DIR/org.eclipse.${J}_*.jar ${J}.jar
done
popd

# Use system libs
%if %{without bootstrap}
%if %{with providers}
pushd %{buildroot}%{_datadir}/eclipse/droplets/ecf-sdk/plugins/org.eclipse.ecf.provider.irc_*
rm lib/irclib.jar && ln -s $(build-classpath irclib) lib/irclib.jar
popd
pushd %{buildroot}%{_datadir}/eclipse/droplets/ecf-runtime/plugins/org.jivesoftware.smack_*
rm jars/xpp.jar && ln -s $(build-classpath xpp3-minimal) jars/xpp.jar
popd
%endif
%endif

%fdupes -s %{buildroot}

%if %{with bootstrap}
%files -n eclipse-ecf-core-bootstrap -f .mfiles
%else
%files core -f .mfiles
%endif
%{_javadir}/eclipse

%if %{without bootstrap}
%files runtime -f .mfiles-runtime

%files sdk -f .mfiles-sdk
%endif

%changelog
