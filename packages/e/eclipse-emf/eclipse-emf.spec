#
# spec file for package eclipse-emf
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
%global _eclipsedir %{_libdir}/eclipse
%global emf_tag d1e5fddbdcb41db9a272c8aaaba7689442310efb
%global xsd_tag be9714f28ae9ccc05cee1ee49424f2f97810fe60
Version:        2.15.0~gitd1e5fdd
Release:        0
Summary:        EMF and XSD Eclipse plug-ins
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/modeling/emf/
Source0:        http://git.eclipse.org/c/emf/org.eclipse.emf.git/snapshot/org.eclipse.emf-%{emf_tag}.tar.xz
Source1:        http://git.eclipse.org/c/xsd/org.eclipse.xsd.git/snapshot/org.eclipse.xsd-%{xsd_tag}.tar.xz
# Avoid hard build-time dep on nebula (not in Fedora)
Patch0:         remove-nebula-dep.patch
# Remove test that requires internet connection
Patch1:         remove-network-tests.patch
# Remove test that seems to fail in some timezones, reported upstream: https://bugs.eclipse.org/bugs/show_bug.cgi?id=534542
Patch2:         remove-timezone-test.patch
# Remove unnecessary imports of JRE packages that are supplied by the system bundle
Patch3:         remove-unnecessary-imports.patch
BuildRequires:  tycho-extras
BuildRequires:  xz
BuildConflicts: java-devel >= 9
%if %{with bootstrap}
Name:           eclipse-emf-bootstrap
%else
Name:           eclipse-emf
%endif
BuildRequires:  fdupes
%if %{without bootstrap}
BuildRequires:  eclipse-ecf-core
BuildRequires:  eclipse-emf-core
BuildRequires:  eclipse-emf-core-sdk
BuildRequires:  eclipse-pde-bootstrap
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  jgit-bootstrap
BuildRequires:  tycho
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  jgit
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: log4j
%else
BuildRequires:  tycho-bootstrap
#!BuildIgnore:  jgit
#!BuildIgnore:  jgit-bootstrap
#!BuildIgnore:  tycho
%endif

%description
The Eclipse Modeling Framework (EMF) and XML Schema Definition (XSD) plug-ins.

%if %{with bootstrap}

%package   -n eclipse-emf-core
Summary:        Eclipse EMF Core Bundles
Group:          Development/Libraries/Java

%description -n eclipse-emf-core
Core EMF bundles required by the Eclipse platform.

%package   -n eclipse-emf-core-sdk
Summary:        Eclipse EMF Core Bundles (Sources and source features)
Group:          Development/Libraries/Java
BuildArch:      noarch

%description -n eclipse-emf-core-sdk
Core EMF bundles required by the Eclipse platform.
This package contains the corresponding sources and source features

%else

%package   runtime
Summary:        Eclipse Modeling Framework (EMF) Eclipse plug-in
Group:          Development/Libraries/Java
BuildArch:      noarch

%description runtime
The Eclipse Modeling Framework (EMF) allows developers to build tools and
other applications based on a structured data model. From a model
specification described in XMI, EMF provides tools and run-time support to
produce a set of Java classes for the model, along with a set of adapter
classes that enable viewing and command-based editing of the model, and a
basic editor.

%package   xsd
Summary:        XML Schema Definition (XSD) Eclipse plug-in
Group:          Development/Libraries/Java
BuildArch:      noarch

%description xsd
The XML Schema Definition (XSD) plug-in is a library that provides an API for
manipulating the components of an XML Schema as described by the W3C XML
Schema specifications, as well as an API for manipulating the DOM-accessible
representation of XML Schema as a series of XML documents.

%package   sdk
Summary:        Eclipse EMF and XSD SDK
Group:          Development/Libraries/Java
BuildArch:      noarch

%description sdk
Documentation and developer resources for the Eclipse Modeling Framework
(EMF) plug-in and XML Schema Definition (XSD) plug-in.

%endif

%prep
%setup -q -c -T -a 0 -a 1
mv org.eclipse.emf-%{emf_tag}/ org.eclipse.emf/
mv org.eclipse.xsd-%{xsd_tag}/ org.eclipse.xsd/

%patch0
%patch1
%patch2
%patch3

pushd org.eclipse.emf

# TODO: ODA, GWT, Xtext and RAP components are not packaged, so don't build corresponding bundles
sed -i -e '/org.eclipse.emf.gwt/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
sed -i -e '/org.eclipse.emf.oda/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
sed -i -e '/org.eclipse.emf.rap/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
sed -i -e '/codegen.ecore.xtext/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
sed -i -e '/ecore.xcore/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
sed -i -e '/test.edit.ui.rap/d' releng/org.eclipse.emf.parent/{plugins,features}/pom.xml
%pom_xpath_remove "plugin[@id='org.eclipse.emf.test.edit.ui.rap']" tests/org.eclipse.emf.tests-feature/feature.xml

# Disable example bundles, we don't want to ship them
%pom_disable_module "../../../examples/org.eclipse.emf.examples-feature" releng/org.eclipse.emf.parent/features
%pom_disable_module "../../../../org.eclipse.xsd/features/org.eclipse.xsd.example-feature" releng/org.eclipse.emf.parent/features
sed -i -e '/<module>.*examples/d' releng/org.eclipse.emf.parent/plugins/pom.xml
%pom_xpath_remove "plugin[@id='org.eclipse.emf.test.examples']" tests/org.eclipse.emf.tests-feature/feature.xml

# Disable modules unneeded for tycho build

%pom_disable_module "tp" releng/org.eclipse.emf.parent
%pom_disable_module "../org.eclipse.emf.site" releng/org.eclipse.emf.parent
%pom_disable_module '../../../features/org.eclipse.emf.all-feature' releng/org.eclipse.emf.parent/features

# Disable jgit/target platform stuff that we can't use in RPM builds
%pom_remove_plugin :target-platform-configuration releng/org.eclipse.emf.parent
%pom_remove_dep :tycho-sourceref-jgit releng/org.eclipse.emf.parent
%pom_remove_dep :tycho-buildtimestamp-jgit releng/org.eclipse.emf.parent
%pom_xpath_remove 'pom:configuration/pom:timestampProvider' releng/org.eclipse.emf.parent
%pom_xpath_remove 'pom:configuration/pom:jgit.ignore' releng/org.eclipse.emf.parent
%pom_xpath_remove 'pom:configuration/pom:jgit.dirtyWorkingTree' releng/org.eclipse.emf.parent
%pom_xpath_remove 'pom:configuration/pom:sourceReferences' releng/org.eclipse.emf.parent

%if %{with bootstrap}
# Only build core modules when bootstrapping
%pom_xpath_replace "pom:modules" "<modules>
<module>../../../features/org.eclipse.emf.base-feature</module>
<module>../../../features/org.eclipse.emf.license-feature</module>
<module>../../../features/org.eclipse.emf.common-feature</module>
<module>../../../features/org.eclipse.emf.ecore-feature</module>
</modules>" releng/org.eclipse.emf.parent/features
%pom_xpath_replace "pom:modules" "<modules>
<module>../../../plugins/org.eclipse.emf.common</module>
<module>../../../plugins/org.eclipse.emf.ecore.change</module>
<module>../../../plugins/org.eclipse.emf.ecore.xmi</module>
<module>../../../plugins/org.eclipse.emf.ecore</module>
</modules>" releng/org.eclipse.emf.parent/plugins
%else
%pom_disable_module ../../../features/org.eclipse.emf.base-feature releng/org.eclipse.emf.parent/features
%pom_disable_module ../../../features/org.eclipse.emf.common-feature releng/org.eclipse.emf.parent/features
%pom_disable_module ../../../features/org.eclipse.emf.ecore-feature releng/org.eclipse.emf.parent/features
%pom_disable_module ../../../plugins/org.eclipse.emf.common releng/org.eclipse.emf.parent/plugins
%pom_disable_module ../../../plugins/org.eclipse.emf.ecore.change releng/org.eclipse.emf.parent/plugins
%pom_disable_module ../../../plugins/org.eclipse.emf.ecore.xmi releng/org.eclipse.emf.parent/plugins
%pom_disable_module ../../../plugins/org.eclipse.emf.ecore releng/org.eclipse.emf.parent/plugins
%endif

popd

# Don't install poms or license features
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":org.eclipse.{emf,xsd}.license" __noinstall

# No need to ship tests as they are run at buildtime
%{mvn_package} ":org.eclipse.emf.tests" __noinstall
%{mvn_package} ":org.eclipse.emf.test.*" __noinstall

%{mvn_package} ":::{sources,sources-feature}:" sdk
%{mvn_package} ":org.eclipse.emf.{sdk,doc,cheatsheets,example.installer}" sdk
%{mvn_package} ":org.eclipse.xsd.{sdk,doc,cheatsheets,example.installer}" sdk
%{mvn_package} "org.eclipse.emf.features:org.eclipse.emf.{base,common,ecore}"
%{mvn_package} "org.eclipse.emf:org.eclipse.emf.{common,ecore,ecore.change,ecore.xmi}"
%{mvn_package} ":org.eclipse.xsd*" xsd
%{mvn_package} ":org.eclipse.emf.mapping.xsd**" xsd
%{mvn_package} ":" runtime

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%y %{SOURCE0})" +v%Y%m%d-%H%M)
%{mvn_build} -j -f -- -f org.eclipse.emf/pom.xml -DforceContextQualifier=$QUALIFIER -Dmaven.test.failure.ignore=true

%install
%mvn_install

%if %{with bootstrap}

# Move to libdir due to being part of core platform
install -d -m 755 %{buildroot}%{_eclipsedir}
mv %{buildroot}%{_datadir}/eclipse/droplets/emf/{plugins,features} %{buildroot}%{_eclipsedir}
rm -r %{buildroot}%{_datadir}/eclipse/droplets/emf

# Fixup metadata
sed -i -e 's|%{_datadir}/eclipse/droplets/emf|%{_eclipsedir}|' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml
sed -i -e 's|%{_datadir}/eclipse/droplets/emf/features/|%{_eclipsedir}/features/|' \
       -e 's|%{_datadir}/eclipse/droplets/emf/plugins/|%{_eclipsedir}/plugins/|' .mfiles
sed -i -e '/droplets/d' .mfiles

%endif

# Remove any symlinks that might be created during bootstrapping due to missing platform bundles
for del in $( (cd %{buildroot}%{_eclipsedir}/plugins && ls | grep -v -e '^org\.eclipse\.emf' ) ) ; do
rm %{buildroot}%{_eclipsedir}/plugins/$del
sed -i -e "/$del/d" .mfiles
done

%fdupes -s %{buildroot}%{_eclipsedir}
%fdupes -s %{buildroot}%{_datadir}/eclipse

%if %{with bootstrap}

%files -n eclipse-emf-core -f .mfiles
%license org.eclipse.emf/features/org.eclipse.emf.license-feature/*.html

%files -n eclipse-emf-core-sdk -f .mfiles-sdk

%else

%files runtime -f .mfiles-runtime

%files xsd -f .mfiles-xsd

%files sdk -f .mfiles-sdk

%endif

%changelog
