#
# spec file for package apache-pdfbox
#
# Copyright (c) 2020 SUSE LLC
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


# Only fontbox and jempbox are built as pdfbox itself depends on Adobe's pcif.
Name:           apache-pdfbox
Version:        2.0.19
Release:        0
Summary:        Java PDF Library
License:        Apache-2.0 AND OFL-1.1
Group:          Development/Libraries/Java
URL:            https://pdfbox.apache.org/
Source0:        http://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip
Source1:        pdfbox-%{version}-build.tar.xz
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-mail
BuildRequires:  bouncycastle-pkix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  unzip
Requires:       apache-commons-logging
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
%setup -q -n pdfbox-%{version} -a1
%pom_change_dep :junit :::test fontbox

%build
mkdir -p lib
build-jar-repository -s lib bcmail bcpkix bcprov commons-logging
ant -Dtest.skip=true package javadoc

%install
# Code
install -d -m 0755 %{buildroot}%{_javadir}/pdfbox
install -d -m 0755 %{buildroot}%{_mavenpomdir}/pdfbox
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
for jar in fontbox pdfbox debugger tools; do
    install -p -m 0644 ${jar}/target/*-%{version}.jar %{buildroot}%{_javadir}/pdfbox/${jar}.jar
	%pom_remove_parent ${jar}
	%pom_xpath_inject pom:project "<groupId>org.apache.pdfbox</groupId><version>%{version}</version>" ${jar}
	install -p -m 0644 ${jar}/pom.xml %{buildroot}%{_mavenpomdir}/pdfbox/${jar}.pom
	%add_maven_depmap pdfbox/${jar}.pom pdfbox/${jar}.jar
	cp -pr ${jar}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${jar}
done
# Compatibility link
ln -s -f %{_javadir}/pdfbox/fontbox.jar %{buildroot}%{_javadir}/

%fdupes -s %{buildroot}%{_javadocdir}

%files javadoc
%{_javadocdir}/%{name}

%files -f .mfiles
%doc RELEASE-NOTES.txt README.md
%license LICENSE.txt NOTICE.txt
%{_javadir}/fontbox.jar

%changelog
