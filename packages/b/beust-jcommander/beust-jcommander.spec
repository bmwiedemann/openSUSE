#
# spec file for package beust-jcommander
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


%define __requires_exclude java-headless
%global short_name jcommander
Name:           beust-%{short_name}
Version:        1.85
Release:        0
Summary:        Java framework for parsing command line parameters
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://jcommander.org/
Source0:        %{short_name}-%{version}.tar.xz
# Adapted from earlier version that still shipped poms. It uses kobalt for building now
Source1:        %{name}.pom
Source2:        %{name}-build.xml
Patch0:         0001-ParseValues-NullPointerException-patch.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java >= 1.8
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       %{short_name} = %{version}-%{release}
BuildArch:      noarch

%description
JCommander is a Java framework that allows parsing command line
parameters (with annotations).

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{version}
%patch -P 0 -p1

chmod -x license.txt
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} build.xml
sed -i 's/@VERSION@/%{version}/g' pom.xml build.xml

%build
%{ant} jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license license.txt
%doc notice.md README.markdown

%files javadoc
%{_javadocdir}/%{name}

%changelog
