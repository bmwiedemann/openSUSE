#
# spec file for package apache-resource-bundles
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           apache-resource-bundles
Version:        1.8
Release:        0
Summary:        Apache Resource Bundles
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/apache-resource-bundles/
Source0:        https://repo1.maven.org/maven2/org/apache/apache/resources/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

%prep
%setup -q

%pom_disable_module resources-bundles-sample

%mvn_alias : org.apache:

%{mvn_file} :apache-jar-resource-bundle apache-resource-bundles/jar
%{mvn_file} :apache-jar-txt-resource-bundle apache-resource-bundles/jar-txt
%{mvn_file} :apache-license-header-resource-bundle apache-resource-bundles/license-header
%{mvn_file} :apache-incubator-disclaimer-resource-bundle apache-resource-bundles/incubator-disclaimer
%{mvn_file} :apache-source-release-assembly-descriptor apache-resource-bundles/source-release

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles

%changelog
