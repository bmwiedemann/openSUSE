#
# spec file for package libformula
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


Name:           libformula
Version:        1.1.6
Release:        0
Summary:        Formula Parser
License:        LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            http://reporting.pentaho.org/
Source:         http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Source99:       %{name}-rpmlintrc
#PATCH-FIX-UPSTREAM, fix some properties for build
Patch0:         libformula-1.1.6.build.patch
Patch1:         libformula-1.1.6-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  apache-commons-logging
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  libbase >= 1.1.6
BuildRequires:  unzip
Requires:       apache-commons-logging
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.1.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
LibFormula provides Excel-Style-Expressions. The implementation provided
here is very generic and can be used in any application that needs to
compute formulas.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase
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
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}.jar

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}

%changelog
