#
# spec file for package xom
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


Name:           xom
Version:        1.3.9
Release:        0
Summary:        XML Object Model
License:        LGPL-2.0-only
URL:            https://github.com/elharo/xom
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-build.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jaxen-bootstrap
BuildRequires:  junit
BuildRequires:  xerces-j2
BuildRequires:  xml-apis
BuildArch:      noarch

%description
XOM is a new XML object model. It is an open source (LGPL),
tree-based API for processing XML with Java that strives
for correctness, simplicity, and performance, in that order.
XOM is designed to be easy to learn and easy to use. It
works very straight-forwardly, and has a very shallow
learning curve. Assuming you're already familiar with XML,
you should be able to get up and running with XOM very quickly.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%package demo
Summary:        Samples for %{name}
Requires:       %{name} = %{version}-%{release}

%description demo
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1

%build
mkdir -p lib
pushd lib
ln -sf $(build-classpath junit) junit.jar
ln -sf $(build-classpath xerces-j2) xercesImpl-2.12.2.jar
ln -sf $(build-classpath xml-apis) xml-apis-1.4.01.jar
ln -sf $(build-classpath jaxen) jaxen-1.1.6.jar
popd

%{ant} jar samples javadoc maven

mv build/maven2/project.xml build/maven2/pom.xml
%pom_add_dep jaxen:jaxen build/maven2/pom.xml

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} build/maven2/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a com.io7m.xom:xom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 build/xom-samples.jar %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%doc README.txt Todo.txt lgpl.txt
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt
%doc lgpl.txt

%files demo
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xom-samples.jar

%changelog
