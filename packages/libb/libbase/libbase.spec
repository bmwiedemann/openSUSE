#
# spec file for package libbase
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


Name:           libbase
Version:        1.1.3
Release:        0
Summary:        JFree Base Services
License:        LGPL-2.0
Group:          Development/Libraries/Java
Url:            http://reporting.pentaho.org/
#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source:         %{name}-%{version}-jarsdeleted.zip
Source99:       libbase-rpmlintrc
#PATCH-FIX-UPSTREAM, fix some properties for build
Patch0:         libbase-1.1.2.build.patch
Patch1:         libbase-1.1.3-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-contrib >= 1.0b3
BuildRequires:  apache-commons-logging
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  unzip
Requires:       apache-commons-logging
Requires:       java
Requires:       jpackage-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(-,root,root)
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}

%changelog
