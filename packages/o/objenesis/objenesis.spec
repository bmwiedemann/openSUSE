#
# spec file for package objenesis
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2000-2009, JPackage Project
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


%global major 3
%global minor 6
%global micro 0
%global fullversion %{major}.%{minor}.%{micro}
%global specversion %{major}.%{minor}
Name:           objenesis
%if %{micro}
Version:        %{fullversion}
Release:        0
%else
Version:        %{specversion}
Release:        0
%endif
Summary:        A library for instantiating Java objects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://objenesis.org/
Source0:        https://github.com/easymock/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}-build.tar.xz
BuildRequires:  fdupes ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Objenesis is a small Java library that serves one purpose: to instantiate
a new object of a particular class.
Java supports dynamic instantiation of classes using Class.newInstance();
however, this only works if the class has an appropriate constructor. There
are many times when a class cannot be instantiated this way, such as when
the class contains constructors that require arguments, that have side effects,
and/or that throw exceptions. As a result, it is common to see restrictions
in libraries stating that classes must require a default constructor.
Objenesis aims to overcome these restrictions by bypassing the constructor
on object instantiation. Needing to instantiate an object without calling
the constructor is a fairly specialized task, however there are certain cases
when this is useful:
* Serialization, Remoting and Persistence - Objects need to be instantiated
  and restored to a specific state, without invoking code.
* Proxies, AOP Libraries and Mock Objects - Classes can be sub-classed without
  needing to worry about the super() constructor.
* Container Frameworks - Objects can be dynamically instantiated in
  non-standard ways.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -a1

%build
ant package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 main/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 0644 exotic/target/%{name}-exotic-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-exotic.jar
install -pm 0644 tck/target/%{name}-tck-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-tck.jar

# poms
install -dm 755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} main/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%{mvn_install_pom} exotic/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-exotic.pom
%{mvn_install_pom} tck/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-tck.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
%add_maven_depmap %{name}/%{name}-exotic.pom %{name}/%{name}-exotic.jar
%add_maven_depmap %{name}/%{name}-tck.pom %{name}/%{name}-tck.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -aL main/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}
cp -aL exotic/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-exotic
cp -aL tck/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-tck
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
