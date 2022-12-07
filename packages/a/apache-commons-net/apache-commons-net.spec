#
# spec file
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


%global base_name    net
%global short_name   commons-%{base_name}
%bcond_with tests
Name:           apache-%{short_name}
Version:        3.9.0
Release:        0
Summary:        Internet protocol suite Java library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml
%pom_remove_parent .

%build
%{ant} \
%if %{without tests}
  -Dtest.skip=true \
%endif
  jar javadoc

%install
# pom
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
