#
# spec file for package jdom
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


Name:           jdom
Version:        1.1.3
Release:        0
Summary:        Java alternative to DOM and SAX
License:        Saxpath
URL:            http://www.jdom.org/
Source0:        http://jdom.org/dist/binary/archive/jdom-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/jdom/jdom/%{version}/jdom-%{version}.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-1.1-OSGiManifest.patch
Patch2:         no-jaxen.patch
Patch10:        CVE-2021-33813.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is a
lightweight and fast, and is optimized for the Java programmer. It's an
alternative to DOM and SAX, although it integrates well with both DOM
and SAX.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Requires:       %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}
%patch0
%patch1
%patch2 -p1
%patch10 -p1
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%build
%{ant} -Dcompile.source=1.8 -Dcompile.target=1.8 -Dj2se.apidoc=%{_javadocdir}/java package javadoc-link

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/%{name}-*-snap.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a jdom:jdom,org.jdom:jdom-legacy

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r build/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# demo
install -dm 0755 %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc CHANGES.txt COMMITTERS.txt README.txt TODO.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%files demo
%{_datadir}/%{name}
%license LICENSE.txt

%changelog
