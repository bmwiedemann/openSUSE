#
# spec file for package joda-time
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


%global tzversion tzdata2018i
Name:           joda-time
Version:        2.10.1
Release:        0
Summary:        Java date and time API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.joda.org/joda-time/
Source0:        https://github.com/JodaOrg/%{name}/archive/v%{version}.tar.gz
Source1:        ftp://ftp.iana.org/tz/releases/%{tzversion}.tar.gz
Source100:      %{name}-build.xml
Patch0:         joda-time-fix-tests.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  joda-convert
BuildArch:      noarch

%description
Joda-Time provides a quality replacement for the Java date
and time classes. The design allows for multiple calendar
systems, while still providing a simple API. The 'default'
calendar is the ISO8601 standard which is used by XML. The
Gregorian, Julian, Buddhist, Coptic and Ethiopic systems
are also included, and we welcome further additions.
Supporting classes include time zone, duration, format
and parsing.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
dos2unix LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
cp %{SOURCE100} build.xml

# all java binaries must be removed from the sources
find . -name '*.jar' -exec rm -f '{}' \;

# replace internal tzdata
rm -f src/main/java/org/joda/time/tz/src/*
tar -xzf %{SOURCE1} -C src/main/java/org/joda/time/tz/src/

%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_set pom:project/pom:properties/pom:maven.compiler.source "1.6"
%pom_xpath_set pom:project/pom:properties/pom:maven.compiler.target "1.6"
%pom_xpath_set pom:project/pom:properties/pom:maven.compiler.compilerVersion "1.6"

%build
%{ant} \
  -Djoda-convert.jar=%{_javadir}/joda-convert.jar \
  clean jar javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
# Don't install a versioned jar and symlink to it, instead install
# the unversioned jar as per Java Packaging Guidelines
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
