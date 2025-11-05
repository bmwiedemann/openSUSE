#
# spec file for package plexus-sec-dispatcher4
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global base_name plexus-sec-dispatcher
%global version_suffix 4
Name:           %{base_name}%{version_suffix}
Version:        4.1.0
Release:        0
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{base_name}
Source0:        https://github.com/codehaus-plexus/%{base_name}/archive/refs/tags/%{base_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  modello >= 2.0.0
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  slf4j2
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildArch:      noarch

%description
Plexus Security Dispatcher Component

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{base_name}-%{version}

cp %{SOURCE1} .
cp %{SOURCE100} build.xml

# Normalize slf4j version to 2
%pom_xpath_set pom:project/pom:properties/pom:version.slf4j 2

%build
mkdir -p lib
build-jar-repository -s lib \
    javax.inject \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    slf4j/api-2
%{ant} \
  jar javadoc

%{mvn_file} :plexus-{*} plexus/@1 plexus/plexus-@1
%{mvn_artifact} pom.xml target/%{base_name}-%{version}.jar
%{mvn_compat_version} : %{version_suffix} %{version}

%install
%mvn_install

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
