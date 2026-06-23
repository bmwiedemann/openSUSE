#
# spec file for package apache-commons-net
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


%global base_name    net
%global short_name   commons-%{base_name}
Name:           apache-%{short_name}
Version:        3.13.0
Release:        0
Summary:        Internet protocol suite Java library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package examples
Summary:        Internet protocol suite Java library (Examples)
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description examples
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

This package contains the examples.

%package ftp
Summary:        Internet protocol suite Java library (FTP)
Group:          Development/Libraries/Java

%description ftp
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

This package contains the FTP related subset of classes.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib commons-io
ant jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
install -pm 0644 target/%{short_name}-%{version}-examples.jar %{buildroot}%{_javadir}/%{short_name}-examples.jar
install -pm 0644 target/%{short_name}-%{version}-ftp.jar %{buildroot}%{_javadir}/%{short_name}-ftp.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
%add_maven_depmap %{short_name}:%{short_name}::examples:%{version} %{short_name}-examples.jar -f examples
%add_maven_depmap %{short_name}:%{short_name}::ftp:%{version} %{short_name}-ftp.jar -f ftp

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files examples -f .mfiles-examples
%license LICENSE.txt NOTICE.txt

%files ftp -f .mfiles-ftp
%license LICENSE.txt NOTICE.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
