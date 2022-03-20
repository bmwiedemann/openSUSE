#
# spec file for package jakarta-commons-transaction
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


%define base_name commons-transaction
Name:           jakarta-commons-transaction
Version:        1.1
Release:        0
Summary:        Commons Transaction
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jakarta.apache.org/commons/transaction/
Source0:        commons-transaction-1.1-src.tar.bz2
BuildRequires:  ant >= 1.6
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-codec
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  reload4j
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       geronimo-jta-1_1-api
Requires:       jakarta-commons-codec
Requires:       reload4j
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

%build
export CLASSPATH=$(build-classpath commons-codec jta reload4j):`pwd`/build/classes
export OPT_JAR_LIST=:
%{ant} \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    -Dbuild.sysclasspath=only -Dant.java.version=1.8 -Dcompile.target=1.8 \
	jar

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/lib/%{base_name}-%{version}.jar \
           %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{base_name}.jar

%files
%license LICENSE.txt
%{_javadir}/*

%changelog
