#
# spec file for package ldap-sdk
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


%global jarname   ldapjdk
%global spname    ldapsp
%global filtname  ldapfilt
%global beansname ldapbeans
Name:           ldap-sdk
Version:        4.21.0
Release:        0
Summary:        LDAP SDK
License:        GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.0-or-later
URL:            https://www.dogtagpki.org/
Source:         https://github.com/dogtagpki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  mozilla-jss
BuildRequires:  slf4j
BuildRequires:  slf4j-jdk14
Requires:       jpackage-utils >= 1.5
Requires:       mozilla-jss
Requires:       slf4j
Requires:       slf4j-jdk14
Provides:       ldapjdk = %{version}
BuildArch:      noarch

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}

%prep
%autosetup

%pom_xpath_set pom:project/pom:version %{version} %{jarname}.pom

%build
%if %{?pkg_vcmp:%pkg_vcmp mozilla-jss >= 5}%{!?pkg_vcmp:0}
build-jar-repository -s -p java-sdk/ldapjdk/lib jss
ln -sf jss.jar java-sdk/ldapjdk/lib/jss4.jar
%else
build-jar-repository -s -p java-sdk/ldapjdk/lib jss4
%endif
%{ant} -f java-sdk/build.xml dist

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 java-sdk/dist/packages/%{jarname}.jar %{buildroot}%{_javadir}/%{jarname}.jar
install -m 644 java-sdk/dist/packages/%{spname}.jar %{buildroot}%{_javadir}/%{spname}.jar
install -m 644 java-sdk/dist/packages/%{filtname}.jar %{buildroot}%{_javadir}/%{filtname}.jar
install -m 644 java-sdk/dist/packages/%{beansname}.jar %{buildroot}%{_javadir}/%{beansname}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{jarname}.pom %{buildroot}%{_mavenpomdir}/JPP-%{jarname}.pom
%add_maven_depmap JPP-%{jarname}.pom %{jarname}.jar -a "ldapsdk:ldapsdk"

install -d -m 755 %{buildroot}%{_javadocdir}/%{jarname}
cp -r java-sdk/dist/doc/* %{buildroot}%{_javadocdir}/%{name}

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{spname}*.jar
%{_javadir}/%{filtname}*.jar
%{_javadir}/%{beansname}*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
