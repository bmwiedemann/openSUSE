#
# spec file for package xmlgraphics-commons
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2000-2008, JPackage Project
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


Name:           xmlgraphics-commons
Version:        2.8
Release:        0
Summary:        XML Graphics Commons
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://xmlgraphics.apache.org/commons/
Source0:        https://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz
Patch0:         xmlgraphics-commons-build_xml.patch
Patch1:         xmlgraphics-commons-jdk10.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  commons-io >= 1.1
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       mvn(commons-io:commons-io) >= 1.1
Requires:       mvn(commons-logging:commons-logging)
BuildArch:      noarch

%description
Apache XML Graphics Commons is a library that consists of
several reusable components used by Apache Batik and
Apache FOP. Many of these components can easily be used
separately outside the domains of SVG and XSL-FO. You will
find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for package %{name}.

%prep
%setup -q %{name}-%{version}
%patch0
%patch1 -p1
find . -name "*.jar" | xargs rm

%build
export CLASSPATH=
build-jar-repository -s lib commons-io commons-logging
ant -Djavac.source=1.8 -Djavac.target=1.8 package javadocs

%install
# jar
install -Dpm 644 build/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%doc README

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
