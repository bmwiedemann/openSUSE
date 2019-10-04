#
# spec file for package jakarta-commons-transaction
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define base_name commons-transaction
Name:           jakarta-commons-transaction
Version:        1.1
Release:        0
Summary:        Commons Transaction
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/commons/transaction/
Source0:        commons-transaction-1.1-src.tar.bz2
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        commons-transaction-1.1-jpp-depmap.xml
Patch0:         commons-transaction-1.1-project_xml.patch
BuildRequires:  ant >= 1.6
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-codec
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  log4j12
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       geronimo-jta-1_1-api
Requires:       jakarta-commons-codec
Requires:       log4j12
Requires:       xerces-j2
Requires:       xml-commons-apis
BuildArch:      noarch

%description
Commons Transaction aims at providing lightweight, standardized, well
tested and efficient implementations of utility classes commonly used
in transactional Java programming. Initially there are implementations
for multi level locks, transactional collections and transactional file
access. There may be additional implementations when the common need
for them becomes obvious. However, the complete component shall remain
compatible to JDK1.2 and should have minimal dependencies.

%prep
%setup -q -c -n %{base_name}
find . -name "*.jar" | xargs rm
%patch0 -b .sav

%build
export CLASSPATH=$(build-classpath commons-codec jta log4j12/log4j-12):`pwd`/build/classes
export OPT_JAR_LIST=:
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Dbuild.sysclasspath=only -Dant.java.version=1.6 -Dcompile.target=1.6 \
	jar

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/commons-transaction-1.1.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in jakarta-*; do \
ln -sf ${jar} ${jar/jakarta-/}; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%files
%doc LICENSE.txt
%{_javadir}/*

%changelog
