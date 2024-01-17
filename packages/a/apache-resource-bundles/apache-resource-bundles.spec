#
# spec file for package apache-resource-bundles
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global jar_version 1.4
%global lh_version 1.1
%global id_version 1.1
Name:           apache-resource-bundles
Version:        2
Release:        0
Summary:        Apache Resource Bundles
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://repo1.maven.org/maven2/org/apache/apache-resource-bundles/
Source0:        https://repo1.maven.org/maven2/org/apache/%{name}/%{version}/%{name}-%{version}.pom
Source1:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}-sources.jar
Source2:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}.pom
Source3:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}-sources.jar
Source4:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}.pom
Source5:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}-sources.jar
Source6:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}.pom
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  unzip
BuildArch:      noarch

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

%prep
%setup -q -cT
cp -p %{SOURCE0} ./pom.xml

# jar
mkdir -p apache-jar-resource-bundle
pushd apache-jar-resource-bundle
jar xvf %{SOURCE1}
cp -p %{SOURCE2} ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# license-header
mkdir -p apache-license-header-resource-bundle
pushd apache-license-header-resource-bundle
jar xvf %{SOURCE3}
cp -p %{SOURCE4} ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# incubator-disclaimer
mkdir -p apache-incubator-disclaimer-resource-bundle
pushd apache-incubator-disclaimer-resource-bundle
jar xvf %{SOURCE5}
cp -p %{SOURCE6} ./pom.xml
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

%{mvn_file} :apache-jar-resource-bundle apache-resource-bundles/jar
%{mvn_file} :apache-license-header-resource-bundle apache-resource-bundles/license-header
%{mvn_file} :apache-incubator-disclaimer-resource-bundle apache-resource-bundles/incubator-disclaimer

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles

%changelog
