#
# spec file for package jsch
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jsch
Version:        0.1.54
Release:        0
Summary:        Pure Java implementation of SSH2
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            http://www.jcraft.com/jsch/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip
Source1:        MANIFEST.MF
Source2:        plugin.properties
Source3:        http://repo1.maven.org/maven2/com/jcraft/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         jsch-0.1.54-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  jzlib
BuildRequires:  unzip
BuildRequires:  zip
Requires:       jzlib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%package        javadoc
Summary:        Pure Java implementation of SSH2
Group:          Development/Libraries/Java

%description    javadoc
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%package        demo
Summary:        Pure Java implementation of SSH2
Group:          Development/Libraries/Java

%description    demo
JSch allows you to connect to an sshd server and use port forwarding,
X11 forwarding, file transfer, etc., and you can integrate its
functionality into your own Java programs.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE3} pom.xml
%pom_remove_parent 

%build
export CLASSPATH=$(build-classpath jzlib)
ant dist javadoc

%install
# inject the OSGi Manifest
mkdir META-INF
cp %{SOURCE1} META-INF
cp %{SOURCE2} plugin.properties
zip dist/lib/%{name}-*.jar META-INF/MANIFEST.MF
zip dist/lib/%{name}-*.jar plugin.properties

# jars
install -Dpm 644 dist/lib/%{name}-*.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr examples/* %{buildroot}%{_datadir}/%{name}

# POM and depmap
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%changelog
