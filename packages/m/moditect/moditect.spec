#
# spec file for package moditect
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


Name:           moditect
Version:        1.1.0
Release:        0
Summary:        Tooling for the Java Module System
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildArch:      noarch

%description
The ModiTect project aims at providing productivity tools for working with the
Java module system ("Jigsaw").

Currently the following tasks are supported:
• Generating module-info.java descriptors for given artifacts (Maven
  dependencies or local JAR files)
• Adding module descriptors to your project's JAR as well as existing JAR files
  (dependencies)
• Creating module runtime images

Compared to authoring module descriptors by hand, using ModiTect saves you work
by defining dependence clauses based on your project's dependencies, describing
exported and opened packages with patterns (instead of listing all packages
separately), auto-detecting service usages and more. You also can use ModiTect
to add a module descriptor to your project JAR while staying on Java 8 with
your own build.

In future versions functionality may be added to work with other tools like
jmod etc. under Maven and other dependency management tools in a comfortable
manner.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_parent parent
%pom_xpath_inject pom:project '<groupId>org.moditect</groupId>' parent

%pom_remove_plugin com.mycila:license-maven-plugin parent

%pom_disable_module integrationtest

%build
%{mvn_build} -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
