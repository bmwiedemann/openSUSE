#
# spec file for package jgraphx
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


Name:           jgraphx
Version:        4.2.2
Release:        0
Summary:        Java-based Diagram Component and Editor
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jgraph
Source0:        https://github.com/jgraph/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       java >= 1.8
BuildArch:      noarch

%description
Jgraphx is the a lightweight and feature-rich graph component for Java,
and the successor to jgraph. It provides automatic 2D layout and routing
for diagrams. Object and relations can be displayed in any Swing UI
via provided zoomable component.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q

# fix executable permissions
chmod 644 docs/manual/images/mx_man_graph_analysis.jpg

# remove all binary libs
find -type f -name "*.jar" | xargs -t rm

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

# Remove copies of source so that we don't confuse
# the debuginfo finder
rm -rf build/src dist/%{name}-%{version}-src

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 lib/jgraphx.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt

%files javadoc
%license license.txt
%{_javadocdir}/%{name}

%changelog
