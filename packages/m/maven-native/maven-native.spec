#
# spec file for package maven-native
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


%global namedversion 1.0-M1
Name:           maven-native
Version:        1.0~M1
Release:        0
Summary:        Maven plugin to compile C and C++ source
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://www.mojohaus.org/plugins.html
# Source code available @ https://github.com/mojohaus/maven-native
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/natives/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mojo-parent
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.bcel:bcel)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildArch:      noarch

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%package components
Summary:        Maven Native Components
Group:          Development/Libraries/Java

%description components
%{summary}.

%package -n native-maven-plugin
Summary:        Native Maven Plugin
Group:          Development/Libraries/Java

%description -n native-maven-plugin
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin -r :sortpom-maven-plugin

%{mvn_package} ":%{name}" %{name}
%{mvn_package} ":%{name}-api" %{name}
%{mvn_package} ":%{name}-components" components
%{mvn_package} ":%{name}-bcc" components
%{mvn_package} ":%{name}-generic-c" components
%{mvn_package} ":%{name}-javah" components
%{mvn_package} ":%{name}-manager" components
%{mvn_package} ":%{name}-msvc" components
%{mvn_package} ":%{name}-mingw" components
%{mvn_package} ":native-maven-plugin" native-maven-plugin
# Empty, manifest-only jar
%{mvn_package} ":%{name}-test" __noinstall

%build

%{mvn_build} -f -s -- -Dmojo.java.target=8 -Dmaven.test.failure.ignore=true -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%license LICENSE.txt

%files components -f .mfiles-components
%license LICENSE.txt

%files -n native-maven-plugin -f .mfiles-native-maven-plugin
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
