#
# spec file for package apache-commons-email
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


%global base_name       email
%global short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.6.0
Release:        0
Summary:        Apache Commons Email Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-activation-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Commons-Email aims to provide an API for sending email. It is built on top of
the JavaMail API, which it aims to simplify.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/Other

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml

%pom_add_dep javax.activation:javax.activation-api::1.2.0

%build
mkdir -p lib
build-jar-repository -s lib glassfish-activation-api javamail
ant package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{short_name}.jar
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
