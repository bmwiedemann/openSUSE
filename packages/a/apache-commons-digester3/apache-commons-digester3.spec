#
# spec file for package apache-commons-digester3
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


%define base_name       digester3
%define short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        3.2
Release:        0
Summary:        Apache Commons Digester
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-digester/
Source:         https://mirror.linux-ia64.org/apache/commons/digester/source/%{short_name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh)
BuildArch:      noarch

%description
The Apache Commons Digester package lets you configure an XML to Java object
mapping module which triggers certain actions called rules whenever a
particular pattern of nested XML elements is recognized.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin
%pom_remove_plugin :maven-jar-plugin
%{mvn_file} : %{name} %{short_name}

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dmaven.compiler.{source,target}=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
