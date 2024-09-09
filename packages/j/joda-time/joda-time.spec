#
# spec file for package joda-time
#
# Copyright (c) 2024 SUSE LLC
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


%global spec_version 2.12
%global tzversion tzdata2024a
Name:           joda-time
Version:        %{spec_version}.7
Release:        0
Summary:        Java date and time API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.joda.org/joda-time/
Source0:        https://github.com/JodaOrg/%{name}/archive/v%{version}.tar.gz
Source1:        ftp://ftp.iana.org/tz/releases/%{tzversion}.tar.gz
Source100:      %{name}-build.xml
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
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

dos2unix LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
cp %{SOURCE100} build.xml

# all java binaries must be removed from the sources
find . -name '*.jar' -exec rm -f '{}' \;

# replace internal tzdata
rm -f src/main/java/org/joda/time/tz/src/*
tar -xzf %{SOURCE1} -C src/main/java/org/joda/time/tz/src/

%build
%{ant} \
  -Dproject.version=%{version} \
  -Dproject.spec.version=%{spec_version} \
  -Djoda-convert.jar=%{_javadir}/joda-convert.jar \
  clean jar javadoc

%install
# jars
install -dm0755 %{buildroot}%{_javadir}
# Don't install a versioned jar and symlink to it, instead install
# the unversioned jar as per Java Packaging Guidelines
install -m0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# poms
install -dm0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
