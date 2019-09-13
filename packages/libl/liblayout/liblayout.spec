#
# spec file for package liblayout
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


Name:           liblayout
Version:        0.2.10
Release:        0
Summary:        CSS based layouting framework
License:        LGPL-2.1+ and Unicode
Group:          Development/Libraries/Java
Url:            http://reporting.pentaho.org/
Source:         http://downloads.sourceforge.net/jfreereport/liblayout-%{version}.zip
Source99:       %{name}-rpmlintrc
BuildRequires:  ant
BuildRequires:  flute
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  libbase >= 1.1.3
BuildRequires:  libfonts
BuildRequires:  libloader
BuildRequires:  librepository
BuildRequires:  pentaho-libxml
BuildRequires:  sac
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
Requires:       flute
Requires:       java
Requires:       jpackage-utils
Requires:       libbase >= 1.0.0
Requires:       libfonts >= 1.1.3
Requires:       libloader >= 1.1.3
Requires:       librepository >= 1.1.3
Requires:       pentaho-libxml
Requires:       sac
Requires:       xml-commons-apis
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
LibLayout is a layouting framework. It is based on the Cascading StyleSheets
standard. The layouting expects to receive its content as a DOM structure
(although it does not rely on the W3C-DOM API).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib flute libloader librepository libxml libfonts \
    sac jaxp libbase commons-logging-api

%build
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 -Dant.build.javadoc.source=1.6 \
    jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install

mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
