#
# spec file for package open-test-reporting
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


%global basever 0.1.0
%global milestone M2
%global filever %{basever}-%{milestone}
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           open-test-reporting
Version:        %{basever}~%{milestone}
Release:        0
Summary:        Language-agnostic test reporting format and tooling
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/ota4j-team/%{name}
Source0:        https://github.com/ota4j-team/%{name}/archive/refs/tags/r%{filever}.tar.gz
Source1:        %{name}-build.tar.xz
Source10:       https://repo1.maven.org/maven2/org/opentest4j/reporting/%{name}-cli/%{filever}/%{name}-cli-%{filever}.pom
Source11:       https://repo1.maven.org/maven2/org/opentest4j/reporting/%{name}-events/%{filever}/%{name}-events-%{filever}.pom
Source12:       https://repo1.maven.org/maven2/org/opentest4j/reporting/%{name}-schema/%{filever}/%{name}-schema-%{filever}.pom
Source13:       https://repo1.maven.org/maven2/org/opentest4j/reporting/%{name}-tooling/%{filever}/%{name}-tooling-%{filever}.pom
Patch0:         0001-Java-8-compatibility.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  picocli
BuildRequires:  slf4j
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Test reporting formats that are agnostic of testing framework
and programming language.

%package cli
Summary:        Module 'cli' of %{name}
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description cli
Test reporting formats that are agnostic of testing framework
and programming language.
This package contains the module 'cli'.

%package events
Summary:        Module 'events' of %{name}
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description events
Test reporting formats that are agnostic of testing framework
and programming language.
This package contains the module 'events'

%package schema
Summary:        Module 'schema' of %{name}
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description schema
Test reporting formats that are agnostic of testing framework
and programming language.
This package contains the module 'schema'.

%package tooling
Summary:        Module 'tooling' of %{name}
Group:          Development/Libraries/Java
Requires:       java-headless >= 9

%description tooling
Test reporting formats that are agnostic of testing framework
and programming language.
This package contains the module 'tooling'.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-r%{filever} -a1
%patch -P 0 -p1
cp %{SOURCE10} cli/pom.xml
cp %{SOURCE11} events/pom.xml
cp %{SOURCE12} schema/pom.xml
cp %{SOURCE13} tooling/pom.xml
mkdir -p lib

%pom_change_dep :log4j-slf4j-impl : cli '
    <optional>true</optional>'

%build
build-jar-repository -s lib picocli/picocli slf4j/api

%{ant} package javadoc

%install
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -d -m 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
for module in schema events tooling cli; do
  # jars
  install -p -m 0644 ${module}/target/%{name}-${module}.jar %{buildroot}%{_javadir}/%{name}/${module}.jar
  #pom
  %{mvn_install_pom} ${module}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${module}.pom
  %add_maven_depmap %{name}/${module}.pom %{name}/${module}.jar -f ${module}
  # javadoc
  cp -r ${module}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${module}
done

%fdupes -s %{buildroot}%{_javadocdir}

%files cli -f .mfiles-cli
%license LICENSE.md

%files events -f .mfiles-events
%license LICENSE.md

%files schema -f .mfiles-schema
%license LICENSE.md

%files tooling -f .mfiles-tooling
%license LICENSE.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
