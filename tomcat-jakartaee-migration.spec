#
# spec file for package tomcat-jakartaee-migration
#
# Copyright (c) 2023 SUSE LLC
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


%global artifactId jakartaee-migration
Name:           tomcat-jakartaee-migration
Version:        1.0.7
Release:        0
Summary:        Tomcat JakartaEE Migration
License:        Apache-2.0
URL:            https://tomcat.apache.org/download-migration.cgi
Source0:        https://archive.apache.org/dist/tomcat/%{artifactId}/v%{version}/source/%{artifactId}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  bcel
BuildRequires:  commons-compress
BuildRequires:  commons-io
BuildRequires:  commons-lang3
BuildRequires:  javapackages-local
Requires:       bcel
Requires:       commons-compress
Requires:       commons-io
Requires:       commons-lang3
Requires:       javapackages-tools
BuildArch:      noarch

%description
The purpose of the tool is to take a web application written for
Java EE 8 that runs on Apache Tomcat 9 and convert it automatically
so it runs on Apache Tomcat 10 which implements Jakarta EE 9.

The tool can be used from the command line or as an Ant task.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib bcel commons-compress commons-io ant/ant
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0755 target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifactId}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
%add_maven_depmap %{name}/%{artifactId}.pom %{name}/%{artifactId}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# script
%jpackage_script org.apache.tomcat.jakartaee.MigrationCLI "" "" %{name}:bcel:commons-compress:commons-io:commons-lang3 javax2jakarta true

# ant
install -d -m 0755 %{buildroot}%{_sysconfdir}/ant.d
echo "%{name} bcel commons-compress commons-io commons-lang3" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%{_bindir}/javax2jakarta
%{_sysconfdir}/ant.d/%{name}
%license LICENSE.txt NOTICE.txt
%doc README.md CHANGES.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
