#
# spec file for package libloader
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


Name:           libloader
Version:        1.1.6
Release:        0
Summary:        Resource Loading Framework
License:        LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            http://reporting.pentaho.org/
Source:         http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Source99:       %{name}-rpmlintrc
#PATCH-FIX-UPSTREAM, fix some properties for build
Patch0:         libloader-1.1.6.build.patch
Patch1:         libloader-1.1.6-sourcetarget.patch
Patch2:         libloader-1.1.6-javadoc.patch
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
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way, totally
transparent to the user of that library.

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
build-jar-repository -s -p lib libbase commons-logging-api
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
