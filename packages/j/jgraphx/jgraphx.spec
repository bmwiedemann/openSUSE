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
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
Requires:       java >= 1.8
Requires:       jpackage-utils
BuildArch:      noarch

%description
Jgraphx is the a lightweight and feature-rich graph component for Java,
and the successor to jgraph. It provides automatic 2D layout and routing
for diagrams. Object and relations can be displayed in any Swing UI
via provided zoomable component.

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

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p lib/jgraphx.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd  %{buildroot}%{_javadir}
    #create symlink
    ln -s %{name}-%{version}.jar %{name}.jar
popd

%files
%license license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%changelog
