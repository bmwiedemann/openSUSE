#
# spec file for package treelayout
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


%global core org.abego.treelayout
Name:           treelayout
Version:        1.0.3
Release:        0
Summary:        Efficient and customizable Tree Layout Algorithm in Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://treelayout.sourceforge.net/
Source0:        https://github.com/abego/treelayout/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Efficiently create compact, highly customizable
tree layouts. The software builds tree layouts
in linear time. I.e. even trees with many nodes
are built fast.

%package demo
Summary:        TreeLayout Core Demo

%description demo
Demo for "org.abego.treelayout.core".

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# This is a dummy POM added just to ease building in the RPM platforms:
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.abego.treelayout</groupId>
  <artifactId>org.abego.treelayout.project</artifactId>
  <packaging>pom</packaging>
  <version>%{version}</version>

  <modules>
    <module>org.abego.treelayout</module>
    <module>org.abego.treelayout.demo</module>
    <!-- Use org.netbeans.api:org-netbeans-api-visual:RELEASE67: -->
    <!--module>org.abego.treelayout.netbeans</module-->
    <!--module>org.abego.treelayout.netbeans.demo</module-->
  </modules>

</project>
EOF

# fix non ASCII chars
iconv -f UTF-8 -t ASCII//TRANSLIT -o %{core}/src/main/java/org/abego/treelayout/package-info.java.tmp \
 %{core}/src/main/java/org/abego/treelayout/package-info.java
mv %{core}/src/main/java/org/abego/treelayout/package-info.java.tmp \
 %{core}/src/main/java/org/abego/treelayout/package-info.java

%{mvn_package} :%{core}.project __noinstall

%build

%{mvn_build} -sf

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{core}.core
%doc %{core}/CHANGES.txt README.md
%license %{core}/src/LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%license %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%license %{core}/src/LICENSE.TXT

%changelog
