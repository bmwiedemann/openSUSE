#
# spec file for package jetty-toolchain
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


Name:           jetty-toolchain
Version:        1.7
Release:        0
Summary:        Jetty Toolchain main POM file
License:        Apache-2.0 OR EPL-1.0
Group:          Development/Libraries/Java
URL:            https://github.com/eclipse/jetty.toolchain
Source0:        https://repo.maven.apache.org/maven2/org/eclipse/jetty/toolchain/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        http://www.eclipse.org/org/documents/epl-v10.html
BuildRequires:  maven-local
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildArch:      noarch

%description
Jetty Toolchain main POM file

%prep
%setup -q -c -T
cp %{SOURCE0} pom.xml
cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin :maven-release-plugin

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt
%license epl-v10.html

%changelog
