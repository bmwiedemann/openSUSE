#
# spec file for package apache-pdfbox
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Only fontbox and jempbox are built as pdfbox itself depends on Adobe's pcif.
Name:           apache-pdfbox
Version:        1.8.16
Release:        0
Summary:        Java PDF Library
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            https://pdfbox.apache.org/
Source0:        http://www-us.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip
Source1:        http://central.maven.org/maven2/org/apache/pdfbox/pdfbox/%{version}/pdfbox-%{version}.pom
Source2:        http://central.maven.org/maven2/org/apache/pdfbox/fontbox/%{version}/fontbox-%{version}.pom
Source3:        http://central.maven.org/maven2/org/apache/pdfbox/jempbox/%{version}/jempbox-%{version}.pom
Patch0:         pdfbox-1.8.12-bouncycastle.patch
Patch1:         disable-downloads.patch
Patch2:         fix-javadoc-dep.patch
Patch3:         pdfbox-1.8.12-sourcetarget.patch
Patch4:         fix-version.patch
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  bouncycastle
BuildRequires:  fdupes
BuildRequires:  icu4j
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  unzip
Requires:       apache-commons-logging
Requires:       icu4j
BuildArch:      noarch

%description
The Apache PDFBox library is an open source Java tool for working with PDF documents.
This project allows creation of new PDF documents, manipulation of existing documents
and the ability to extract content from documents.
Apache PDFBox also includes several command line utilities.

%package javadoc
Summary:        API Documentation for PDFBox
Group:          Documentation/HTML
Requires:       %{name} = %{version}-%{release}

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n pdfbox-%{version}
%autopatch -p1

%build
# Build
ant -buildfile pdfbox/build.xml \
    -Dbcprov.jar=$(build-classpath bcprov) -Djunit.jar=$(build-classpath junit4) \
    -Dicu4j.jar=$(build-classpath icu4j) -Dlogging.jar=$(build-classpath commons-logging) \
    -Dbuild.sysclasspath=first -Dcompile.source=8 -Dcompile.target=8 \
    fontbox.package jempbox.package javadoc

%install
# Code
install -d %{buildroot}%{_javadir}
for jar in fontbox jempbox; do
    install -p -m644 ${jar}/target/${jar}-%{version}.jar %{buildroot}%{_javadir}/${jar}.jar
done

install -d -m 0755 %{buildroot}/%{_mavenpomdir}/
install -m 0644 %{SOURCE2} %{buildroot}/%{_mavenpomdir}/JPP-fontbox.pom
install -m 0644 %{SOURCE3} %{buildroot}/%{_mavenpomdir}/JPP-jempbox.pom

%add_maven_depmap JPP-fontbox.pom fontbox.jar
%add_maven_depmap JPP-jempbox.pom jempbox.jar

# JavaDoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr pdfbox/target/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files
%doc RELEASE-NOTES.txt NOTICE.txt README.txt
%license LICENSE.txt
%{_javadir}/fontbox.jar
%{_javadir}/jempbox.jar
%{_mavenpomdir}/JPP-fontbox.pom
%{_mavenpomdir}/JPP-jempbox.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%changelog
