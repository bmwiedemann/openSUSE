#
# spec file for package jameica
#
# Copyright (c) 2020 SUSE LLC
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


%define _build 455
%define _buildreleases 455
%define _tag V_2_8_6_BUILD_%{_build}
Name:           jameica
Version:        2.8.6
Release:        0
Summary:        Runtime environment for Java applications like Hibiscus
License:        GPL-2.0-only AND LGPL-2.0-only AND Apache-2.0 AND CPL-1.0 AND Zlib AND MPL-1.0 AND EPL-1.0
Group:          Productivity/Office/Finance
URL:            http://www.willuhn.de/products/jameica/
Source:         https://github.com/willuhn/jameica/archive/%{_tag}.tar.gz
BuildRequires:  ant
BuildRequires:  dos2unix
#BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.6
BuildRequires:  jpackage-utils
BuildRequires:  nanoxml = 2.2.3
BuildRequires:  paperclips = 1.0.4
BuildRequires:  swtcalendar
BuildRequires:  velocity = 1.7
BuildRequires:  xml-apis
#Requires:       eclipse-swt
Requires:       nanoxml = 2.2.3
Requires:       paperclips = 1.0.4
Requires:       swtcalendar
Requires:       velocity = 1.7

%ifarch %{ix86} ppc s390
%global bits 32
%endif
%ifarch x86_64 ia64 s390x aarch64 armv7l arm64
%global bits 64
%endif
%if 0%{?__isa_bits}
%global bits %{__isa_bits}
%endif

%description
Serves as a base framework for recurring tasks on Hibiscus.
Keeps a unified look & feel. Strictly separate program and
user data. Supports synchronous and asynchronous data exchange
via between plugins (via messaging) and allows client server
communication via RMI, XML-RPC and SOAP. Comes with headless
mode (no GUI for servers) and logging.

%package devel
Summary:        SDK for the Jameica framework
Group:          Development/Languages/Java
Requires:       jameica

%description devel
Source code required to build and develop Jameica plugins.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Developer documentation for Jameica.

%prep
%setup -q -n %{name}-%{_tag}
# rpmlint
find . -type f -name '*.txt' -exec chmod -x {} \;
find . -type f -name '*.html' -exec chmod -x {} \;
find . -type f -name '*.properties' -exec chmod -x {} \;

rm build/jameica-win32.exe
rm build/jameica-win64.exe
rm build/launch4j-win32.xml
rm build/launch4j-win64.xml
rm build/jameica-macos64.sh
rm build/jameica-openbsd.sh

rm -rf lib/swt/macos64
rm -rf lib/swt/win32
rm -rf lib/swt/win64
# remove arm because of missing ld-linux-aarch64.so.1 package in suse
rm -rf lib/swt/linux-arm64

# unbundle NanoXML
rm -rf lib/nanoxml/*
ln -sf %{_javadir}/nanoxml-2.2.3.jar lib/nanoxml/nanoxml-2.2.3.jar

# unbundle PaperClips
rm -rf lib/paperclips/*
ln -sf %{_javadir}/net.sf.paperclips_1.0.4.jar lib/paperclips/net.sf.paperclips_1.0.4.jar

# unbundle SWT Calender
rm -rf lib/swtcalendar/*
ln -sf %{_javadir}/swtcalendar.jar lib/swtcalendar/swtcalendar.jar

# unbundle Velocity
rm -rf lib/velocity/*
ln -sf %{_javadir}/velocity.jar lib/velocity/velocity-1.7.jar

# unbundle eclipse-swt
##rm -fr lib/swt/linux*/swt.jar
##%%if %{bits} > 32
##mkdir -p lib/swt/linux64
##ln -sf $(find-jar swt) lib/swt/linux64/
##%%else
##mkdir -p lib/swt/linux
##ln -sf $(find-jar swt) lib/swt/linux/
##%%endif

%build
export CLASSPATH="$(build-classpath xml-apis)"
ant -f build/build.xml init compile jar zip src javadoc

%install
mkdir -p %{buildroot}%{_prefix}/lib/jameica/plugins
cp -r releases/%{version}-%{_buildreleases}/%{name} %{buildroot}%{_prefix}/lib
chmod +x %{buildroot}%{_prefix}/lib/%{name}/rcjameica
chmod +x %{buildroot}%{_prefix}/lib/%{name}/jameicaserver.sh
chmod +x %{buildroot}%{_prefix}/lib/%{name}/jameica.sh

rm %{buildroot}%{_prefix}/lib/%{name}/jameica-win32.jar
rm %{buildroot}%{_prefix}/lib/%{name}/jameica-win64.jar
rm %{buildroot}%{_prefix}/lib/%{name}/jameica-macos64.jar
rm %{buildroot}%{_prefix}/lib/%{name}/jameica-openbsd.jar

%if %{bits} > 32
rm %{buildroot}%{_prefix}/lib/%{name}/jameica-linux.jar
  %ifarch aarch64 armv7l arm64
  rm %{buildroot}%{_prefix}/lib/%{name}/jameica-linux64.jar
  %else
  rm %{buildroot}%{_prefix}/lib/%{name}/jameica-linuxarm64.jar
  %endif
%else
rm %{buildroot}%{_prefix}/lib/%{name}/jameica-linux64.jar
%endif

# Mac OS X stuff
rm %{buildroot}%{_prefix}/lib/%{name}/*.plist
rm %{buildroot}%{_prefix}/lib/%{name}/*.icns

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_prefix}/lib/%{name}/jameica.sh %{buildroot}%{_bindir}/jameica
ln -sf %{_prefix}/lib/%{name}/jameicaserver.sh %{buildroot}%{_bindir}/jameicaserver

cp -r src %{buildroot}%{_prefix}/lib/jameica

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r releases/%{version}-%{_buildreleases}/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%fdupes %{buildroot}%{_prefix}/lib/%{name}

%files
%doc build/ChangeLog README.md
%license LICENSE COPYING
%{_bindir}/*
%{_prefix}/lib/jameica
%{_prefix}/lib/jameica/lib
%dir %{_prefix}/lib/jameica/plugins
%exclude %{_prefix}/lib/jameica/src

%files devel
%{_prefix}/lib/jameica/src

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
