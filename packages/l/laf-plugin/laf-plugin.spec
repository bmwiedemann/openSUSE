#
# spec file for package laf-plugin
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


Name:           laf-plugin
Version:        1.0
Release:        0
Summary:        Generic plugin framework for Java look-and-feels
# nanoxml distributed with laf-plugin is licensed under Zlib license while laf-plugin itself is BSD-3-Clause
License:        BSD-3-Clause AND Zlib
Group:          Development/Libraries/Java
URL:            https://java.net/projects/laf-plugin
# Upstream download URL https://laf-plugin.dev.java.net/files/documents/4261/50297/%{name}-all.zip seems dead
Source0:        %{name}-all.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  unzip
BuildRequires:  xmlbeans
Requires:       java >= 1.8
Requires:       jpackage-utils
BuildArch:      noarch

%description
The goal of this project is to provide a small infrastructure that
provides plugin mechanism for third-party components in look-and-feel
libraries.

%package javadoc
Summary:        Javadoc for laf-plugin
Group:          Documentation/HTML
Recommends:     %{name} = %{version}

%description javadoc
The goal of this project is to provide a small infrastructure that
provides plugin mechanism for third-party components in look-and-feel
libraries.

This package provides the Java (HTML) Documentation for %{name}.

%prep
%setup -q -c -n %{name}
cp %{SOURCE1} build.xml
rm -rf drop/*
dos2unix     src/org/jvnet/lafplugin/*.license
chmod 644 src/org/jvnet/lafplugin/*.license

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 all

javadoc -quiet \
    -d doc \
    -source 1.8 \
    -classpath ./build/classes50 \
    -public \
    `find ./ -name \*.java`

%install
# jars
install -Dm 644 drop/%{name}-50.jar %{buildroot}%{_javadir}/%{name}-50.jar
ln -sf %{name}-50.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%license src/org/jvnet/lafplugin/*.license
%{_javadir}/%{name}*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
