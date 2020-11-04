#
# spec file for package time-api
#
# Copyright (c) 2019 SUSE LLC
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


%global oname threeten
Name:           time-api
Version:        0.6.4
Release:        0
Summary:        JSR-310 - Date and Time API
License:        BSD-3-Clause AND GPL-2.0-or-later AND SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            http://threeten.github.com/
Source0:        https://github.com/ThreeTen/%{oname}/archive/v%{version}.tar.gz
Source1:        %{name}-template-pom.xml
Patch0:         %{name}-0.6.4-dont-compile-openjdk-classes.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildArch:      noarch

%description
A date and time API for Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

# Use system libraries
sed -i 's|src="${maven.ibiblio.url}/@{group}/@{artifact}/@{version}/@{artifact}-@{version}@{variant}.jar"|src="file://%{_datadir}/java/@{artifact}.jar"|' build.xml

%patch0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

sed -i 's/\r//' COPYRIGHT-ASSIGN.txt LICENSE.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt \
 OpenJDKChallenge.txt README.txt RELEASE-NOTES.txt TODO.txt

%build

%{mvn_build} -f

%install

%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

# https://fedoraproject.org/wiki/Packaging:Java#Packages_providing_APIs
mkdir -p %{buildroot}%{_javadir}/javax.time
ln -sf %{_javadir}/%{name}/%{name}.jar %{buildroot}%{_javadir}/javax.time/

%files -f .mfiles
%{_javadir}/javax.time
%license LICENSE.txt
%doc COPYRIGHT-ASSIGN.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt
%doc OpenJDKChallenge.txt README.txt RELEASE-NOTES.txt TODO.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc COPYRIGHT-ASSIGN.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt

%changelog
