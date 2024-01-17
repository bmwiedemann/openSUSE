#
# spec file for package aqute-bnd
#
# Copyright (c) 2023 SUSE LLC
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


Name:           aqute-bnd
Version:        6.3.1
Release:        0
Summary:        BND Tool
# Part of jpm is under BSD, but jpm is not included in binary RPM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://bnd.bndtools.org/
Source0:        bnd-%{version}.tar.xz
Source1:        bnd-%{version}-build_xml.tar.xz
Source2:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.exporters/%{version}/biz.aQute.bnd.exporters-%{version}.pom
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/aQute.libg/%{version}/aQute.libg-%{version}.pom
Source4:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source5:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
Source6:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.annotation/%{version}/biz.aQute.bnd.annotation-%{version}.pom
Source7:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.ant/%{version}/biz.aQute.bnd.ant-%{version}.pom
Source8:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.util/%{version}/biz.aQute.bnd.util-%{version}.pom
Patch1:         0001-Disable-removed-commands.patch
Patch2:         0002-Port-to-OSGI-7.0.0.patch
Patch3:         0003-Remove-unmet-dependencies.patch
Patch4:         reproducible-timestamps.patch
Patch5:         reproducible-packages-list.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jline
BuildRequires:  osgi-annotation
BuildRequires:  osgi-compendium
BuildRequires:  osgi-core
BuildRequires:  slf4j
Requires:       %{name}lib = %{version}-%{release}
# Explicit javapackages-tools requires since bnd script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
BuildArch:      noarch

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package -n aqute-bndlib
Summary:        BND library
Group:          Development/Libraries/Java

%description -n aqute-bndlib
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n bnd-%{version} -a 1

mkdir -p lib
build-jar-repository -s lib \
  slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium ant jline

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# the commands pull in more dependencies than we want (felix-resolver, jetty)
rm biz.aQute.bnd/src/aQute/bnd/main/{ExportReportCommand,MbrCommand,RemoteCommand,ReporterLogger,ResolveCommand,Shell}.java

sed -i 's|${Bundle-Version}|%{version}|' biz.aQute.bndlib/src/aQute/bnd/osgi/bnd.info

# libg
pushd aQute.libg
cp -p %{SOURCE3} pom.xml
%pom_add_dep org.osgi:osgi.cmpn:7
%pom_remove_dep org.osgi:org.osgi.dto
%pom_remove_dep org.osgi:org.osgi.framework
%pom_remove_dep org.osgi:org.osgi.resource
%pom_remove_dep org.osgi:org.osgi.util.function
%pom_remove_dep org.osgi:org.osgi.util.promise
%pom_xpath_remove pom:dependency/pom:scope
popd

# bnd.annotation
pushd biz.aQute.bnd.annotation
cp -p %{SOURCE6} pom.xml
%pom_add_dep org.osgi:osgi.core:7
%pom_add_dep org.osgi:osgi.cmpn:7
%pom_remove_dep org.osgi:org.osgi.namespace.extender
%pom_remove_dep org.osgi:org.osgi.namespace.service
%pom_remove_dep org.osgi:org.osgi.resource
%pom_remove_dep org.osgi:org.osgi.service.serviceloader
%pom_xpath_remove pom:dependency/pom:scope
popd

# bndlib
pushd biz.aQute.bndlib
cp -p %{SOURCE5} pom.xml
%pom_add_dep org.osgi:osgi.cmpn:7
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
%pom_remove_dep org.osgi:org.osgi.dto
%pom_remove_dep org.osgi:org.osgi.framework
%pom_remove_dep org.osgi:org.osgi.namespace.contract
%pom_remove_dep org.osgi:org.osgi.namespace.extender
%pom_remove_dep org.osgi:org.osgi.namespace.implementation
%pom_remove_dep org.osgi:org.osgi.namespace.service
%pom_remove_dep org.osgi:org.osgi.resource
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.repository
%pom_remove_dep org.osgi:org.osgi.util.function
%pom_remove_dep org.osgi:org.osgi.util.promise
%pom_remove_dep org.osgi:org.osgi.util.tracker
%pom_xpath_remove pom:dependency/pom:scope
popd

# bnd.ant
pushd biz.aQute.bnd.ant
cp -p %{SOURCE7} pom.xml
%pom_xpath_remove pom:dependency/pom:scope
popd

# bnd.exporters
pushd biz.aQute.bnd.exporters
cp -p %{SOURCE2} pom.xml
%pom_remove_dep org.osgi:org.osgi.service.subsystem
%pom_xpath_remove pom:dependency/pom:scope
popd

# bnd
pushd biz.aQute.bnd
cp -p %{SOURCE4} pom.xml
%pom_remove_dep :biz.aQute.resolve
%pom_remove_dep :biz.aQute.repository
%pom_remove_dep :biz.aQute.bnd.reporter
%pom_remove_dep :biz.aQute.remote.api
%pom_remove_dep :snakeyaml
%pom_remove_dep :jline
%pom_remove_dep org.osgi:org.osgi.service.coordinator
%pom_remove_dep org.osgi:org.osgi.service.resolver
%pom_remove_dep org.osgi:org.osgi.dto
%pom_remove_dep org.osgi:org.osgi.framework
%pom_remove_dep org.osgi:org.osgi.resource
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.repository
%pom_remove_dep org.osgi:org.osgi.util.function
%pom_remove_dep org.osgi:org.osgi.util.promise
%pom_remove_dep org.osgi:org.osgi.util.tracker
%pom_xpath_remove pom:dependency/pom:scope
popd

# bnd.util
pushd biz.aQute.bnd.util
cp -p %{SOURCE8} pom.xml
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_xpath_remove pom:dependency/pom:scope
popd

%build
%{ant}
%{ant} javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 biz.aQute.bnd.exporters/target/biz.aQute.bnd.exporters-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bnd.exporters.jar
install -pm 0644 biz.aQute.bnd.util/target/biz.aQute.bnd.util-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bnd.util.jar
install -pm 0644 biz.aQute.bnd.annotation/target/biz.aQute.bnd.annotation-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bnd.annotation.jar
install -pm 0644 aQute.libg/target/aQute.libg-%{version}.jar %{buildroot}%{_javadir}/%{name}/aQute.libg.jar
install -pm 0644 biz.aQute.bndlib/target/biz.aQute.bndlib-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bndlib.jar
install -pm 0644 biz.aQute.bnd/target/biz.aQute.bnd-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bnd.jar
install -pm 0644 biz.aQute.bnd.ant/target/biz.aQute.bnd.ant-%{version}.jar %{buildroot}%{_javadir}/%{name}/biz.aQute.bnd.ant.jar
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} biz.aQute.bnd.exporters/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bnd.exporters.pom
%add_maven_depmap %{name}/biz.aQute.bnd.exporters.pom %{name}/biz.aQute.bnd.exporters.jar -f bndlib
%{mvn_install_pom} biz.aQute.bnd.util/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bnd.util.pom
%add_maven_depmap %{name}/biz.aQute.bnd.util.pom %{name}/biz.aQute.bnd.util.jar -f bndlib
%{mvn_install_pom} biz.aQute.bnd.annotation/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bnd.annotation.pom
%add_maven_depmap %{name}/biz.aQute.bnd.annotation.pom %{name}/biz.aQute.bnd.annotation.jar -f bndlib
%{mvn_install_pom} aQute.libg/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/aQute.libg.pom
%add_maven_depmap %{name}/aQute.libg.pom %{name}/aQute.libg.jar -f bndlib
%{mvn_install_pom} biz.aQute.bndlib/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bndlib.pom
%add_maven_depmap %{name}/biz.aQute.bndlib.pom %{name}/biz.aQute.bndlib.jar -f bndlib -a biz.aQute.bnd:bndlib,biz.aQute:bndlib
%{mvn_install_pom} biz.aQute.bnd/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bnd.pom
%add_maven_depmap %{name}/biz.aQute.bnd.pom %{name}/biz.aQute.bnd.jar -a biz.aQute.bnd:bnd,biz.aQute:bnd
%{mvn_install_pom} biz.aQute.bnd.ant/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/biz.aQute.bnd.ant.pom
%add_maven_depmap %{name}/biz.aQute.bnd.ant.pom %{name}/biz.aQute.bnd.ant.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
mv biz.aQute.bnd.exporters/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bnd.exporters
mv biz.aQute.bnd.util/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bnd.util
mv biz.aQute.bnd.annotation/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bnd.annotation
mv aQute.libg/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/aQute.libg
mv biz.aQute.bndlib/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bndlib
mv biz.aQute.bnd/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bnd
mv biz.aQute.bnd.ant/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/biz.aQute.bnd.ant
%fdupes -s %{buildroot}%{_javadocdir}

install -d -m 755 %{buildroot}%{_sysconfdir}/ant.d
echo "aqute-bnd slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium" >%{buildroot}%{_sysconfdir}/ant.d/%{name}

%jpackage_script aQute.bnd.main.bnd "" "" aqute-bnd:slf4j/api:slf4j/simple:osgi-annotation:osgi-core:osgi-compendium bnd 1

%files -f .mfiles
%license LICENSE
%{_bindir}/bnd
%config(noreplace) %{_sysconfdir}/ant.d/*
%dir %{_sysconfdir}/ant.d

%files -n aqute-bndlib -f .mfiles-bndlib
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}

%changelog
