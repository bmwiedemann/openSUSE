#
# spec file for package plexus-i18n
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


%global base_ver 1.0
%global beta_ver 10
%global namedver %{base_ver}-beta-%{beta_ver}
%global parent plexus
%global subname i18n
%bcond_with tests
Name:           %{parent}-%{subname}
Version:        1.0~beta10
Release:        0
Summary:        Plexus I18N Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-i18n
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10/
# tar cjf plexus-i18n-1.0-beta-10-src.tar.bz2 plexus-i18n-1.0-beta-10/
Source0:        %{name}-%{namedver}-src.tar.bz2
Source1:        %{name}-build.xml
Patch0:         %{name}-migration-to-component-metadata.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  guava
BuildRequires:  xbean
BuildConflicts: java-devel >= 9
%endif

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedver}
cp %{SOURCE1} build.xml
%patch -P 0 -p1

%pom_add_dep org.eclipse.sisu:org.eclipse.sisu.plexus:0.9.0.M2

%build
mkdir -p lib
build-jar-repository -s lib \
    plexus/utils \
    org.eclipse.sisu.plexus
%if %{with tests}
build-jar-repository -s lib \
    guava/guava \
    xbean/xbean-reflect \
    plexus/classworlds
%endif

%{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{namedver}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
