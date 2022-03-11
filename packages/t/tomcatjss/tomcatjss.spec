#
# spec file for package tomcatjss
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <stasiek@michalski.cc>.
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


Name:           tomcatjss
Version:        7.4.1
Release:        0
Summary:        JSS Connector for Apache Tomcat
License:        LGPL-2.0-or-later
URL:            https://www.dogtagpki.org/wiki/TomcatJSS
Source:         https://github.com/dogtagpki/tomcatjss/archive/v%{version}/tomcatjss-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  apache-commons-lang
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  mozilla-jss >= 4.6
BuildRequires:  slf4j
BuildRequires:  slf4j-jdk14
BuildRequires:  tomcat >= 9.0.7
Requires:       apache-commons-lang
Requires:       mozilla-jss > 4.6
Requires:       slf4j
Requires:       slf4j-jdk14
Requires:       tomcat >= 9.0.7
BuildArch:      noarch

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

%prep
%setup -q

%build
# Skip build

%install
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
%if %{?pkg_vcmp:%pkg_vcmp mozilla-jss >= 5}%{!?pkg_vcmp:0}
	-Djss.jar=$(find-jar jss) \
%else
	-Djss.jar=$(find-jar jss4) \
%endif
    -Dversion=%{version} \
    -Dsrc.dir=tomcat-8.5 \
    -Djnidir=%{_jnidir} \
    -Dinstall.doc.dir=%{buildroot}%{_docdir}/%{name} \
    -Dinstall.jar.dir=%{buildroot}%{_javadir} \
    install

# We use a separate licenses directory
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%license LICENSE
%doc README
%{_javadir}/*

%changelog
