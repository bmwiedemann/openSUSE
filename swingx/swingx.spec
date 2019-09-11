#
# spec file for package swingx
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


Name:           swingx
Version:        0.9.4
Release:        0
Summary:        A collection of Swing components
License:        LGPL-2.0-only
Group:          Development/Libraries/Java
Url:            https://swingx.dev.java.net/
Source0:        https://swingx.dev.java.net/files/documents/2981/110622/%{name}-%{version}-src.tar.bz2
# Remove external dependency that's now included in JDK 1.6
# See http://forums.java.net/jive/thread.jspa?messageID=318384
Patch0:         swingx-0.9.4-LoginService.patch
# Remove build dependencies on included binary jars and add system jars
# Remove main class from manifest
Patch1:         swingx-0.9.4-project-properties.patch
# Don't do the "demo taglet" stuff
Patch2:         swingx-0.9.4-swinglabs-build-impl.patch
# Resolve the ambiguity of toArray in jdk11
Patch3:         swingx-0.9.4-toArray.patch
BuildRequires:  ant
BuildRequires:  batik
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
Requires:       java >= 1.6.0
BuildArch:      noarch

%description
SwingX contains a collection of powerful, useful, and just plain fun Swing
components. Each of the Swing components have been extended, providing
data-aware functionality out of the box. New useful components have been
created like the JXDatePicker, JXTaskPane, and JXImagePanel.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Documentation for the SwingX widgets

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
rm -rf lib/

%build
ant -Djavac.source=1.6 -Djavac.target=1.6 jar javadoc

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}/%{_mavenpomdir}/
install -m 0644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/
cp -r dist/javadoc %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc COPYING README
%{_javadir}/*.jar
%{_mavenpomdir}/*
%config(noreplace) %{_datadir}/maven-metadata/%{name}.xml

%files javadoc
%{_javadocdir}/%{name}

%changelog
