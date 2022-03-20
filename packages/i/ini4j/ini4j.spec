#
# spec file for package ini4j
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


Name:           ini4j
Version:        0.5.1
Release:        0
Summary:        Java API for handling Windows ini file format
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.ini4j.org/
# wget http://switch.dl.sourceforge.net/sourceforge/ini4j/%{name}-%{version}-all.zip
# unzip -q *zip
# cd ini4j-0.5.1/
# fastjar -cf ini4j-0.5.1-sources
# mkdir src; mv META-INF org src/
# tar -cjf ../ini4j-0.5.1-sources.tar.bz2 src/ LICENSE.txt NOTICE.txt
Source0:        %{name}-%{version}-sources.tar.bz2
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        %{name}-%{version}.build.xml
Source3:        %{name}-%{version}.buildinfo.properties
Patch0:         ini4j-java8-compat.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
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
Requires(postun):/bin/rm

%description javadoc
The [ini4j] is a simple Java API for handling configuration files in
Windows .ini format. Additionally, the library includes Java
Preferences API implementation based on the .ini file.

%prep
%setup -q -c
# remove existing binaries
find . -type f \( -iname "*.jar" -o -iname "*.class" -o -iname "*.exe" -o -iname "*.so" \) | \
  xargs -t rm -f

cp %{SOURCE2} build.xml
mkdir -p src%{_sysconfdir}
cp %{SOURCE3} src%{_sysconfdir}/buildinfo.properties

%patch0 -p1

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 build
ant javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
