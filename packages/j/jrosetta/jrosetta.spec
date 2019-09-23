#
# spec file for package jrosetta
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           jrosetta
Version:        1.0.4
Release:        0
Summary:        API and graphical components for console
License:        GPL-2.0
Group:          Development/Libraries/Java
Url:            http://dev.artenum.com/projects/JRosetta
Source0:        http://maven.artenum.com/content/groups/public/com/artenum/jrosetta/%{version}/jrosetta-%{version}-sources.jar
Source1:        jrosetta-build-ant-1.0.4.tar.gz
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel >= 1.6
BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  junit
BuildRequires:  unzip
Requires:       java >= 1.6
Requires:       jpackage-utils >= 1.5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
JRosetta provides a common base for graphical component that could be used
to build a graphical console in Swing with the latest requirements, such as
command history, completion and so on for instance for scripting language
or command line.

%prep
%setup -q -c -n %{name}-%{version}-sources -a1
cp -r %{name}-%{version}/modules/* .
rm -r %{name}-%{version}/
rm -r META-INF
rm %{name}-*/pom.xml

%build
cd jrosetta-api
ant \
    -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    build-jar

cd ../jrosetta-engine
ant \
    -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
    -Djava.encoding=UTF-8 \
    build-jar

%install
mkdir -p %{buildroot}%{_javadir}
cp -p %{name}-api/build/%{name}-API-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}-API-%{version}.jar
ln -s %{name}-API-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}-API.jar
cp -p %{name}-engine/build/%{name}-engine-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}-engine-%{version}.jar
ln -s %{name}-engine-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}-engine.jar

%files
%defattr(-,root,root)
%{_javadir}/jrosetta*.jar

%changelog
