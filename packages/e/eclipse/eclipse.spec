#
# spec file for package eclipse
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%bcond_with contrib_tools
%else
%bcond_with bootstrap
%bcond_without contrib_tools
%endif
%global eb_commit       c985e357223668b4bc1fb76ea6b9e0c12829b7e8
%global eclipse_rel   4.15
%global eclipse_tag     R-%{eclipse_rel}-202003050155
%global _jetty_version  9.4.27
%global _lucene_version 8.4.1
%global _batik_version 1.11
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
%ifarch s390x x86_64 aarch64 ppc64le riscv64
    %global eclipse_arch %{_arch}
%endif
# Desktop file information
%global app_name %{?app_name_prefix}%{!?app_name_prefix:Eclipse}
%global app_exec %{?app_exec_prefix} eclipse
# Eclipse is arch-specific, but multilib agnostic
%global _eclipsedir %{_libdir}/eclipse
%global use_wayland 0
Version:        %{eclipse_rel}
Release:        0
Summary:        An open, extensible IDE
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/
# eclipse-create-tarball.sh
Source0:        eclipse-platform-sources-%{eclipse_rel}-clean.tar.xz
# Can generate locally with:
# git archive --format=tar --prefix=org.eclipse.linuxtools.eclipse-build-%%{eb_commit}/ \
#   %%{eb_commit} | xz > org.eclipse.linuxtools.eclipse-build-%%{eb_commit}.tar.xz
Source1:        http://git.eclipse.org/c/linuxtools/org.eclipse.linuxtools.eclipse-build.git/snapshot/org.eclipse.linuxtools.eclipse-build-%{eb_commit}.tar.xz
Source100:      eclipse-create-tarball.sh
# Eclipse should not include source for dependencies that are not supplied by this package
# and should not include source for bundles that are not relevant to our platform
Patch0:         eclipse-no-source-for-dependencies.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=377515
Patch1:         eclipse-p2-pick-up-renamed-jars.patch
# Patch for this was contributed. Unlikely to be released.
Patch2:         eclipse-ignore-version-when-calculating-home.patch
# Add support for all arches supported by us
Patch4:         eclipse-secondary-arches.patch
Patch5:         eclipse-debug-symbols.patch
# Add support for riscv64
Patch6:         eclipse-riscv64.patch
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=408138
Patch12:        eclipse-fix-dropins.patch
# Feature plugin definitions lock onto version of plugin at build-time.
# If plugin is external, updating it breaks the feature. (version changes)
# Workaround : Change <plugin> definition to a 'requirement'
# Also makes the following BSN changes at the same time:
# com.sun.el -> com.sun.el.javax.el
# javax.el -> javax.el-api
# javax.servlet -> javax.servlet-api
# org.apache.jasper.glassfish -> org.glassfish.web.javax.servlet.jsp
# javax.annotation -> javax.annotation-api
# org.w3c.dom.smil -> removed
Patch13:        eclipse-feature-plugins-to-category-ius.patch
Patch14:        eclipse-support-symlink-bundles.patch
# Fix various JDT and PDE tests
Patch15:        eclipse-fix-tests.patch
# Droplet fixes
Patch17:        eclipse-pde-tp-support-droplets.patch
# Disable uses by default
Patch18:        eclipse-disable-uses-constraints.patch
# Droplet fixes
Patch19:        eclipse-make-droplets-runnable.patch
Patch20:        eclipse-disable-droplets-in-dropins.patch
# Temporary measure until wayland improves
Patch21:        prefer_x11_backend.patch
# Fix errors when building ant launcher
Patch22:        fix_ant_build.patch
# Hide the p2 Droplets from cluttering Install Wizard Combo
Patch23:        eclipse-hide-droplets-from-install-wizard.patch
# Avoid the need for a javascript interpreter at build time
Patch24:        eclipse-swt-avoid-javascript-at-build.patch
# Avoid optional dep used only for tests
Patch25:        eclipse-patch-out-fileupload-dep.patch
# Force a clean on the restart after p2 operations
Patch26:        force-clean-after-p2-operations.patch
Patch27:        compiler-release.patch
# Adapt the symlinks to the openSUSE install of batik
Patch31:        eclipse-suse-batik.patch
# Add symlink for osgi-core
Patch32:        eclipse-suse-osgi-core.patch
# Fix build on ppc64 big endian
Patch33:        eclipse-ppc64.patch
Patch34:        eclipse-libkeystorelinuxnative.patch
# PATCH-FIX-UPSTREAM bsc#1183728 CVE-2020-27225 Help Subsystem does not authenticate active help requests
Patch35:        eclipse-CVE-2020-27225.patch
Patch36:        eclipse-ant.patch
Patch37:        reproducible-p2_timestamp.patch
Patch38:        eclipse-CVE-2023-4218.patch
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
BuildRequires:  apache-commons-jxpath
BuildRequires:  apache-commons-logging
BuildRequires:  apiguardian
BuildRequires:  atinject
BuildRequires:  cbi-plugins
BuildRequires:  desktop-file-utils
BuildRequires:  eclipse-license2
BuildRequires:  gcc
BuildRequires:  glassfish-annotation-api
BuildRequires:  glassfish-el > 3.0.0
BuildRequires:  glassfish-el-api > 3.0.0
BuildRequires:  glassfish-jsp >= 2.2.5
BuildRequires:  glassfish-jsp-api >= 2.2.1-4
BuildRequires:  glassfish-servlet-api >= 3.1.0
BuildRequires:  google-gson
BuildRequires:  hamcrest
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  icu4j >= 65.1
# Build with Java 11
BuildRequires:  java-devel >= 11
BuildRequires:  jgit
BuildRequires:  jsch >= 0.1.46
BuildRequires:  jsoup
BuildRequires:  junit >= 4.12
BuildRequires:  junit5 >= 5.4.0
BuildRequires:  lucene-analysis >= %{_lucene_version}
BuildRequires:  lucene-analyzers-smartcn >= %{_lucene_version}
BuildRequires:  lucene-core >= %{_lucene_version}
BuildRequires:  lucene-queryparser >= %{_lucene_version}
BuildRequires:  make
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-local
BuildRequires:  maven-shade-plugin
BuildRequires:  objectweb-asm >= 7.0
BuildRequires:  osgi-core
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sac
BuildRequires:  sat4j
BuildRequires:  sonatype-oss-parent
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-maven-plugin
BuildRequires:  xmlgraphics-batik >= %{_batik_version}
BuildRequires:  xmlgraphics-batik-css >= %{_batik_version}
BuildRequires:  xmlgraphics-commons >= 2.3
BuildRequires:  xz-java
BuildRequires:  zip
BuildRequires:  osgi(org.apache.felix.gogo.command) >= 1.0.2
BuildRequires:  osgi(org.apache.felix.gogo.runtime) >= 1.1.0
BuildRequires:  osgi(org.apache.felix.gogo.shell) >= 1.1.0
BuildRequires:  osgi(org.apache.felix.scr) >= 2.1.16
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
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}
%if %{with bootstrap}
Name:           eclipse-bootstrap
%else
Name:           eclipse
%endif
# Build deps that are excluded when bootstrapping
%if %{without bootstrap}
BuildRequires:  eclipse-ecf-core >= 3.14.1
BuildRequires:  eclipse-emf-core > 2.14.99
BuildRequires:  eclipse-pde-bootstrap
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  tycho
#!BuildIgnore:  eclipse-ecf-core-bootstrap
#!BuildIgnore:  eclipse-emf-core-bootstrap
#!BuildIgnore:  eclipse-pde
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
%if %{with contrib_tools}
BuildRequires:  eclipse-egit
BuildRequires:  eclipse-emf-runtime
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
Requires:       java-headless >= 1.8
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
Requires:       java-headless >= 1.8
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
Requires:       eclipse-equinox-osgi-bootstrap = %{version}-%{release}
Requires:       eclipse-swt-bootstrap = %{version}-%{release}
%else

%package        platform
Requires:       %{name}-equinox-osgi = %{version}-%{release}
Requires:       %{name}-swt = %{version}-%{release}
Requires:       eclipse-ecf-core >= 3.14.7
Requires:       eclipse-emf-core >= 2.21.0
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
Requires:       apache-commons-jxpath
Requires:       apache-commons-logging
Requires:       atinject
Requires:       glassfish-annotation-api
Requires:       glassfish-el > 3.0.0
Requires:       glassfish-el-api > 3.0.0
Requires:       glassfish-jsp >= 2.2.5
Requires:       glassfish-jsp-api >= 2.2.1-4
Requires:       glassfish-servlet-api >= 3.1.0
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       icu4j >= 65.1
Requires:       jsch >= 0.1.46-2
Requires:       lucene-analysis >= %{_lucene_version}
Requires:       lucene-analyzers-smartcn >= %{_lucene_version}
Requires:       lucene-core >= %{_lucene_version}
Requires:       lucene-queryparser >= %{_lucene_version}
Requires:       sac
Requires:       sat4j
Requires:       xml-commons-apis
Requires:       xmlgraphics-batik >= %{_batik_version}
Requires:       xmlgraphics-batik-css >= %{_batik_version}
Requires:       xmlgraphics-commons >= 2.3
Requires:       osgi(org.apache.felix.gogo.command) >= 1.0.2
Requires:       osgi(org.apache.felix.gogo.runtime) >= 1.1.0
Requires:       osgi(org.apache.felix.gogo.shell) >= 1.1.0
Requires:       osgi(org.apache.felix.scr) >= 2.1.16
Requires:       osgi(org.eclipse.jetty.continuation) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.http) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.io) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.security) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.server) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.servlet) >= %{_jetty_version}
Requires:       osgi(org.eclipse.jetty.util) >= %{_jetty_version}
Requires:       osgi(org.tukaani.xz)
Requires:       osgi(osgi.core)
Recommends:     eclipse-usage

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
Requires:       junit >= 4.12
Requires:       junit5 >= 5.4.0
Provides:       %{name} = %{version}-%{release}
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
Requires:       objectweb-asm >= 7.0

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

%if %{with contrib_tools}
%if %{with bootstrap}
%package        -n eclipse-contributor-tools-bootstrap
Requires:       eclipse-platform-bootstrap = %{version}-%{release}
%else

%package        contributor-tools
Requires:       %{name}-platform = %{version}-%{release}
Obsoletes:      eclipse-contributor-tools-bootstrap
%endif
Summary:        Tools for Eclipse Contributors
# No longer shipping tests
Group:          Development/Libraries/Java
Obsoletes:      %{name}-tests < 4.14-2

%if %{with bootstrap}
%description    -n eclipse-contributor-tools-bootstrap
%else

%description    contributor-tools
%endif
This package contains tools specifically for Eclipse contributors. It includes
SWT tools, E4 tools, Rel-Eng tools and Eclipse Test frameworks.
%endif

%prep
%setup -q -T -c

# Extract main source
tar --strip-components=1 -xf %{SOURCE0}

# Extract linuxtools/eclipse-build sources
tar --strip-components=1 -xf %{SOURCE1}

%patch -P 0
%patch -P 1
%patch -P 2 -p1
%patch -P 4 -p1
%patch -P 5
%patch -P 6 -p1
%patch -P 12
%patch -P 13 -p1
%patch -P 14
%patch -P 15
%patch -P 17 -p1
%patch -P 18
%patch -P 19
%patch -P 20
%if ! %{use_wayland}
%patch -P 21
%endif
%patch -P 22
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25
%patch -P 26 -p1
%patch -P 27

%patch -P 31 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1
%patch -P 35 -p1
%patch -P 36 -p1
%patch -P 37 -p1

%patch -P 38 -p1

# Extend the objectweb-asm requirements
sed -i -e 's/org\.objectweb\.asm\.tree;bundle-version="\[6\.0\.0,8\.0\.0)"/org\.objectweb\.asm\.tree;bundle-version="\[6\.0\.0,10\.0\.0)"/g' \
  eclipse.pde.ui/apitools/org.eclipse.pde.api.tools/META-INF/MANIFEST.MF
sed -i -e 's/org\.objectweb\.asm;bundle-version="\[6\.0\.0,8\.0\.0)"/org\.objectweb\.asm;bundle-version="\[6\.0\.0,10\.0\.0)"/g' \
  eclipse.pde.ui/apitools/org.eclipse.pde.api.tools/META-INF/MANIFEST.MF

# Optional (unused) multipart support (see patch 25)
rm rt.equinox.bundles/bundles/org.eclipse.equinox.http.servlet/src/org/eclipse/equinox/http/servlet/internal/multipart/MultipartSupport{Impl,FactoryImpl,Part}.java

# No strict bin includes
sed -i -e '/jgit.dirtyWorkingTree>/a<strictSrcIncludes>false</strictSrcIncludes><strictBinIncludes>false</strictBinIncludes>' eclipse-platform-parent/pom.xml

# Remove jgit deps because building from source tarball, not a git repo
%pom_remove_dep :tycho-buildtimestamp-jgit eclipse-platform-parent
%pom_remove_dep :tycho-sourceref-jgit eclipse-platform-parent
%pom_xpath_remove 'pom:configuration/pom:timestampProvider' eclipse-platform-parent
%pom_xpath_remove 'pom:configuration/pom:sourceReferences' eclipse-platform-parent

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
%pom_disable_module bundles/org.eclipse.equinox.p2.artifact.optimizers rt.equinox.p2
%pom_disable_module bundles/org.eclipse.equinox.p2.artifact.processors rt.equinox.p2
%pom_disable_module bundles/org.eclipse.equinox.p2.artifact.checksums.bouncycastle rt.equinox.p2

# Don't need annotations for obsolete JDKs
%pom_disable_module org.eclipse.jdt.annotation_v1 eclipse.jdt.core
%pom_xpath_remove "plugin[@version='1.1.400.qualifier']" eclipse.jdt/org.eclipse.jdt-feature/feature.xml
sed -i -e '/org\.eclipse\.jdt\.annotation;bundle-version="\[1\.1\.0,2\.0\.0)"/d' \
  eclipse.jdt.core/org.eclipse.jdt.core.tests.{model,builder,compiler}/META-INF/MANIFEST.MF \
  eclipse.jdt.core/org.eclipse.jdt.apt.pluggable.tests/META-INF/MANIFEST.MF \
  eclipse.jdt.ui/org.eclipse.jdt.ui.tests/META-INF/MANIFEST.MF
sed -i -e 's/javax.annotation/javax.annotation-api/' eclipse-platform-parent/pom.xml \
  eclipse.jdt.core/org.eclipse.jdt.core.tests.compiler/META-INF/MANIFEST.MF

# Disable examples
%pom_disable_module examples rt.equinox.p2
%pom_disable_module examples eclipse.platform.ui
%pom_disable_module org.eclipse.debug.examples.core eclipse.platform.debug
%pom_disable_module org.eclipse.debug.examples.memory eclipse.platform.debug
%pom_disable_module org.eclipse.debug.examples.mixedmode eclipse.platform.debug
%pom_disable_module org.eclipse.debug.examples.ui eclipse.platform.debug
%pom_disable_module bundles/org.eclipse.sdk.examples eclipse.platform.releng
%pom_disable_module features/org.eclipse.sdk.examples-feature eclipse.platform.releng
%pom_disable_module examples/org.eclipse.swt.examples.ole.win32 eclipse.platform.swt
%pom_disable_module examples/org.eclipse.compare.examples eclipse.platform.team
%pom_disable_module examples/org.eclipse.compare.examples.xml eclipse.platform.team
%pom_disable_module examples/org.eclipse.team.examples.filesystem eclipse.platform.team
%pom_disable_module org.eclipse.jface.text.examples eclipse.platform.text
%pom_disable_module org.eclipse.ui.genericeditor.examples eclipse.platform.text
%pom_disable_module org.eclipse.ui.intro.quicklinks.examples eclipse.platform.ua
%pom_disable_module org.eclipse.ui.intro.solstice.examples eclipse.platform.ua

# Disable tests
for pom in eclipse.jdt.core{,.binaries} eclipse.jdt.debug eclipse.jdt.ui eclipse.pde.build eclipse.pde.ui{,/apitools} \
    eclipse.platform eclipse.platform.debug eclipse.platform.releng eclipse.platform.resources eclipse.platform.runtime \
    eclipse.platform.swt eclipse.platform.team eclipse.platform.text eclipse.platform.ui eclipse.platform.ua \
    rt.equinox.bundles rt.equinox.framework rt.equinox.p2 ; do
  sed -i -e '/<module>.*tests.*<\/module>/d' $pom/pom.xml
done
%pom_disable_module bundles/org.eclipse.equinox.frameworkadmin.test rt.equinox.p2
%pom_disable_module eclipse-junit-tests eclipse.platform.releng.tychoeclipsebuilder
%pom_disable_module ./tests/org.eclipse.e4.tools.test eclipse.platform.ui.tools

# Disable test framework if we are not shipping tests
%pom_disable_module features/org.eclipse.test-feature eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.test eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.test.performance eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.test.performance.win32 eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.ant.optional.junit eclipse.platform.releng

# Disable servletbridge stuff
%pom_disable_module bundles/org.eclipse.equinox.http.servletbridge rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.servletbridge rt.equinox.bundles
%pom_disable_module bundles/org.eclipse.equinox.servletbridge.template rt.equinox.bundles

# Don't need enforcer on RPM builds
%pom_remove_plugin :maven-enforcer-plugin eclipse-platform-parent

# This part generates secondary fragments using primary fragments
rm -rf eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.{aarch64,s390x,ppc64}
rm -rf rt.equinox.framework/bundles/org.eclipse.equinox.launcher.gtk.linux.{aarch64,s390x,ppc64}
for dir in rt.equinox.binaries rt.equinox.framework/bundles eclipse.platform.swt.binaries/bundles ; do
  utils/ensure_arch.sh "$dir" x86_64 aarch64 s390x ppc64 riscv64
done

# Remove platform-specific stuff that we don't care about to reduce build time
# (i.e., all bundles that are not applicable to the current build platform --
# this reduces the build time on arm by around 20 minutes per architecture that
# we are not currently building)
TYCHO_ENV="<environment><os>linux</os><ws>gtk</ws><arch>%{eclipse_arch}</arch></environment>"
%pom_xpath_set "pom:configuration/pom:environments" "$TYCHO_ENV" eclipse-platform-parent
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
  module=$(grep ">bundles/$b<" rt.equinox.bundles/pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module bundles/$b rt.equinox.bundles
    %pom_xpath_remove -f "plugin[@id='$b']" rt.equinox.p2/features/org.eclipse.equinox.p2.core.feature/feature.xml
  fi
done
for b in `ls eclipse.platform.team/bundles/ | grep -P -e 'org.eclipse.core.net\.(?!linux.%{eclipse_arch}$)'` ; do
  %pom_disable_module bundles/$b eclipse.platform.team
done
for b in `ls eclipse.platform.resources/bundles/ | grep -P -e 'org.eclipse.core.filesystem\.(?!linux\.%{eclipse_arch}$)'` ; do
  module=$(grep ">bundles/$b<" eclipse.platform.resources/pom.xml || :)
  if [ -n "$module" ] ; then
    %pom_disable_module bundles/$b eclipse.platform.resources
  fi
done
%pom_disable_module org.eclipse.jdt.launching.macosx eclipse.jdt.debug
%pom_disable_module org.eclipse.jdt.launching.ui.macosx eclipse.jdt.debug
%pom_disable_module bundles/org.eclipse.compare.win32 eclipse.platform.team
%pom_disable_module org.eclipse.e4.ui.workbench.renderers.swt.cocoa eclipse.platform.ui/bundles
%pom_disable_module org.eclipse.ui.cocoa eclipse.platform.ui/bundles
%pom_disable_module org.eclipse.ui.win32 eclipse.platform.ui/bundles
%pom_disable_module bundles/org.eclipse.core.resources.win32.x86_64 eclipse.platform.resources
for f in eclipse.jdt/org.eclipse.jdt-feature/feature.xml \
         eclipse.platform.ui/features/org.eclipse.e4.rcp/feature.xml \
         eclipse.platform.releng/features/org.eclipse.rcp/feature.xml \
         eclipse.platform.releng/features/org.eclipse.platform-feature/feature.xml ; do
  %pom_xpath_remove -f "plugin[@os='macosx']" $f
  %pom_xpath_remove -f "plugin[@os='win32']" $f
  %pom_xpath_remove -f "plugin[@ws='win32']" $f
  for arch in x86_64 aarch64 ppc64le s390x ppc64 riscv64; do
    if [ "$arch" != "%{eclipse_arch}" ] ; then
      %pom_xpath_remove -f "plugin[@arch='$arch']" $f
    fi
  done
done

%if %{with bootstrap} || %{without contrib_tools}
# Disable contributor tools that have external dependencies during bootstrap
%pom_disable_module eclipse.platform.ui.tools
%pom_disable_module features/org.eclipse.swt.tools.feature eclipse.platform.swt
%pom_disable_module bundles/org.eclipse.swt.tools.base eclipse.platform.swt
%pom_disable_module bundles/org.eclipse.swt.tools.spies eclipse.platform.swt
%pom_disable_module bundles/org.eclipse.swt.tools eclipse.platform.swt
%pom_disable_module features/org.eclipse.releng.tools eclipse.platform.releng
%pom_disable_module bundles/org.eclipse.releng.tools eclipse.platform.releng
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
for f in eclipse.platform.swt.binaries/bundles/org.eclipse.swt.gtk.linux.*/META-INF/MANIFEST.MF \
         eclipse.platform.resources/bundles/org.eclipse.core.filesystem.linux.*/META-INF/MANIFEST.MF \
         eclipse.platform.team/bundles/org.eclipse.core.net.linux.*/META-INF/MANIFEST.MF ; do
    echo -e "Eclipse-BundleShape: dir\n\n" >> $f;
done

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

# Use system osgi.annotation lib
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi/osgi/
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi.services/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.framework/bundles/org.eclipse.osgi.util/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.http.servlet/osgi/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.coordinator/lib/
ln -s $(build-classpath osgi-annotation) rt.equinox.bundles/bundles/org.eclipse.equinox.log.stream/osgi/

# Allow library detector to build on Java 11
sed -i -e 's/target="1.1" source="1.3"/target="1.6" source="1.6"/' eclipse.jdt.debug/org.eclipse.jdt.launching/scripts/buildLaunchingSupportJAR.xml

# The order of these mvn_package calls is important
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":org.eclipse.pde.tools.versioning" contributor-tools
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
%{mvn_package} "org.eclipse.cvs{,.feature}:" cvs
%{mvn_package} "org.eclipse.team:org.eclipse.team.cvs*" cvs
%{mvn_package} "org.eclipse.pde{,.ui,.feature}:" pde
%{mvn_package} ":org.eclipse.pde.api.tools*" pde
%{mvn_package} "org.eclipse.ui:org.eclipse.ui.trace" pde
%{mvn_package} "org.eclipse.sdk{,.feature}:" sdk
%{mvn_package} ":" __noinstall

%build
# Compiler/linker flags for native parts
export M_CFLAGS="$CFLAGS"
export M_ARCH="$LDFLAGS"

#This is the lowest value where the build succeeds. 512m is not enough.
export MAVEN_OPTS="-Xmx1024m -XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState ${MAVEN_OPTS}"
export JAVA_HOME=%{_jvmdir}/java

# Pre-build agent jar needed for AdvancedSourceLookupSupport
sed -i -e '/createSourcesJar/d' -e 's/7\.2/7.0/' eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent/pom.xml
sed -i -e 's/V14/V11/' eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent/src/main/java/org/eclipse/jdt/launching/internal/weaving/ClassfileTransformer.java
(cd eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent && xmvn -e -o -B clean verify)
mv eclipse.jdt.debug/org.eclipse.jdt.launching.javaagent/target/javaagent-shaded.jar \
  eclipse.jdt.debug/org.eclipse.jdt.launching/lib

# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%%y %{SOURCE0})" +v%%Y%%m%%d-%%H%%M)
%{mvn_build} -j -f -- -e -DforceContextQualifier=$QUALIFIER \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{with bootstrap}
    -P !api-generation,!build-docs \
%endif
    -Declipse.javadoc=%{_jvmdir}/java/bin/javadoc -Dnative=gtk.linux.%{eclipse_arch} \
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
%{mvn_package} "org.eclipse.swt:" swt

# Install Maven metadata for OSGi jars
for J in $OSGI_JARS ; do
  JAR=%{buildroot}%{_eclipsedir}/plugins/org.eclipse.${J}_*.jar
  VER=$(echo $JAR | sed -e "s/.*${J}_\(.*\)\.jar/\1/")
  %{mvn_artifact} "org.eclipse.osgi:$J:jar:$VER" $JAR
  %{mvn_alias} "org.eclipse.osgi:$J" "org.eclipse.osgi:org.eclipse.$J" "org.eclipse.platform:org.eclipse.$J"
done

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

#fix so permissions
find %{buildroot}/%{_eclipsedir} -name *.so -exec chmod a+x {} \;

# Usage marker
install -d -m 755 %{buildroot}%{_eclipsedir}/.pkgs
echo "%{version}-%{release}" > %{buildroot}%{_eclipsedir}/.pkgs/Distro%{?dist}

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
%files -n eclipse-platform-bootstrap
%else

%files platform
%endif
%{_bindir}/eclipse
%{_eclipsedir}/eclipse
%{_eclipsedir}/.pkgs
%{_eclipsedir}/.eclipseproduct
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
%{_eclipsedir}/plugins/org.eclipse.e4.ui.ide_*
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
%{_eclipsedir}/plugins/org.eclipse.text.quicksearch_*
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
%{_eclipsedir}/plugins/org.eclipse.ui.views.log_*
%{_eclipsedir}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_eclipsedir}/plugins/org.eclipse.ui.workbench_*
%{_eclipsedir}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_eclipsedir}/plugins/org.eclipse.update.configurator_*
%{_eclipsedir}/plugins/org.eclipse.urischeme_*
%{_eclipsedir}/plugins/org.glassfish.web.javax.servlet.jsp_*
%{_eclipsedir}/plugins/osgi.core_*
%{_eclipsedir}/plugins/org.sat4j.core_*
%{_eclipsedir}/plugins/org.sat4j.pb_*
%{_eclipsedir}/plugins/org.tukaani.xz_*
%{_eclipsedir}/plugins/org.w3c.css.sac_*
%{_eclipsedir}/plugins/org.w3c.dom.svg_*
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
%{_datadir}/appdata/eclipse-pde.metainfo.xml

%if %{with bootstrap}
%files -n eclipse-p2-discovery-bootstrap -f .mfiles-p2-discovery
%else

%files p2-discovery -f .mfiles-p2-discovery
%endif

%if %{with contrib_tools}
%if %{with bootstrap}
%files -n eclipse-contributor-tools-bootstrap -f .mfiles-contributor-tools
%else

%files contributor-tools -f .mfiles-contributor-tools
%endif
%endif

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
