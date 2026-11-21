#
# spec file for package apache-pdfbox
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "extras"
%bcond_without extras
%else
%bcond_with extras
%endif
Version:        3.0.8
Release:        0
%if %{with extras}
Name:           apache-pdfbox-%{flavor}
%else
Name:           apache-pdfbox
%endif
License:        Apache-2.0 AND OFL-1.1
Group:          Development/Libraries/Java
URL:            https://pdfbox.apache.org/
Source0:        https://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip
Source1:        https://archive.apache.org/dist/pdfbox/%{version}/pdfbox-%{version}-src.zip.asc
Source2:        pdfbox-build.tar.xz
Source3:        https://www.apache.org/dist/pdfbox/KEYS#/pdfbox.keyring
BuildRequires:  ant
BuildRequires:  apache-commons-logging
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-mail
BuildRequires:  bouncycastle-pkix
BuildRequires:  bouncycastle-util
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildArch:      noarch
%if %{with extras}
Summary:        Extra modules for Apache PDFBox
BuildRequires:  apache-commons-io
BuildRequires:  apache-pdfbox = %{version}
BuildRequires:  lucene-analyzers-common
BuildRequires:  lucene-core
BuildRequires:  picocli
Requires:       apache-commons-io
Requires:       apache-commons-logging
Requires:       apache-pdfbox = %{version}
Requires:       apache-pdfbox-jbig2
Requires:       bouncycastle
Requires:       bouncycastle-pkix
Requires:       bouncycastle-util
Requires:       javapackages-tools
Requires:       picocli
%else
Summary:        Java PDF Library
Requires:       apache-commons-logging
%endif

%description
The Apache PDFBox library is an open source Java tool for working with PDF documents.
This project allows creation of new PDF documents, manipulation of existing documents
and the ability to extract content from documents.
Apache PDFBox also includes several command line utilities.
%if %{with extras}

This package contains extra modules for Apache PDFBox that depend on picocli.
%endif

%package javadoc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}-%{release}

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q -n pdfbox-%{version} -a2

# Remove provided binaries
find -name '*.class' -delete
find -name '*.jar' -delete

%build
mkdir -p lib
build-jar-repository -s lib bcmail bcpkix bcprov bcutil commons-logging
%if %{without extras}
ant -Dproject.version=%{version} -Dtest.skip=true package javadoc
%else
build-jar-repository -s lib ant/ant commons-io lucene/lucene-core lucene/lucene-analyzers-common pdfbox picocli
ant -f build-extras.xml -Dproject.version=%{version} -Dtest.skip=true package javadoc
%endif

%install
# Code
install -d -m 0755 %{buildroot}%{_javadir}/pdfbox
install -d -m 0755 %{buildroot}%{_mavenpomdir}/pdfbox
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%if %{without extras}
  for jar in fontbox io pdfbox xmpbox; do
    install -p -m 0644 ${jar}/target/*-%{version}.jar %{buildroot}%{_javadir}/pdfbox/${jar}.jar
    %{mvn_install_pom} ${jar}/pom.xml %{buildroot}%{_mavenpomdir}/pdfbox/${jar}.pom
    %add_maven_depmap pdfbox/${jar}.pom pdfbox/${jar}.jar
    cp -pr ${jar}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${jar}
  done
%else
  for jar in debugger tools preflight examples; do
    install -p -m 0644 ${jar}/target/*-%{version}.jar %{buildroot}%{_javadir}/pdfbox/${jar}.jar
    %{mvn_install_pom} ${jar}/pom.xml %{buildroot}%{_mavenpomdir}/pdfbox/${jar}.pom
    %add_maven_depmap pdfbox/${jar}.pom pdfbox/${jar}.jar
    cp -pr ${jar}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${jar}
  done
  %jpackage_script org.apache.pdfbox.tools.PDFBox "" "" pdfbox:commons-logging:commons-io:picocli:bcpkix:bcprov:bcutil:apache-pdfbox-jbig2 pdfbox true
  %jpackage_script org.apache.pdfbox.debugger.PDFDebugger "" "" pdfbox:commons-logging:commons-io:picocli:bcpkix:bcprov:bcutil:apache-pdfbox-jbig2 pdfbox-debugger true
  %jpackage_script org.apache.pdfbox.preflight.Validator_A1b "" "" pdfbox:commons-logging:commons-io:picocli:bcpkix:bcprov:bcutil:apache-pdfbox-jbig2 pdfbox-preflight true
%endif

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt README.md
%if %{with extras}
%{_bindir}/pdfbox
%{_bindir}/pdfbox-debugger
%{_bindir}/pdfbox-preflight
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
