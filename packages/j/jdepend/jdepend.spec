#
# spec file for package jdepend
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


Name:           jdepend
Version:        2.10
Release:        0
Summary:        Java Design Quality Metrics
License:        MIT
Group:          Development/Libraries/Java
URL:            http://www.clarkware.com/software/JDepend.html
Source0:        https://github.com/clarkware/jdepend/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%package demo
Summary:        Demonstration and sample files for jdepend
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

This package contains demonstration and sample files for JDepend.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
%{ant} \
	-Dant.build.javac.source=1.8 \
	-Dant.build.javac.target=1.8 \
	jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 dist/%{name}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}
cp -pr build/docs/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# # demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr sample %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.md
%doc CHANGELOG.md README.md

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
