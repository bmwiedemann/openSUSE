#
# spec file for package plexus-ant-factory
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


%global parent plexus
%global subname ant-factory
%global base_ver 1.0
%global alpha_ver 2.1
%global namedversion %{base_ver}-alpha-%{alpha_ver}
%bcond_with tests
Name:           %{parent}-%{subname}
Version:        %{base_ver}~a%{alpha_ver}
Release:        0
Summary:        Plexus Ant component factory
# Email from copyright holder confirms license.
# See plexus-ant-factory_license_and_copyright.txt
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/tags/plexus-ant-factory-1.0-alpha-2.1/ plexus-ant-factory/
# tar cjf plexus-ant-factory-src.tar.bz2 plexus-ant-factory/
Source0:        %{name}-src.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        %{name}-build.xml
Source100:      plexus-ant-factory_license_and_copyright.txt
Patch0:         plexus-ant-factory-sisu-plexus.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
Ant component class creator for Plexus.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
%patch -P 0 -p1
cp %{SOURCE1} LICENSE
cp %{SOURCE2} build.xml
%pom_change_dep :plexus-container-default org.eclipse.sisu:org.eclipse.sisu.plexus:0.9.0.M2

%build
mkdir -p lib

build-jar-repository -s lib plexus/classworlds plexus/utils org.eclipse.sisu.plexus
%{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  jar

build-jar-repository -s lib ant/ant
%{ant} javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{parent}
install -pm 0644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{parent}/%{subname}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{parent}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{parent}/%{subname}.pom
%add_maven_depmap %{parent}/%{subname}.pom %{parent}/%{subname}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%dir %{_javadir}/plexus

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
