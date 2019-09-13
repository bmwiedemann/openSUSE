#
# spec file for package joda-convert
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           joda-convert
Version:        1.9.2
Release:        0
Summary:        Java library for conversion to and from standard string formats
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/JodaOrg/joda-convert/
Source0:        https://github.com/JodaOrg/joda-convert/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  guava20
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Java library to enable conversion to and from standard string formats.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml
dos2unix *.txt

%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%{ant} \
  -Dguava20.jar=%{_javadir}/guava20/guava-20.0.jar \
  clean jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
