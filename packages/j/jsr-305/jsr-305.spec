#
# spec file for package jsr-305
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


Name:           jsr-305
Version:        3.0.2
Release:        0
Summary:        Correctness annotations for Java code
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://code.google.com/p/jsr-305/
Source0:        %{name}-%{version}.tar.xz
Source1:        jsr-305-ri-build.xml
# File containing URL to CC-BY license text
Source2:        NOTICE-CC-BY.txt
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Documentation/HTML

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp -a %{SOURCE1} ri/build.xml
cp %{SOURCE2} NOTICE-CC-BY
dos2unix sampleUses/pom.xml

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

for module in ri tcl sampleUses proposedAnnotations; do
  %pom_remove_parent ${module}
done

%build
pushd ri
%{ant} jar javadoc
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 ri/target/jsr305-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/jsr305.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 ri/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr ri/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license ri/LICENSE NOTICE-CC-BY
%{_javadir}/jsr305.jar

%files javadoc
%license ri/LICENSE NOTICE-CC-BY
%{_javadocdir}/%{name}

%changelog
