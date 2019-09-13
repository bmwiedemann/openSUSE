#
# spec file for package spec-version-maven-plugin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spec-version-maven-plugin
Version:        1.2
Release:        0
Summary:        Spec Version Maven Plugin
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            http://glassfish.java.net/
Source0:        https://github.com/javaee/spec-version-maven-plugin/archive/%{version}.tar.gz
Source1:        https://github.com/javaee/spec-version-maven-plugin/raw/master/LICENSE
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildArch:      noarch

%description
Maven Plugin to configure APIs version and
specs in a MANIFEST.MF file.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

cp -p %{SOURCE1} LICENSE.txt
dos2unix LICENSE.txt

%{mvn_file} :%{name} %{name}

%build

%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
