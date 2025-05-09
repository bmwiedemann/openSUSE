#
# spec file for package jakarta-mail
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


%global srcname mail-api
%global artifact_name jakarta.%{srcname}
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           jakarta-mail
Version:        2.1.3
Release:        0
Summary:        Jakarta Mail API
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/jakartaee/mail-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-activation
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{srcname}-%{version}
cp %{SOURCE1} api/build.xml

%build
pushd api
mkdir -p lib
build-jar-repository -s lib jakarta-activation
%{ant} package javadoc
popd

%install
pushd api
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -p -m 0644 target/%{artifact_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifact_name}.jar

#pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifact_name}.pom
%add_maven_depmap %{name}/%{artifact_name}.pom %{name}/%{artifact_name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
popd

%fdupes -s %{buildroot}%{_javadocdir}

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
