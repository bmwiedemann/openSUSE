#
# spec file for package xpp2
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


%define originalname PullParser
Name:           xpp2
Version:        2.1.10
Release:        0
Summary:        XML Pull Parser
License:        Apache-1.1
Group:          Development/Libraries/Java
Url:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/
Source0:        http://www.extreme.indiana.edu/xgws/xsoap/xpp/download/PullParser2/PullParser2.1.10.tar.bz2
Patch0:         xpp2-build_xml.patch
Patch1:         xpp2-enum.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit >= 1.6
BuildRequires:  fdupes
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       xml-commons-apis
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode. All
active development concentrates on its successor XPP3/MXP1

%package javadoc
Summary:        XML Pull Parser
Group:          Development/Libraries/Java

%description javadoc
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode. All
active development concentrates on its successor XPP3/MXP1

%package manual
Summary:        XML Pull Parser
Group:          Development/Libraries/Java

%description manual
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode. All
active development concentrates on its successor XPP3/MXP1

%package demo
Summary:        XML Pull Parser
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description demo
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode. All
active development concentrates on its successor XPP3/MXP1

%prep
%setup -q -n %{originalname}%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav
%patch1 -p1

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath xml-commons-apis xerces-j2)
ant all api api.impl
CLASSPATH=$CLASSPATH:$(build-classpath junit):build/tests:build/lib/PullParser-2.1.10.jar
java AllTests

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{originalname}-intf-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-intf-%{version}.jar
cp -p build/lib/%{originalname}-standard-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-standard-%{version}.jar
cp -p build/lib/%{originalname}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp -p build/lib/%{originalname}-x2-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-x2-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}/api
mkdir -p %{buildroot}%{_javadocdir}/%{name}/api_impl
cp -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}/api
cp -pr doc/api_impl/* %{buildroot}%{_javadocdir}/%{name}/api_impl
rm -rf doc/{build.txt,api,api_impl}
# manual
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr doc/* %{buildroot}%{_datadir}/doc/%{name}
cp -p README.html %{buildroot}%{_datadir}/doc/%{name}
cp -p LICENSE.txt %{buildroot}%{_datadir}/doc/%{name}
# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src/java/samples/* %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%{_datadir}/doc/%{name}/README.html
%{_datadir}/doc/%{name}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-intf.jar
%{_javadir}/%{name}-intf-%{version}.jar
%{_javadir}/%{name}-standard.jar
%{_javadir}/%{name}-standard-%{version}.jar
%{_javadir}/%{name}-x2.jar
%{_javadir}/%{name}-x2-%{version}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_datadir}/doc/%{name}
%exclude %{_datadir}/doc/%{name}/README.html
%exclude %{_datadir}/doc/%{name}/LICENSE.txt

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%changelog
