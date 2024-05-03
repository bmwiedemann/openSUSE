#
# spec file for package plexus-build-api0
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


%global base_name plexus-build-api
Name:           %{base_name}0
Version:        0.0.8
Release:        0
Summary:        Sonatype Plexus Build API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-build-api
Source0:        https://github.com/codehaus-plexus/%{base_name}/archive/refs/tags/%{base_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        %{name}-build.xml
Patch0:         plexus-build-api0-utils-3.3.0.patch
Patch1:         plexus-build-api0-javadoc.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildArch:      noarch

%description
Sonatype Plexus Build API

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{base_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
cp -p %{SOURCE1} LICENSE
cp -p %{SOURCE2} build.xml

%pom_remove_parent .

%build
mkdir -p lib
build-jar-repository -s lib plexus/utils plexus/classworlds plexus-containers/plexus-container-default
%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{base_name}-%{version}.jar %{buildroot}%{_javadir}/plexus/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/%{name}.pom
%add_maven_depmap plexus/%{name}.pom plexus/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
