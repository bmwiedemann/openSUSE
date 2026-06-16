#
# spec file for package jakarta-messaging
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


%global srcname messaging
%global src_ver %{version}-RELEASE
# The automatic requires would be java-headless >= 11, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           jakarta-messaging
Version:        3.1.0
Release:        0
Summary:        JMS / Jakarta Messaging API
License:        EPL-2.0 OR GPL-2.0 WITH Classpath-Exception
Group:          Development/Libraries/Java
URL:            https://github.com/jakartaee/messaging
Source0:        %{url}/archive/%{src_ver}/%{srcname}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-annotations
BuildRequires:  java-devel >= 11
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
This package contains the API definition source code for the Jakarta
Messaging API.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{srcname}-%{src_ver}
cp %{SOURCE1} api/build.xml

# remove unnecessary maven plugins
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-jar-plugin api

%build
pushd api
mkdir -p lib
build-jar-repository -s lib jakarta-annotations
%{ant} package javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/jakarta.jms-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/jakarta.jms-api.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jakarta.jms-api.pom
%add_maven_depmap %{name}/jakarta.jms-api.pom %{name}/jakarta.jms-api.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
