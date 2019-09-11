#
# spec file for package pentaho-libxml
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


%define origname libxml
Name:           pentaho-libxml
Version:        1.1.3
Release:        0
Summary:        Namespace aware SAX parser utility library
License:        LGPL-2.0
Group:          Development/Libraries/Java
Url:            http://reporting.pentaho.org/
#Original source: http://downloads.sourceforge.net/jfreereport/%%{origname}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source:         %{origname}-%{version}-jarsdeleted.zip
#PATCH-FIX-UPSTREAM, fix some properties for build
Patch0:         libxml-1.1.2-build.patch
Patch1:         pentaho-libxml-1.1.3-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase
BuildRequires:  libloader
BuildRequires:  unzip
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.1.2
Requires:       libloader >= 1.1.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Pentaho LibXML is a namespace aware SAX parser utility library. It
facilitates implementing non-trivial SAX input handlers.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1
find . -name "*.jar" -delete
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase libloader
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{origname}-%{version}.jar %{buildroot}%{_javadir}/%{origname}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{origname}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{origname}

%files
%defattr(-,root,root)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{origname}.jar

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{origname}

%changelog
