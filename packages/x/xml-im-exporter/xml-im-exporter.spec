#
# spec file for package xml-im-exporter
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


Name:           xml-im-exporter
Version:        1.1
Release:        0
Summary:        XML Im-/Exporter
License:        LGPL-2.0+
Group:          Development/Libraries/Java
Url:            http://xml-im-exporter.sourceforge.net/
Source0:        xml-im-exporter1.1.tar.bz2
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/de/zeigermann/xml/xml-im-exporter/1.1/xml-im-exporter-1.1.pom
Patch0:         xml-im-exporter-build_xml.patch
Patch1:         encoding.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
# Needed for maven conversions
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildArch:      noarch

%description
XML Im-/Exporter is a low level library to assist you in the straight
forward process of importing and exporting XML from and to your Java
classes. All of this is designed having performance and simplicity in
mind.

%package javadoc
Summary:        XML Im-/Exporter
Group:          Development/Libraries/Java

%description javadoc
XML Im-/Exporter is a low level library to assist you in the straight
forward process of importing and exporting XML from and to your Java
classes. All of this is designed having performance and simplicity in
mind.

%prep
%setup -q -n %{name}
# remove all binary libs
find . -name "*.jar" | xargs rm
#for j in $(find . -name "*.jar"); do
#    mv $j $j.no
#done
# wrong end of line encoding
sed -i -e 's/.$//' *.txt doc/javadoc/stylesheet.css doc/javadoc/package-list
%patch0 -b .sav
%patch1 -p1

%build
export CLASSPATH=
export OPT_JAT_LIST="junit ant/ant-junit"
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 -Djavac.encoding="utf-8" jar test javadocs

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/%{name}%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# maven
install -d -m 755 %{buildroot}%{_mavenpomdir}/
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
rm -f TEST-*.txt # has test durations that differ across builds

%files
%defattr(0644,root,root,0755)
%doc doc/index.html *.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
