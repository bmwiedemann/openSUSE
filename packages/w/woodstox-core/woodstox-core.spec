#
# spec file for package woodstox-core
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


%global base_name woodstox
%global core_name %{base_name}-core
Name:           %{core_name}
Version:        7.2.1
Release:        0
Summary:        XML processor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/woodstox
Source0:        https://github.com/FasterXML/%{base_name}/archive/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
# Drop requirements on defunct optional dependencies: msv and relaxng
Patch0:         0001-Patch-out-optional-support-for-msv-and-relax-schema-.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jurand
BuildRequires:  osgi-core
BuildRequires:  stax2-api
Provides:       %{base_name} = %{version}
Obsoletes:      %{base_name} < %{version}
BuildArch:      noarch

%description
Woodstox is a validating namespace-aware StAX-compliant (JSR-173) XML
processor written in Java. XML processor means that it handles both
input (= parsing) and output (= writing, serialization)), as well as
supporting tasks such as validation.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1 -n %{base_name}-%{name}-%{version}
cp %{SOURCE1} build.xml

%pom_remove_dep relaxngDatatype:relaxngDatatype
%pom_remove_dep com.sun.xml.bind.jaxb:isorelax
%pom_remove_dep net.java.dev.msv:
rm -rf src/main/java/com/ctc/wstx/msv

# Not needed since pre-generated service files
# are part of the sources
%{java_remove_annotations} . -n ServiceProvider

%build
mkdir -p lib
build-jar-repository -s lib stax2-api osgi-core
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
for i in asl lgpl; do
  ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{name}-${i}.jar
done

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a com.fasterxml.woodstox:%{name}-asl,com.fasterxml.woodstox:%{name}-lgpl

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/*-asl.jar
%{_javadir}/*-lgpl.jar
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
