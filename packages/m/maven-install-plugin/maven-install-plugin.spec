#
# spec file for package maven-install-plugin
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


%global base_ver 3.0.0
%global milestone M1
%bcond_with tests
Name:           maven-install-plugin
Version:        %{base_ver}~%{milestone}
Release:        0
Summary:        Maven Install Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-install-plugin
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{base_ver}-%{milestone}/%{name}-%{base_ver}-%{milestone}-source-release.zip
Patch0:         0001-MINSTALL-143-Remove-a-lot-of-checksum-related-dead-c.patch
Patch1:         0002-MINSTALL-171-Update-plugin-requires-Maven-3.2.5.patch
Patch2:         0003-Fix-tests-with-modular-javas.patch
Patch3:         0004-Fix-tests-with-maven-resolver-1.7.3.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch
%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-impl) >= 1.7
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
%endif

%description
Copies the project artifacts to the user's local repository.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{base_ver}-%{milestone}
%autopatch -p1

%build
%{mvn_build} \
%if %{without tests}
    -f \
%endif
    -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
