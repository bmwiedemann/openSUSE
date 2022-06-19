#
# spec file for package jdepend
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


%define section		free
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
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Obsoletes:      %{name}-javadoc
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

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
%{ant} \
	-Dant.build.javac.source=1.8 \
	-Dant.build.javac.target=1.8 \
	jar

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar

# # demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr sample %{buildroot}%{_datadir}/%{name}

%files
%defattr(0644,root,root,0755)
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_javadir}/*
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%changelog
