#
# spec file for package eclipse
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
%global eb_commit       44643cbda3dfd6f00fbf1b346dae7068df2a9ef9
%global eclipse_date    20180906
%global eclipse_time    0745
%global short_version   4.9
%global eclipse_tag     I%{eclipse_date}-%{eclipse_time}
%global _jetty_version  9.4.11
%global _lucene_version 7.1.0
%define __requires_exclude .*SUNWprivate_1\\.1.*
%ifarch %{ix86}
    %global eclipse_arch x86
%endif
%ifarch %{arm}
    %global eclipse_arch arm
%endif
%ifarch ppc64 ppc64p7
    %global eclipse_arch ppc64
%endif
%ifarch s390x x86_64 aarch64 ppc64le
    %global eclipse_arch %{_arch}
%endif
# Desktop file information
%global app_name %{?app_name_prefix}%{!?app_name_prefix:Eclipse}
%global app_exec %{?app_exec_prefix} eclipse
%global _eclipsedir %{_libdir}/eclipse
%global use_wayland 0
Version:        %{short_version}.0
Release:        0
Summary:        An open, extensible IDE
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/
# eclipse-create-tarball.sh
Source0:        eclipse-platform-sources-%{short_version}-clean.tar.xz
Source1:        http://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/snapshot/org.eclipse.linuxtools.eclipse-build-%{eb_commit}.tar.xz
Source100:      eclipse-create-tarball.sh
# Eclipse should not include source for dependencies that are not supplied by this package
# and should not include source for bundles that are not relevant to our platform
Patch0:         eclipse-no-source-for-dependencies.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=377515
Patch1:         eclipse-p2-pick-up-renamed-jars.patch
# Patch for this was contributed. Unlikely to be released.
Patch2:         eclipse-ignore-version-when-calculating-home.patch
# CBI uses timestamps generated from the git commits. We don't have the repo,
# just source, and we don't want additional dependencies.
Patch3:         eclipse-remove-jgit-provider.patch
Patch4:         eclipse-secondary-arches.patch
Patch5:         eclipse-debug-symbols.patch
Patch6:         eclipse-test-support.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=408138
Patch12:        eclipse-fix-dropins.patch
# org.mockito -> org.mockito.mockito-core
# org.hamcrest-> org.hamcrest.core
Patch14:        eclipse-mockito.patch
Patch15:        eclipse-support-symlink-bundles.patch
# Feature plugin definitions lock onto version of plugin at build-time.
# If plugin is external, updating it breaks the feature. (version changes)
# Workaround : Change <plugin> definition to a 'requirement'
# Also makes the following BSN changes at the same time:
# com.sun.el -> com.sun.el.javax.el
# javax.el -> javax.el-api
# javax.servlet -> javax.servlet-api
# org.apache.jasper.glassfish -> org.glassfish.web.javax.servlet.jsp
# javax.annotation -> removed
# org.w3c.dom.smil -> removed
Patch16:        eclipse-feature-plugins-to-category-ius.patch
# Fix various JDT and PDE tests
Patch20:        eclipse-fix-tests.patch
# Droplet fixes
Patch21:        eclipse-adjust-droplets.patch
Patch22:        eclipse-pde-tp-support-droplets.patch
# Only build gtk3 backend for SWT
Patch23:        eclipse-swt-disable-gtk2.patch
# Disable uses by default
Patch24:        eclipse-disable-uses-constraints.patch
# Droplet fixes
Patch26:        eclipse-make-droplets-runnable.patch
Patch27:        eclipse-disable-droplets-in-dropins.patch
# Temporary measure until wayland improves
Patch28:        prefer_x11_backend.patch
# Fix errors when building ant launcher
Patch29:        fix_ant_build.patch
# Hide the p2 Droplets from cluttering Install Wizard Combo
Patch30:        eclipse-hide-droplets-from-install-wizard.patch
# Adapt the symlinks to the openSUSE install of batik
Patch31:        eclipse-suse-batik.patch
# Fix build of ImageDescriptor.createImage(boolean, Device)
Patch32:        eclipse-imagedescriptor.patch
# Fix build on ppc64 big endian
Patch33:        eclipse-ppc64.patch
# Fix build with objectweb-asm 7
Patch34:        eclipse-asm7.patch
Patch35:        eclipse-arm32.patch
Patch36:        eclipse-force-gtk2.patch
Patch37:        eclipse-felix-scr-dependencies.patch
Patch38:        eclipse-lucene-8.patch
Patch39:        eclipse-gcc10.patch
BuildRequires:  ant >= 1.10.5
BuildRequires:  ant-antlr
BuildRequires:  ant-apache-bcel
BuildRequires:  ant-apache-bsf
BuildRequires:  ant-apache-log4j
BuildRequires:  ant-apache-oro
BuildRequires:  ant-apache-regexp
BuildRequires:  ant-apache-resolver
BuildRequires:  ant-apache-xalan2
BuildRequires:  ant-commons-logging
BuildRequires:  ant-commons-net
BuildRequires:  ant-javamail
BuildRequires:  ant-jdepend
BuildRequires:  ant-jmf
BuildRequires:  ant-jsch
BuildRequires:  ant-junit
BuildRequires:  ant-junit5
BuildRequires:  ant-swing
BuildRequires:  ant-testutil
BuildRequires:  ant-xz
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-el >= 1.0
BuildRequires:  apache-commons-fileupload
BuildRequires:  apache-commons-jxpath
BuildRequires:  apache-commons-logging
BuildRequires:  apiguardian
BuildRequires:  atinject
BuildRequires:  batik >= 1.10
BuildRequires:  batik-css >= 1.10
BuildRequires:  cbi-plugins
BuildRequires:  desktop-file-utils
BuildRequires:  easymock
BuildRequires:  eclipse-license2
BuildRequires:  gcc
BuildRequires:  glassfish-el > 3.0.0
BuildRequires:  glassfish-el-api > 3.0.0
BuildRequires:  glassfish-jsp >= 2.2.5
BuildRequires:  glassfish-jsp-api >= 2.2.1
BuildRequires:  glassfish-servlet-api >= 3.1.0
BuildRequires:  hamcrest
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  icu4j >= 62.1
BuildRequires:  jgit
BuildRequires:  jsch >= 0.1.46
BuildRequires:  jsoup
BuildRequires:  junit >= 4.12
BuildRequires:  junit5
BuildRequires:  lucene-analysis >= %{_lucene_version}
BuildRequires:  lucene-analyzers-smartcn >= %{_lucene_version}
BuildRequires:  lucene-core >= %{_lucene_version}
BuildRequires:  lucene-queryparser >= %{_lucene_version}
BuildRequires:  make
BuildRequires:  maven-local
BuildRequires:  mockito
BuildRequires:  objectweb-asm >= 6.1.1
BuildRequires:  osgi-compendium
BuildRequires:  pkgconfig
BuildRequires:  rhino
BuildRequires:  rsync
BuildRequires:  sac
BuildRequires:  sat4j
BuildRequires:  sonatype-oss-parent
BuildRequires:  tycho-extras
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-maven-plugin
BuildRequires:  xmlgraphics-commons >= 2.2
BuildRequires:  xz-java
BuildRequires:  zip
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  osgi(javax.servlet-api)
BuildRequires:  osgi(org.apache.felix.gogo.command) >= 1.0.2
BuildRequires:  osgi(org.apache.felix.gogo.runtime) >= 1.1.0
BuildRequires:  osgi(org.apache.felix.gogo.shell) >= 1.1.0
BuildRequires:  osgi(org.apache.felix.scr) >= 2.0.14
BuildRequires:  osgi(org.eclipse.jetty.continuation) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.http) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.io) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.security) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.server) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.servlet) >= %{_jetty_version}
BuildRequires:  osgi(org.eclipse.jetty.util) >= %{_jetty_version}
BuildRequires:  osgi(osgi.annotation)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildConflicts: java-devel >= 9
%if %{with bootstrap}
Name:           eclipse-bootstrap
%else
Name:           eclipse
%endif
# Build deps that are excluded when bootstrapping
%if %{without bootstrap}
# For contributor tools
BuildRequires:  eclipse-ecf-core >= 3.14.1
BuildRequires:  eclipse-egit
BuildRequires:  eclipse-emf-core > 2.14.99
BuildRequires:  eclipse-emf-runtime
BuildRequires:  eclipse-pde-bootstrap
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  tycho
#!BuildIgnore:  eclipse-ecf-core-bootstrap
#!BuildIgnore:  eclipse-emf-core-bootstrap
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
%else
BuildRequires:  eclipse-ecf-core-bootstrap
BuildRequires:  eclipse-emf-core-bootstrap
BuildRequires:  tycho-bootstrap
#!BuildIgnore:  eclipse-ecf-core
#!BuildIgnore:  eclipse-emf-core
#!BuildIgnore:  tycho
%endif

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%if %{with bootstrap}
%package        -n eclipse-swt-bootstrap
%else
%package        swt
Obsoletes:      eclipse-swt-bootstrap
%endif
Summary:        SWT Library for GTK+
Group:          Development/Libraries/Java
Requires:       gtk3
Requires:       java-headless >= 1.8.0
Requires:       javapackages-tools
Requires:       libwebkit2gtk-4_0-37

%if %{with bootstrap}
%description -n eclipse-swt-bootstrap
%else
%description swt
%endif
SWT Library for GTK+.

%if %{with bootstrap}
%package        -n eclipse-equinox-osgi-bootstrap
%else
%package        equinox-osgi
Obsoletes:      eclipse-equinox-osgi-bootstrap
%endif
Summary:        Eclipse OSGi - Equinox
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8.0
Requires:       javapackages-tools
Provides:       osgi(system.bundle) = %{version}

%if %{with bootstrap}
%description  -n eclipse-equinox-osgi-bootstrap
%else
%description  equinox-osgi
%endif
Eclipse OSGi - Equinox

%if %{with bootstrap}
%package        -n eclipse-platform-bootstrap
%else
%package        platform
Obsoletes:      eclipse-platform-bootstrap
%endif
Summary:        Eclipse platform common files
Group:          Development/Libraries/Java
Requires:       ant >= 1.10.5
Requires:       ant-antlr
Requires:       ant-apache-bcel
Requires:       ant-apache-bsf
Requires:       ant-apache-log4j
Requires:       ant-apache-oro
Requires:       ant-apache-regexp
Requires:       ant-apache-resolver
Requires:       ant-apache-xalan2
Requires:       ant-commons-logging
Requires:       ant-commons-net
Requires:       ant-javamail
Requires:       ant-jdepend
Requires:       ant-jmf
Requires:       ant-jsch
Requires:       ant-junit
Requires:       ant-junit5
Requires:       ant-swing
Requires:       ant-testutil
Requires:       ant-xz
Requires:       apache-commons-codec
Requires:       apache-commons-el >= 1.0
Requires:       apache-commons-jxpath
Requires:       apache-commons-logging
Requires:       atinject
Requires:       batik >= 1.10
Requires:       batik-css >= 1.10
Requires:       glassfish-el > 3.0.0
Requires:       glassfish-el-api > 3.0.0
Requires:       glassfish-jsp >= 2.2.5
Requires:       glassfish-jsp-api >= 2.2.1
Requires:       glassfish-servlet-api >= 3.1.0
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       icu4j >= 62.1
Requires:       jsch >= 0.1.46
Requires:       osgi-compendium
Requires:       sac
Requires:       sat4j
Requires:       xml-commons-apis
Requires:       xmlgraphics-commons >= 2.2
Requires:       osgi(org.apache.felix.gogo.command) >= 1.0.2
Requires:       osgi(org.apache.felix.gogo.runtime) >= 1.0.4
Requires:       osgi(org.apache.felix.gogo.shell) >= 1.0.0
Requires:       osgi(org.apache.felix.scr) >= 2.0.14
Requires:       osgi(org.eclipse.jetty.continuation) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.http) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.io) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.security) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.server) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.servlet) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.util) >= %{_jetty_version}
Requires:       osgi(org.tukaani.xz)
%requires_ge    lucene-analysis
%requires_ge    lucene-analyzers-smartcn
%requires_ge    lucene-core
%requires_ge    lucene-queryparser

%if %{with bootstrap}
Requires:       eclipse-equinox-osgi-bootstrap = %{version}-%{release}
Requires:       eclipse-swt-bootstrap = %{version}-%{release}
%else
Requires:       %{name}-equinox-osgi = %{version}-%{release}
Requires:       %{name}-swt = %{version}-%{release}
Requires:       eclipse-ecf-core >= 3.14.0
Requires:       eclipse-emf-core >= 2.14.0
%endif

%if %{with bootstrap}
%description    -n eclipse-platform-bootstrap
%else
%description    platform
%endif
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%if %{with bootstrap}
%package        -n eclipse-jdt-bootstrap
Requires:       eclipse-platform-bootstrap = %{version}-%{release}
%else
%package        jdt
Requires:       %{name}-platform = %{version}-%{release}
Obsoletes:      eclipse-jdt-bootstrap
%endif
Summary:        Eclipse Java Development Tools
Group:          Development/Libraries/Java
Requires:       osgi(org.hamcrest.core)
Requires:       osgi(org.junit) >= 4.12
BuildArch:      noarch

%if %{with bootstrap}
%description    -n eclipse-jdt-bootstrap
%else
%description    jdt
%endif
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%if %{with bootstrap}
%package        -n eclipse-pde-bootstrap
Requires:       eclipse-jdt-bootstrap = %{version}-%{release}
Requires:       eclipse-platform-bootstrap = %{version}-%{release}
%else
%package        pde
Requires:       %{name}-jdt = %{version}-%{release}
Requires:       %{name}-platform = %{version}-%{release}
Obsoletes:      eclipse-pde-bootstrap
%endif
Summary:        Eclipse Plugin Development Environment
Group:          Development/Libraries/Java
Requires:       objectweb-asm >= 6.1.1

%if %{with bootstrap}
%description    -n eclipse-pde-bootstrap
%else
%description    pde
%endif
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%if %{with bootstrap}
%package        -n eclipse-p2-discovery-bootstrap
Requires:       eclipse-platform-bootstrap = %{version}-%{release}
%else
%package        p2-discovery
Requires:       %{name}-platform = %{version}-%{release}
Obsoletes:      eclipse-p2-discovery-bootstrap
%endif
Summary:        Eclipse p2 Discovery
Group:          Development/Libraries/Java
BuildArch:      noarch

%if %{with bootstrap}
%description    -n eclipse-p2-discovery-bootstrap
%else
%description    p2-discovery
%endif
The p2 Discovery mechanism provides a simplified and branded front-end for the
p2 provisioning platform. Discovery can be used as a tool to display and
install from existing P2 repositories or as a framework to build branded
installer UIs.

%if %{with bootstrap}
%package        -n eclipse-contributor-tools-bootstrap
Requires:       eclipse-platform-bootstrap = %{version}-%{release}
%else
%package        contributor-tools
Requires:       %{name}-platform = %{version}-%{release}
Obsoletes:      eclipse-contributor-tools-bootstrap
%endif
Summary:        Tools for Eclipse Contributors
Group:          Development/Libraries/Java
Requires:       easymock
Requires:       mockito

%if %{with bootstrap}
%description    -n eclipse-contributor-tools-bootstrap
%else
%description    contributor-tools
%endif
This package contains tools specifically for Eclipse contributors. It includes
SWT tools, E4 tools, Rel-Eng tools and Eclipse Test frameworks.

%if %{with bootstrap}
%package        -n eclipse-tests-bootstrap
Requires:       eclipse-contributor-tools-bootstrap = %{version}-%{release}
%else
%package        tests
Requires:       %{name}-contributor-tools = %{version}-%{release}
Obsoletes:      eclipse-tests-bootstrap
%endif
Summary:        Eclipse Tests
Group:          Development/Libraries/Java

%if %{with bootstrap}
%description    -n eclipse-tests-bootstrap
%else
%description    tests
%endif
Eclipse Tests.

%prep
%setup -q -n eclipse-platform-sources-%{eclipse_tag}

# Extract linuxtools/eclipse-build sources
tar --strip-components=1 -xf %{SOURCE1}

%patch0
%patch1
%patch2
%patch3
%patch4 -p1
%patch5
#%patch6
%patch12
%patch14
%patch15
%patch16
%patch20
%patch21
%patch22
#%patch23
%patch24
%patch26
%patch27
%if ! %{use_wayland}
%patch28
%endif
%patch29
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%ifarch s390 %{arm} %{ix86} ppc
%patch36 -p1
%endif
%patch37 -p1
%if %{?pkg_vcmp:%pkg_vcmp lucene-core >= 8}%{!?pkg_vcmp:0}
%patch38 -p1
%endif
%patch39 -p1

# Use ecj when bootstrapping
%if %{with bootstrap}
sed -i -e 's/groupId>org.eclipse.jdt</groupId>org.eclipse.tycho</' eclipse-platform-parent/pom.xml
%endif

# Resolving the target platform requires too many changes, so don't use it
%pom_xpath_remove "pom:configuration/pom:target" eclipse-platform-parent

# Disable as many products as possible to make the build faster, we care only for the IDE
%pom_disable_module platform.sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module rcp eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module rcp.sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module rcp.config eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module equinox-sdk eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module equinox.starterkit.product eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module eclipse.platform.repository eclipse.platform.releng.tychoeclipsebuilder

# Disable bundles that we don't ship as part of the remaining products
%pom_disable_module bundles/org.eclipse.equinox.cm.test rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.sdk rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.console.jaas.fragment rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.console.ssh rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.ip rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.transforms.xslt rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.transforms.hook rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.caching.j9 rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.caching rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.weaving.hook rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.compendium.sdk rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.core.sdk rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.p2.sdk rt.equinox.p2
%pom_disable_module features/org.eclipse.equinox.server.p2 rt.equinox.bundles
%pom_disable_module features/org.eclipse.equinox.serverside.sdk rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.p2.tests.reconciler.product rt.equinox.p2
%pom_disable_module bundles/org.eclipse.equinox.p2.artifact.optimizers rt.equinox.p2
%pom_disable_module bundles/org.eclipse.equinox.p2.artifact.processors rt.equinox.p2

# Don't need annotations for obsolete JDKs
%pom_disable_module org.eclipse.jdt.annotation_v1 eclipse.jdt.core
%pom_xpath_remove "plugin[@version='1.1.300.qualifier']" eclipse.jdt/org.eclipse.jdt-feature/feature.xml
sed -i -e '/org\.eclipse\.jdt\.annotation;bundle-version="\[1\.1\.0,2\.0\.0)"/d' \
  eclipse.jdt.core/org.eclipse.jdt.core.tests.{model,builder,compiler}/META-INF/MANIFEST.MF \
  eclipse.jdt.core/org.eclipse.jdt.apt.pluggable.tests/META-INF/MANIFEST.MF \
  eclipse.jdt.ui/org.eclipse.jdt.ui.tests/META-INF/MANIFEST.MF

# Disable examples
%pom_disable_module bundles/org.eclipse.sdk.examples eclipse.platform.releng
%pom_disable_module features/org.eclipse.sdk.examples-feature eclipse.platform.releng
%pom_disable_module examples/org.eclipse.swt.examples.ole.win32 eclipse.platform.swt

# Disable servletbridge stuff
%pom_disable_module bundles/org.eclipse.equinox.http.servletbridge rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.servletbridge rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.servletbridge.template rt.equinox.bundles

# This part generates secondary fragments using primary fragments
for dir in rt.equinox.binaries rt.equinox.framework/bundles eclipse.platform.swt.binaries/bundles ; do
  utils/ensure_arch.sh "$dir" x86 arm
  utils/ensure_arch.sh "$dir" x86_64 aarch64 ppc64
done

# Remove platform-specific stuff that we don't care about to reduce build time
# (i.e., all bundles that are not applicable to the current build platform --
# this reduces the build time on arm by around 20 minutes per architecture that
# we are not currently building)
TYCHO_ENV="<environment><os>linux</os><ws>gtk</ws><arch>%{eclipse_arch}</arch></environment>"
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV" eclipse-platform-parent
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV" eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV" eclipse.platform.ui/bundles/org.eclipse.e4.ui.swt.gtk
for b in `ls eclipse.platform.swt.binaries/bundles | grep -P -e 'org.eclipse.swt\.(?!gtk\.linux.%{eclipse_arch}$)'` ; do
  module=$(grep ">bundles/$b<" eclipse.platform.swt.binaries/pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module bundles/$b eclipse.platform.swt.binaries
    %pom_xpath_inject "pom:excludes" "<plugin id='$b'/>" eclipse.platform.ui/features/org.eclipse.e4.rcp
  fi
done
for b in `ls rt.equinox.framework/bundles | grep -P -e 'org.eclipse.equinox.launcher\.(?!gtk\.linux.%{eclipse_arch}$)'` ; do
  module=$(grep ">bundles/$b<" rt.equinox.framework/pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module bundles/$b rt.equinox.framework
    %pom_xpath_remove -f "plugin[@id='$b']" rt.equinox.framework/features/org.eclipse.equinox.executable.feature/feature.xml
  fi
done
for b in `(cd rt.equinox.bundles/bundles && ls -d *{macosx,win32,linux}*) | grep -P -e 'org.eclipse.equinox.security\.(?!linux\.%{eclipse_arch}$)'` ; do
  %pom_disable_module bundles/$b rt.equinox.bundles
  %pom_xpath_remove "plugin[@id='$b']" rt.equinox.p2/features/org.eclipse.equinox.p2.core.feature/feature.xml
done
for b in `ls eclipse.platform.team/bundles/org.eclipse.core.net/fragments/ | grep -P -e 'org.eclipse.core.net\.(?!linux.%{eclipse_arch}$)'` ; do
  %pom_disable_module bundles/org.eclipse.core.net/fragments/$b eclipse.platform.team
done
for b in `ls eclipse.platform.resources/bundles/ | grep -P -e 'org.eclipse.core.filesystem\.(?!linux\.%{eclipse_arch}$)'` ; do
  module=$(grep ">bundles/$b<" eclipse.platform.resources/pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module bundles/$b eclipse.platform.resources
    %pom_xpath_remove -f "plugin[@id='$b']" eclipse.platform.resources/tests/org.eclipse.core.tests.filesystem.feature/feature.xml
  fi
done
%pom_disable_module org.eclipse.jdt.launching.macosx eclipse.jdt.debug
%pom_disable_module org.eclipse.jdt.launching.ui.macosx eclipse.jdt.debug
%pom_disable_module bundles/org.eclipse.compare.win32 eclipse.platform.team
%pom_disable_module org.eclipse.e4.ui.workbench.renderers.swt.cocoa eclipse.platform.ui/bundles
%pom_disable_module org.eclipse.ui.cocoa eclipse.platform.ui/bundles
%pom_disable_module org.eclipse.ui.win32 eclipse.platform.ui/bundles
%pom_disable_module bundles/org.eclipse.core.resources.win32.x86 eclipse.platform.resources
%pom_disable_module bundles/org.eclipse.core.resources.win32.x86_64 eclipse.platform.resources
for f in eclipse.jdt/org.eclipse.jdt-feature/feature.xml \
         eclipse.platform.ui/features/org.eclipse.e4.rcp/feature.xml \
         eclipse.platform.releng/features/org.eclipse.rcp/feature.xml \
         eclipse.platform.releng/features/org.eclipse.platform-feature/feature.xml ; do
  %pom_xpath_remove -f "plugin[@os='macosx']" $f
  %pom_xpath_remove -f "plugin[@os='win32']" $f
  %pom_xpath_remove -f "plugin[@ws='win32']" $f
  for arch in x86 x86_64 arm aarch64 ppc64 ppc64le s390x ; do
    if [ "$arch" != "%{eclipse_arch}" ] ; then
      %pom_xpath_remove -f "plugin[@arch='$arch']" $f
    fi
  done
done

# Fix versions in secondary arch fragments
fix_files=$(grep -lr 3.107.100 eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.*)
sed -i -e "s/3.107.100/3.108.0/" $fix_files
fix_files=$(grep -lr '1\.1\.[67]00' rt.equinox.framework/bundles/org.eclipse.equinox.launcher.gtk.linux.*)
sed -i -e "s/1\.1\.[67]00/1.1.800/" $fix_files
sed -i -e "/Fragment-Host/s/\(bundle-version=\).*/\1\"1.0.0\"/" $fix_files

# We don't need SWT fragments since we only care for current arch
%pom_disable_module tests/org.eclipse.swt.tests.fragments.feature eclipse.platform.swt
%pom_xpath_remove "pom:dependency-resolution" eclipse.platform.swt/tests/org.eclipse.swt.tests{,.gtk}

# Disable contributor tools that have external dependencies during bootstrap
%if %{with bootstrap}
%pom_disable_module eclipse.platform.ui.tools
%pom_disable_module features/org.eclipse.releng.tools eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.releng.tools eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.releng.tests eclipse.platform.releng
%pom_xpath_remove "plugin[@id='org.eclipse.releng.tests']" \
  eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml
%endif

# Include some extra features with the product that some other projects may need at
# build time as part of their target platform definitions
sed -i -e '/<features>/a<feature id="org.eclipse.core.runtime.feature"/>' \
  eclipse.platform.releng.tychoeclipsebuilder/platform/platform.product

# Ensure batch compiler gets installed correctly
sed -i -e '/org.eclipse.ui.themes/i<plugin id="org.eclipse.jdt.core.compiler.batch" download-size="0" install-size="0" version="0.0.0" unpack="false"/>' \
  eclipse.platform.releng/features/org.eclipse.platform-feature/feature.xml
sed -i -e '/<\/excludes>/i<plugin id="org.eclipse.jdt.core.compiler.batch"/>' \
  eclipse.platform.releng/features/org.eclipse.platform-feature/pom.xml

# Remove uneeded hamcrest bundles
%pom_xpath_remove "plugin[@id='org.hamcrest']" eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml
%pom_xpath_remove "plugin[@id='org.hamcrest.text']" eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml

# Use unbundled mockito
%pom_xpath_remove "plugin[@id='org.mockito']" eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml
%pom_xpath_inject "feature" '<plugin id="org.mockito.mockito-core" download-size="0" install-size="0" version="0.0.0" unpack="false"/>' eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml
%pom_xpath_inject "feature" '<plugin id="net.sf.cglib.core" download-size="0" install-size="0" version="0.0.0" unpack="false"/>' eclipse.platform.releng/features/org.eclipse.sdk.tests/feature.xml

# Prevent dep cycle
%pom_xpath_remove "plugin[@id='org.eclipse.core.tests.harness']" eclipse.platform.releng/features/org.eclipse.test-feature/feature.xml

# Include maven descriptors to allow our test execution setup to work
%pom_xpath_set "pom:plugin[pom:artifactId = 'tycho-packaging-plugin']/pom:configuration/pom:archive/pom:addMavenDescriptor" "true" eclipse-platform-parent

# Don't set perms on files for platforms that aren't linux
for f in rt.equinox.framework/features/org.eclipse.equinox.executable.feature/build.properties; do
  grep '^root\.linux\.gtk\.%{eclipse_arch}[.=]' $f > tmp
  sed -i -e '/^root\./d' $f && cat tmp >> $f
done

# Hack - this can go away once upstream grows arm and aarch64 support
mkdir -p rt.equinox.binaries/org.eclipse.equinox.executable/bin/gtk/linux/%{eclipse_arch}

# Ensure that bundles with native artifacts are dir-shaped, so no *.so is extracted into user.home
for f in rt.equinox.bundles/bundles/org.eclipse.equinox.security.linux.*/META-INF/MANIFEST.MF \
         eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.*/META-INF/MANIFEST.MF \
         eclipse.platform.resources/bundles/org.eclipse.core.filesystem.linux.*/META-INF/MANIFEST.MF \
         eclipse.platform.team/bundles/org.eclipse.core.net/fragments/org.eclipse.core.net.linux.*/META-INF/MANIFEST.MF ; do
    echo -e "Eclipse-BundleShape: dir\n\n" >> $f;
done

# Add dep on Java API stubs when compiling with JDT
%pom_xpath_inject "pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='tycho-compiler-plugin']/pom:dependencies" \
  "<dependency><groupId>org.eclipse</groupId><artifactId>java10api</artifactId><version>10</version></dependency>" eclipse-platform-parent

# Build fake ant bundle that contains symlinks to system jars
dependencies/fake_ant_dependency.sh

# Allow usage of javax.servlet.jsp 2.3.
sed -i '/javax\.servlet\.jsp/ s/2\.3/2\.4/' rt.equinox.bundles/bundles/org.eclipse.equinox.jsp.jasper/META-INF/MANIFEST.MF

# Use javax.servlet-api (Glassfish) instead of javax.servlet (Tomcat)
find -name feature.xml | xargs sed -i -e 's|"javax.servlet"|"javax.servlet-api"|'
sed -i -e "2iRequire-Bundle: javax.servlet-api" rt.equinox.bundles/bundles/org.eclipse.equinox.http.{jetty,servlet}/META-INF/MANIFEST.MF

# Fix constraint on gogo runtime
sed -i -e '/org.apache.felix.service.command/s/;status=provisional//' rt.equinox.bundles/bundles/org.eclipse.equinox.console{,.ssh}/META-INF/MANIFEST.MF

# Pre-compiling JSPs does not currently work
%pom_remove_plugin org.eclipse.jetty:jetty-jspc-maven-plugin eclipse.platform.ua/org.eclipse.help.webapp

# Remove generated files not present during bootstrap build
# org.eclipse.platform.doc.isv, org.eclipse.jdt.doc.isv, org.eclipse.pde.doc.user
%if %{with bootstrap}
sed -i '22,51d' eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests/src/main/assembly/assembly.xml
%endif

# Use system osgi.annotation lib
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi/osgi/
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi.services/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi.util/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.http.servlet/osgi/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.coordinator/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.log.stream/osgi/

# This test doesn't build on 32bit
# See: https://bugs.eclipse.org/bugs/show_bug.cgi?id=534174
rm eclipse.platform.swt/tests/org.eclipse.swt.tests.gtk/ManualTests/org/eclipse/swt/tests/gtk/snippets/Bug421127_Clipping_is_wrong.java

# The order of these mvn_package calls is important
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":*tests*" tests
%{mvn_package} ":org.eclipse.equinox.frameworkadmin.test" tests
%{mvn_package} ":org.eclipse.equinox.p2.installer" tests
%{mvn_package} ":org.eclipse.jface.examples.databinding" tests
%{mvn_package} ":org.eclipse.pde.tools.versioning" tests
%{mvn_package} ":org.eclipse.update.core" tests
%{mvn_package} "org.eclipse.test:org.eclipse.test" contributor-tools
%{mvn_package} ":*examples*" __noinstall
%{mvn_package} "::jar:sources{,-feature}:" sdk
%{mvn_package} ":org.eclipse.jdt.doc.isv" sdk
%{mvn_package} ":org.eclipse.platform.doc.isv" sdk
%{mvn_package} ":org.eclipse.equinox.executable" sdk
%{mvn_package} "org.eclipse.jdt{,.feature}:" jdt
%{mvn_package} ":org.eclipse.ant.{launching,ui}" jdt
%{mvn_package} ":org.eclipse.equinox.p2.discovery.{feature,compatibility}" p2-discovery
%{mvn_package} ":org.eclipse.equinox.p2{,.ui}.discovery" p2-discovery
%{mvn_package} ":org.eclipse.e4{,.core}.tools*" contributor-tools
%{mvn_package} ":org.eclipse.releng.tools" contributor-tools
%{mvn_package} ":org.eclipse.swt.tools*" contributor-tools
%{mvn_package} "org.eclipse.test{,.feature}:" contributor-tools
%{mvn_package} ":org.eclipse.ant.optional.junit" contributor-tools
%{mvn_package} "org.eclipse.cvs{,.feature}:" cvs
%{mvn_package} "org.eclipse.team:org.eclipse.team.cvs*" cvs
%{mvn_package} "org.eclipse.pde{,.ui,.feature}:" pde
%{mvn_package} "org.eclipse.ui:org.eclipse.ui.{views.log,trace}" pde
%{mvn_package} "org.eclipse.sdk{,.feature}:" sdk
%{mvn_package} ":" __noinstall

%build
#This is the lowest value where the build succeeds. 512m is not enough.
export MAVEN_OPTS="-Xmx2g -XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
export JAVA_HOME=%{_jvmdir}/java

# Pre-build agent jar needed for AdvancedSourceLookupSupport
sed -i -e '/createSourcesJar/d' eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent/pom.xml
(cd eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent && xmvn -o -B clean verify)
mv eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent/target/javaagent-shaded.jar \
  eclipse.jdt.debug/org.eclipse.jdt.launching/lib

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%%y %{SOURCE0})" +v%%Y%%m%%d-%%H%%M)
%{mvn_build} -j -f -- -DforceContextQualifier=$QUALIFIER \
%if %{with bootstrap}
   -P !api-generation,!build-docs \
%endif
   -Declipse.javadoc=%{_bindir}/javadoc -Dnative=gtk.linux.%{eclipse_arch} \
   -Dtycho.local.keepTarget \
   -Dfedora.p2.repos=$(pwd)/.m2/p2/repo-sdk/plugins -DbuildType=X

# Location that the product is materialised
product="eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.eclipse.platform.ide/linux/gtk/%{eclipse_arch}"

# Re-symlink ant bundle to use system jars
dependencies/fake_ant_dependency.sh $product/eclipse/plugins/org.apache.ant_*

# Symlink necessary plugins that are provided by other packages
dependencies/replace_platform_plugins_with_symlinks.sh $product/eclipse %{_javadir} %{_jnidir}

pushd $product/eclipse

#clean up
rm -rf configuration/org.eclipse.core.runtime
rm -rf configuration/org.eclipse.equinox.app
rm -rf configuration/org.eclipse.update
rm -rf configuration/org.eclipse.osgi
rm -rf p2/org.eclipse.equinox.p2.core/cache/*
# no icon needed
rm -f icon.xpm

# EMF and ECF are packaged separately
rm -rf features/org.eclipse.emf.* plugins/org.eclipse.emf.* \
  features/org.eclipse.ecf.* plugins/org.eclipse.ecf.* plugins/org.eclipse.ecf_*

#delete all local repositories. We want to have only "original" by default.
pushd p2/org.eclipse.equinox.p2.engine/.settings
    sed -i "/repositories\/file/d" *.prefs ../profileRegistry/SDKProfile.profile/.data/.settings/*.prefs
    sed -i "/repositories\/memory/d" *.prefs ../profileRegistry/SDKProfile.profile/.data/.settings/*.prefs
popd

# ini file adjustements
sed -i "s|-Xms40m|-Xms512m|g" eclipse.ini
sed -i "s|-Xmx512m|-Xmx1024m|g" eclipse.ini
sed -i '1i-protect\nroot' eclipse.ini

# Temporary fix until https://bugs.eclipse.org/294877 is resolved
cat >> eclipse.ini <<EOF
-Dorg.eclipse.swt.browser.UseWebKitGTK=true
-XX:CompileCommand=exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith
-XX:CompileCommand=exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>
-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate
-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding
-XX:CompileCommand=exclude,org/python/pydev/editor/codecompletion/revisited/PythonPathHelper,isValidSourceFile
-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState
-Dorg.eclipse.equinox.p2.reconciler.dropins.directory=%{_datadir}/eclipse/dropins
-Dp2.fragments=%{_eclipsedir}/droplets,%{_datadir}/eclipse/droplets
-Declipse.p2.skipMovedInstallDetection=true
-Dosgi.resolver.usesMode=ignore
EOF

popd #eclipse

%install
%{mvn_file} ":{*}" eclipse/@1
%mvn_install

# Some directories we need
install -d -m 755 %{buildroot}%{_sysconfdir}
install -d -m 755 %{buildroot}%{_jnidir}
install -d -m 755 %{buildroot}%{_javadir}/eclipse
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_bindir}

# Install icons
install -D eclipse.platform/platform/org.eclipse.platform/eclipse32.png \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D eclipse.platform/platform/org.eclipse.platform/eclipse48.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D eclipse.platform/platform/org.eclipse.platform/eclipse256.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -d %{buildroot}%{_datadir}/pixmaps
ln -s %{_datadir}/icons/hicolor/256x256/apps/%{name}.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Install desktop file
sed -i -e 's/Exec=eclipse/Exec=%{app_exec}/g' desktopintegration/eclipse.desktop
sed -i -e 's/Name=Eclipse/Name=%{app_name}/g' desktopintegration/eclipse.desktop
sed -i -e 's/Icon=eclipse/Icon=%{name}/g' desktopintegration/eclipse.desktop
install -m644 -D desktopintegration/eclipse.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install appstream appdata
install -m644 -D desktopintegration/eclipse.appdata.xml      %{buildroot}%{_datadir}/appdata/eclipse.appdata.xml
install -m644 -D desktopintegration/eclipse-jdt.metainfo.xml %{buildroot}%{_datadir}/appdata/eclipse-jdt.metainfo.xml
install -m644 -D desktopintegration/eclipse-pde.metainfo.xml %{buildroot}%{_datadir}/appdata/eclipse-pde.metainfo.xml

LOCAL_PWD=`pwd`
#change the installation p2 files
pushd eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.eclipse.platform.ide/linux/gtk/%{eclipse_arch}/eclipse/p2/org.eclipse.equinox.p2.engine/profileRegistry/SDKProfile.profile/
for i in `ls | grep "profile.gz"` ; do  \
        echo $i ; \
        gunzip $i ; \
        sed -i -e "s@${LOCAL_PWD}/eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.eclipse.platform.ide/linux/gtk/%{eclipse_arch}/eclipse@%{_eclipsedir}@g" *.profile ; \
        gzip *.profile ; \
    done
popd

#installation itself - copy it into right location
rsync -vrpl eclipse.platform.releng.tychoeclipsebuilder/platform/target/products/org.eclipse.platform.ide/linux/gtk/%{eclipse_arch}/eclipse \
    %{buildroot}%{_libdir}

# Symlink eclipse binary
pushd %{buildroot}%{_bindir}
    ln -s %{_eclipsedir}/eclipse
popd

# Symlink eclipse ini
pushd %{buildroot}/%{_sysconfdir}/
    ln -s %{_eclipsedir}/eclipse.ini
popd

# List jars to be symlinked into javadir
pushd %{buildroot}%{_eclipsedir}/plugins
EQUINOX_JARS=$(ls . | grep -P '^org.eclipse.equinox(?!.*\.ui[\._])' | sed -e 's|^org\.eclipse\.\(.*\)_.*|\1|')
OSGI_JARS=$(ls . | grep '^org.eclipse.osgi' | sed -e 's|^org\.eclipse\.\(.*\)_.*|\1|')
popd

# Symlink jars into javadir
location=%{_eclipsedir}/plugins
while [ "$location" != "/" ] ; do
    location=$(dirname $location)
    updir="$updir../"
done
pushd %{buildroot}%{_javadir}/eclipse
for J in $EQUINOX_JARS core.contenttype core.jobs core.net core.runtime ; do
  DIR=$updir%{_eclipsedir}/plugins
  if [ "$J" != "equinox.http.servlet" ] ; then
    [ -e "`ls $DIR/org.eclipse.${J}_*.jar`" ] && ln -s $DIR/org.eclipse.${J}_*.jar ${J}.jar
  fi
done
popd

# Generate addition Maven metadata
rm -rf .xmvn/ .xmvn-reactor
%{mvn_package} "org.eclipse.osgi:" equinox-osgi
%{mvn_package} "org.eclipse.equinox.http:" platform
%{mvn_package} "org.eclipse.swt:" swt

# Install Maven metadata for OSGi jars
for J in $OSGI_JARS ; do
  JAR=%{buildroot}%{_eclipsedir}/plugins/org.eclipse.${J}_*.jar
  VER=$(echo $JAR | sed -e "s/.*${J}_\(.*\)\.jar/\1/")
  %{mvn_artifact} "org.eclipse.osgi:$J:jar:$VER" $JAR
  if [ "$J" = "osgi" ] ; then
    %{mvn_alias} "org.eclipse.osgi:$J" "org.eclipse.osgi:org.eclipse.$J" "org.eclipse.tycho:org.eclipse.$J" "org.eclipse:$J"
  else
    %{mvn_alias} "org.eclipse.osgi:$J" "org.eclipse.osgi:org.eclipse.$J" "org.eclipse.tycho:org.eclipse.$J"
  fi
done

# Install Maven metadata for Equinox HTTP Servlet
JAR=%{buildroot}%{_eclipsedir}/plugins/org.eclipse.equinox.http.servlet_*.jar
VER=$(echo $JAR | sed -e "s/.*_\(.*\)\.jar/\1/")
%{mvn_artifact} "org.eclipse.equinox.http:equinox.http.servlet:jar:$VER" $JAR
%{mvn_alias} "org.eclipse.equinox.http:equinox.http.servlet" "org.eclipse.equinox.http:servlet"

# Install Maven metadata for SWT
JAR=%{buildroot}%{_eclipsedir}/plugins/org.eclipse.swt_*.jar
VER=$(echo $JAR | sed -e "s/.*_\(.*\)\.jar/\1/")
%{mvn_artifact} "org.eclipse.swt:org.eclipse.swt:jar:$VER" ./eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.%{eclipse_arch}/target/org.eclipse.swt.gtk.linux.%{eclipse_arch}-*-SNAPSHOT.jar
%{mvn_alias} "org.eclipse.swt:org.eclipse.swt" "org.eclipse.swt:swt"
%{mvn_file} "org.eclipse.swt:org.eclipse.swt" swt
%{mvn_file} ":{*}" eclipse/@1

%mvn_install

# Symlink SWT jar
pushd %{buildroot}/%{_eclipsedir}/
    ln -s $(abs2rel %{_jnidir}/swt.jar %{_eclipsedir})
popd

# Tests framework
unzip eclipse.platform.releng.tychoeclipsebuilder/eclipse-junit-tests/target/eclipse-junit-tests-bundle.zip \
  -d %{buildroot}/%{_datadir}/ -x eclipse-testing/runtests.bat eclipse-testing/runtestsmac.sh
cp utils/splitter.xsl %{buildroot}/%{_datadir}/eclipse-testing
rm %{buildroot}/%{_datadir}/eclipse-testing/eclipse-junit-tests-*.zip

# These properties are not correct and nested properties won't get resolved
sed -i '/org.eclipse.equinox.p2.reconciler.test/ d' %{buildroot}/%{_datadir}/eclipse-testing/equinoxp2tests.properties

# Package testbundle-to-eclipse-test
cp -r testbundle-to-eclipse-test %{buildroot}/%{_datadir}/eclipse-testing/testbundle
mv %{buildroot}/%{_datadir}/eclipse-testing/testbundle/eclipse-runTestBundles %{buildroot}/%{_bindir}/eclipse-runTestBundles

#fix so permissions
find %{buildroot}/%{_eclipsedir} -name *.so -exec chmod a+x {} \;

# Usage marker
install -d -m 755 %{buildroot}%{_eclipsedir}/.pkgs
echo "%{version}-%{release}" > %{buildroot}%{_eclipsedir}/.pkgs/Distro%{?dist}

%if %{with bootstrap}
%post -n eclipse-platform-bootstrap
%else
%post platform
%endif
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%if %{with bootstrap}
%postun -n eclipse-platform-bootstrap
%else
%postun platform
%endif
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%if %{with bootstrap}
%files -n eclipse-swt-bootstrap -f .mfiles-swt
%else
%files swt -f .mfiles-swt
%endif
%{_eclipsedir}/plugins/org.eclipse.swt_*
%{_eclipsedir}/plugins/org.eclipse.swt.gtk.linux.*
%{_eclipsedir}/swt.jar
%{_jnidir}/swt.jar

%if %{with bootstrap}
%files -n eclipse-platform-bootstrap -f .mfiles-platform
%else
%files platform -f .mfiles-platform
%endif
%{_bindir}/eclipse
%{_eclipsedir}/eclipse
%{_eclipsedir}/.eclipseproduct
%{_eclipsedir}/.pkgs
%config %{_eclipsedir}/eclipse.ini
%config %{_sysconfdir}/eclipse.ini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_datadir}/appdata/eclipse.appdata.xml
%dir %{_eclipsedir}/configuration/
%dir %{_eclipsedir}/configuration/org.eclipse.equinox.simpleconfigurator/
%{_eclipsedir}/configuration/config.ini
%{_eclipsedir}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%{_eclipsedir}/features/org.eclipse.core.runtime.feature_*
%{_eclipsedir}/features/org.eclipse.e4.rcp_*
%{_eclipsedir}/features/org.eclipse.equinox.core.feature_*
%{_eclipsedir}/features/org.eclipse.equinox.p2.core.feature_*
%{_eclipsedir}/features/org.eclipse.equinox.p2.extras.feature_*
%{_eclipsedir}/features/org.eclipse.equinox.p2.rcp.feature_*
%{_eclipsedir}/features/org.eclipse.equinox.p2.user.ui_*
%{_eclipsedir}/features/org.eclipse.help_*
%{_eclipsedir}/features/org.eclipse.platform_*
%{_eclipsedir}/features/org.eclipse.rcp_*
%{_eclipsedir}/plugins/com.ibm.icu_*
%{_eclipsedir}/plugins/com.jcraft.jsch_*
%{_eclipsedir}/plugins/com.sun.el.javax.el_*
%{_eclipsedir}/plugins/javax.*
%{_eclipsedir}/plugins/org.apache.*
%{_eclipsedir}/plugins/org.eclipse.ant.core_*
%{_eclipsedir}/plugins/org.eclipse.compare_*
%{_eclipsedir}/plugins/org.eclipse.compare.core_*
%{_eclipsedir}/plugins/org.eclipse.core.commands_*
%{_eclipsedir}/plugins/org.eclipse.core.contenttype_*
%{_eclipsedir}/plugins/org.eclipse.core.databinding.beans_*
%{_eclipsedir}/plugins/org.eclipse.core.databinding.observable_*
%{_eclipsedir}/plugins/org.eclipse.core.databinding.property_*
%{_eclipsedir}/plugins/org.eclipse.core.databinding_*
%{_eclipsedir}/plugins/org.eclipse.core.expressions_*
%{_eclipsedir}/plugins/org.eclipse.core.externaltools_*
%{_eclipsedir}/plugins/org.eclipse.core.filebuffers_*
%{_eclipsedir}/plugins/org.eclipse.core.filesystem*
%{_eclipsedir}/plugins/org.eclipse.core.jobs_*
%{_eclipsedir}/plugins/org.eclipse.core.net*
%{_eclipsedir}/plugins/org.eclipse.core.resources_*
%{_eclipsedir}/plugins/org.eclipse.core.runtime_*
%{_eclipsedir}/plugins/org.eclipse.core.variables_*
%{_eclipsedir}/plugins/org.eclipse.debug.core_*
%{_eclipsedir}/plugins/org.eclipse.debug.ui_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.commands_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.contexts_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.di_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.di.annotations_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.di.extensions_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.di.extensions.supplier_*
%{_eclipsedir}/plugins/org.eclipse.e4.core.services_*
%{_eclipsedir}/plugins/org.eclipse.e4.emf.xpath_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.bindings_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.css.core_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.css.swt_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.css.swt.theme_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.di_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.dialogs_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.model.workbench_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.services_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.swt.gtk_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.widgets_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.workbench_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.workbench3_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.workbench.addons.swt_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.workbench.renderers.swt_*
%{_eclipsedir}/plugins/org.eclipse.e4.ui.workbench.swt_*
%{_eclipsedir}/plugins/org.eclipse.equinox.app_*
%{_eclipsedir}/plugins/org.eclipse.equinox.bidi_*
%{_eclipsedir}/plugins/org.eclipse.equinox.common_*
%{_eclipsedir}/plugins/org.eclipse.equinox.concurrent_*
%{_eclipsedir}/plugins/org.eclipse.equinox.console_*
%{_eclipsedir}/plugins/org.eclipse.equinox.ds_*
%{_eclipsedir}/plugins/org.eclipse.equinox.event_*
%{_eclipsedir}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_eclipsedir}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_eclipsedir}/plugins/org.eclipse.equinox.http.jetty_*
%{_eclipsedir}/plugins/org.eclipse.equinox.http.registry_*
%{_eclipsedir}/plugins/org.eclipse.equinox.http.servlet_*
%{_eclipsedir}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_eclipsedir}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_eclipsedir}/plugins/org.eclipse.equinox.launcher_*
%{_eclipsedir}/plugins/org.eclipse.equinox.launcher.gtk.linux.*_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.console_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.core_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.director_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.director.app_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.engine_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.metadata_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.operations_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.publisher_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.publisher.eclipse_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.repository_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.repository.tools_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.transport.ecf_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.ui_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.ui.importexport_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_eclipsedir}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_eclipsedir}/plugins/org.eclipse.equinox.preferences_*
%{_eclipsedir}/plugins/org.eclipse.equinox.registry_*
%{_eclipsedir}/plugins/org.eclipse.equinox.security*
%{_eclipsedir}/plugins/org.eclipse.equinox.simpleconfigurator_*
%{_eclipsedir}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_eclipsedir}/plugins/org.eclipse.equinox.util_*
%{_eclipsedir}/plugins/org.eclipse.help_*
%{_eclipsedir}/plugins/org.eclipse.help.base_*
%{_eclipsedir}/plugins/org.eclipse.help.ui_*
%{_eclipsedir}/plugins/org.eclipse.help.webapp_*
%{_eclipsedir}/plugins/org.eclipse.jdt.core.compiler.batch_*
%{_eclipsedir}/plugins/org.eclipse.jetty.*
%{_eclipsedir}/plugins/org.eclipse.jface_*
%{_eclipsedir}/plugins/org.eclipse.jface.databinding_*
%{_eclipsedir}/plugins/org.eclipse.jface.text_*
%{_eclipsedir}/plugins/org.eclipse.jsch.core_*
%{_eclipsedir}/plugins/org.eclipse.jsch.ui_*
%{_eclipsedir}/plugins/org.eclipse.ltk.core.refactoring_*
%{_eclipsedir}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_eclipsedir}/plugins/org.eclipse.platform_*
%{_eclipsedir}/plugins/org.eclipse.platform.doc.user_*
%{_eclipsedir}/plugins/org.eclipse.rcp_*
%{_eclipsedir}/plugins/org.eclipse.search_*
%{_eclipsedir}/plugins/org.eclipse.team.core_*
%{_eclipsedir}/plugins/org.eclipse.team.genericeditor.diff.extension_*
%{_eclipsedir}/plugins/org.eclipse.team.ui_*
%{_eclipsedir}/plugins/org.eclipse.text_*
%{_eclipsedir}/plugins/org.eclipse.ui_*
%{_eclipsedir}/plugins/org.eclipse.ui.browser_*
%{_eclipsedir}/plugins/org.eclipse.ui.cheatsheets_*
%{_eclipsedir}/plugins/org.eclipse.ui.console_*
%{_eclipsedir}/plugins/org.eclipse.ui.editors_*
%{_eclipsedir}/plugins/org.eclipse.ui.externaltools_*
%{_eclipsedir}/plugins/org.eclipse.ui.forms_*
%{_eclipsedir}/plugins/org.eclipse.ui.genericeditor_*
%{_eclipsedir}/plugins/org.eclipse.ui.ide_*
%{_eclipsedir}/plugins/org.eclipse.ui.ide.application_*
%{_eclipsedir}/plugins/org.eclipse.ui.intro_*
%{_eclipsedir}/plugins/org.eclipse.ui.intro.quicklinks_*
%{_eclipsedir}/plugins/org.eclipse.ui.intro.universal_*
%{_eclipsedir}/plugins/org.eclipse.ui.monitoring_*
%{_eclipsedir}/plugins/org.eclipse.ui.navigator_*
%{_eclipsedir}/plugins/org.eclipse.ui.navigator.resources_*
%{_eclipsedir}/plugins/org.eclipse.ui.net_*
%{_eclipsedir}/plugins/org.eclipse.ui.themes_*
%{_eclipsedir}/plugins/org.eclipse.ui.views_*
%{_eclipsedir}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_eclipsedir}/plugins/org.eclipse.ui.workbench_*
%{_eclipsedir}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_eclipsedir}/plugins/org.eclipse.update.configurator_*
%{_eclipsedir}/plugins/org.eclipse.urischeme_*
%{_eclipsedir}/plugins/org.glassfish.web.javax.servlet.jsp_*
%{_eclipsedir}/plugins/org.sat4j.core_*
%{_eclipsedir}/plugins/org.sat4j.pb_*
%{_eclipsedir}/plugins/org.tukaani.xz_*
%{_eclipsedir}/plugins/org.w3c.css.sac_*
%{_eclipsedir}/plugins/org.w3c.dom.svg_*
%{_eclipsedir}/plugins/osgi.cmpn_*
%doc %{_eclipsedir}/readme
%{_eclipsedir}/artifacts.xml
%{_eclipsedir}/p2
%{_javadir}/eclipse/core*
%{_javadir}/eclipse/equinox*

%if %{with bootstrap}
%files -n eclipse-jdt-bootstrap -f .mfiles-jdt
%else
%files jdt -f .mfiles-jdt
%endif
%{_datadir}/appdata/eclipse-jdt.metainfo.xml

%if %{with bootstrap}
%files -n eclipse-pde-bootstrap -f .mfiles-pde -f .mfiles-cvs -f .mfiles-sdk
%else
%files pde -f .mfiles-pde -f .mfiles-cvs -f .mfiles-sdk
%endif
%{_eclipsedir}/droplets/*-sdk/features/org.eclipse.equinox.executable_*
%{_datadir}/appdata/eclipse-pde.metainfo.xml

%if %{with bootstrap}
%files -n eclipse-p2-discovery-bootstrap -f .mfiles-p2-discovery
%else
%files p2-discovery -f .mfiles-p2-discovery
%endif

%if %{with bootstrap}
%files -n eclipse-contributor-tools-bootstrap -f .mfiles-contributor-tools
%else
%files contributor-tools -f .mfiles-contributor-tools
%endif

%if %{with bootstrap}
%files -n eclipse-tests-bootstrap -f .mfiles-tests
%else
%files tests -f .mfiles-tests
%endif
%{_bindir}/eclipse-runTestBundles
%{_datadir}/eclipse-testing

%if %{with bootstrap}
%files -n eclipse-equinox-osgi-bootstrap -f .mfiles-equinox-osgi
%else
%files equinox-osgi -f .mfiles-equinox-osgi
%endif
%{_eclipsedir}/plugins/org.eclipse.osgi_*
%{_eclipsedir}/plugins/org.eclipse.osgi.compatibility.state_*
%{_eclipsedir}/plugins/org.eclipse.osgi.services_*
%{_eclipsedir}/plugins/org.eclipse.osgi.util_*

%changelog
