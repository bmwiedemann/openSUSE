#
# spec file for package librepository
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


Name:           librepository
Version:        1.1.3
Release:        0
Summary:        Hierarchical repository abstraction layer
License:        LGPL-2.0
Group:          Development/Libraries/Java
Url:            http://reporting.pentaho.org/
#Original source: http://downloads.sourceforge.net/jfreereport/%%name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source:         %{name}-%{version}-jarsdeleted.zip
Source99:       %{name}-rpmlintrc
#PATCH-FIX-UPSTREAM, fix some properties for build
Patch0:         librepository-1.1.2.build.patch
Patch1:         librepository-1.1.3-sourcetarget.patch
Patch2:         librepository-1.1.3-javadoc.patch
BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase >= 1.1.3
BuildRequires:  unzip
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.1.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
LibRepository provides a simple abstraction layer to access bulk content that
is organized in a hierarchical layer.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1
%patch2 -p1
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase
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
