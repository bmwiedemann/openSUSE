#
# spec file for package eclipse-emf-bootstrap
#
# Copyright (c) 2022 SUSE LLC
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
%global emf_tag R2_22_0
%global xsd_tag R2_22_0
Version:        2.22.0
Release:        0
Summary:        EMF and XSD Eclipse plug-ins
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/modeling/emf/
Source0:        https://git.eclipse.org/c/emf/org.eclipse.emf.git/snapshot/org.eclipse.emf-%{emf_tag}.tar.xz
Source1:        https://git.eclipse.org/c/xsd/org.eclipse.xsd.git/snapshot/org.eclipse.xsd-%{xsd_tag}.tar.xz
# Avoid hard build-time dep on nebula
Patch0:         0001-Remove-dependency-on-nebula.patch
# Remove test that requires internet connection
Patch1:         0002-Remove-test-that-requires-talking-to-the-internet.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  xz
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}
%if %{with bootstrap}
Name:           eclipse-emf-bootstrap
BuildRequires:  tycho-bootstrap
#!BuildIgnore:  tycho
%else
Name:           eclipse-emf
BuildRequires:  eclipse-ecf-core-bootstrap
BuildRequires:  eclipse-emf-core-bootstrap
BuildRequires:  eclipse-pde-bootstrap
BuildRequires:  eclipse-platform-bootstrap
BuildRequires:  jgit
BuildRequires:  tycho
#!BuildIgnore:  eclipse-platform
#!BuildIgnore:  tycho-bootstrap
#!BuildRequires: log4j
%endif

%description
The Eclipse Modeling Framework (EMF) and XML Schema Definition (XSD) plug-ins.

%if %{with bootstrap}
%package   -n eclipse-emf-core-bootstrap
%else

%package   core
Obsoletes:      eclipse-emf-core-bootstrap
%endif
Summary:        Eclipse EMF Core Bundles
Group:          Development/Libraries/Java

%if %{with bootstrap}
%description -n eclipse-emf-core-bootstrap
%else

%description core
%endif
Core EMF bundles required by the Eclipse platform.

%if %{without bootstrap}
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
Obsoletes:      %{name}-core-sdk
BuildArch:      noarch

%description sdk
Documentation and developer resources for the Eclipse Modeling Framework
(EMF) plug-in and XML Schema Definition (XSD) plug-in.
%endif

%prep
%setup -q -c -T -a 0 -a 1
mv org.eclipse.emf-%{emf_tag}/ org.eclipse.emf/
mv org.eclipse.xsd-%{xsd_tag}/ org.eclipse.xsd/

%patch0 -p1
%patch1 -p1

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
%endif

popd

# Don't install poms or license features
%{mvn_package} "::pom::" __noinstall
%{mvn_package} ":org.eclipse.{emf,xsd}.license" __noinstall
%{mvn_package} ":org.eclipse.emf.base" __noinstall

# No need to ship tests as they are run at buildtime
%{mvn_package} ":org.eclipse.emf.tests" __noinstall
%{mvn_package} ":org.eclipse.emf.test.*" __noinstall

%if %{with bootstrap}
%{mvn_package} ":::{sources,sources-feature}:" __noinstall
%else
%{mvn_package} ":::{sources,sources-feature}:" sdk
%endif
%{mvn_package} ":org.eclipse.emf.{sdk,doc,cheatsheets,example.installer}" sdk
%{mvn_package} ":org.eclipse.xsd.{sdk,doc,cheatsheets,example.installer}" sdk
%{mvn_package} "org.eclipse.emf.features:org.eclipse.emf.{base,common,ecore}"
%{mvn_package} "org.eclipse.emf:org.eclipse.emf.{common,ecore,ecore.change,ecore.xmi}"
%{mvn_package} ":org.eclipse.xsd*" xsd
%{mvn_package} ":org.eclipse.emf.mapping.xsd**" xsd
%{mvn_package} ":" runtime

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%%y %{SOURCE0})" +v%%Y%%m%%d-%%H%%M)
%{mvn_build} -j -f -- -f org.eclipse.emf/pom.xml -DforceContextQualifier=$QUALIFIER -Dmaven.test.failure.ignore=true

%install
%mvn_install

# Move to libdir due to being part of core platform
install -d -m 755 %{buildroot}%{_eclipsedir}
mv %{buildroot}%{_datadir}/eclipse/droplets/emf/{plugins,features} %{buildroot}%{_eclipsedir}
rm -r %{buildroot}%{_datadir}/eclipse/droplets/emf

# Fixup metadata
sed -i -e 's|%{_datadir}/eclipse/droplets/emf|%{_eclipsedir}|' %{buildroot}%{_datadir}/maven-metadata/%{name}.xml
sed -i -e 's|%{_datadir}/eclipse/droplets/emf/features/|%{_eclipsedir}/features/|' \
       -e 's|%{_datadir}/eclipse/droplets/emf/plugins/|%{_eclipsedir}/plugins/|' .mfiles
sed -i -e '/droplets/d' .mfiles

# Remove any symlinks that might be created during bootstrapping due to missing platform bundles
for del in $( (cd %{buildroot}%{_eclipsedir}/plugins && ls | grep -v -e '^org\.eclipse\.emf' ) ) ; do
rm %{buildroot}%{_eclipsedir}/plugins/$del
sed -i -e "/$del/d" .mfiles
done

%fdupes -s %{buildroot}%{_eclipsedir}
%fdupes -s %{buildroot}%{_datadir}/eclipse

%if %{with bootstrap}
%files -n eclipse-emf-core-bootstrap -f .mfiles
%else

%files core -f .mfiles
%endif
%license org.eclipse.emf/features/org.eclipse.emf.license-feature/*.html

%if %{without bootstrap}
%files runtime -f .mfiles-runtime

%files xsd -f .mfiles-xsd

%files sdk -f .mfiles-sdk
%endif

%changelog
