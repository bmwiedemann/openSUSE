#
# spec file for package libserializer
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


Name:           libserializer
Version:        1.1.6
Release:        0
Summary:        JFreeReport General Serialization Framework
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            http://reporting.pentaho.org
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Source99:       %{name}-rpmlintrc
Patch0:         libserializer-1.1.6.build.patch
Patch1:         libserializer-1.1.6-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  libbase >= 1.1.6
BuildRequires:  unzip
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.1.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom java serialization handlers.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch -P 0 -p1 -b .build
%patch -P 1 -p1
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/libserializer-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

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
