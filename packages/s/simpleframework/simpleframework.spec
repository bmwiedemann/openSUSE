#
# spec file for package simpleframework
#
# Copyright (c) 2025 SUSE LLC
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


Name:           simpleframework
Version:        6.0.1
Release:        0
Summary:        Simple Framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/ngallagher/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh-external)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
The goal of Simple is to bring simplicity, scalability, and performance to
server side Java. The primary focus of the project is to provide a truly
embeddable Java based HTTP and WebSocket engine capable of handling enormous
loads. Simple provides a truly asynchronous service model, request completion
is driven using an internal, transparent, monitoring system. This allows Simple
to vastly outperform most popular Java based servers in a multi-tier
environment, as it requires only a very limited number of threads to handle
very high quantities of concurrent clients. Simple has consistently out
performed both commercial and open source Java Servlet engines and WebSocket
platforms and has a fully comprehensive API that is as usable for experienced
Java developers as it is for beginners. Best of all, Simple is completely free,
and is released under the terms of the Apache License, which ensures its
availability for use by open source and proprietary developers alike.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} .
sed -i -e 's/\r//g' README.md

%pom_remove_plugin -r :maven-source-plugin simple
%pom_remove_plugin -r :maven-compiler-plugin simple
%pom_remove_plugin -r :maven-javadoc-plugin simple

%build
pushd simple
%{mvn_build} -f -- -Dsource=8
popd

%install
pushd simple
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}
popd

%files -f simple/.mfiles
%license LICENSE-2.0.txt
%doc README.md

%files javadoc -f simple/.mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
