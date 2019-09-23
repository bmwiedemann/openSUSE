#
# spec file for package ini4j
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ini4j
Version:        0.5.1
Release:        0
Summary:        Java API for handling Windows ini file format
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://www.ini4j.org/
# wget http://switch.dl.sourceforge.net/sourceforge/ini4j/%{name}-%{version}-all.zip
# unzip -q *zip
# cd ini4j-0.5.1/
# fastjar -cf ini4j-0.5.1-sources
# mkdir src; mv META-INF org src/
# tar -cjf ../ini4j-0.5.1-sources.tar.bz2 src/ LICENSE.txt NOTICE.txt
Source0:        %{name}-%{version}-sources.tar.bz2
Source1:        %{name}-%{version}.build.xml
Source2:        %{name}-%{version}.buildinfo.properties
Patch0:         ini4j-java8-compat.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  unzip
Requires:       java
BuildArch:      noarch

%description
The [ini4j] is a simple Java API for handling configuration files in
Windows .ini format. Additionally, the library includes Java
Preferences API implementation based on the .ini file.

%package javadoc
Summary:        Java API for handling Windows ini file format
Group:          Development/Libraries/Java
Requires(post): /bin/ln
Requires(post): /bin/rm
Requires(postun): /bin/rm

%description javadoc
The [ini4j] is a simple Java API for handling configuration files in
Windows .ini format. Additionally, the library includes Java
Preferences API implementation based on the .ini file.

%prep
%setup -q -c
# remove existing binaries
find . -type f \( -iname "*.jar" -o -iname "*.class" -o -iname "*.exe" -o -iname "*.so" \) | \
  xargs -t rm -f

cp %{SOURCE1} build.xml
mkdir -p src/etc
cp %{SOURCE2} src%{_sysconfdir}/buildinfo.properties

%patch0 -p1

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 build
ant javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}-%{version}

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%{_javadocdir}/%{name}

%changelog
