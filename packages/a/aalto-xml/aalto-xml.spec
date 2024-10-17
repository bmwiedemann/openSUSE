#
# spec file for package aalto-xml
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


Name:           aalto-xml
Version:        1.3.3
Release:        0
Summary:        Ultra-high performance non-blocking XML processor (Stax API + extensions)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildArch:      noarch

%description
Aalto XML processor is an ultra-high performance next generation Stax XML
processor implementation, implementing both basic Stax API (javax.xml.stream)
and Stax2 API extension (org.codehaus.woodstox.stax2). In addition, it also
implements SAX2 API.

In additional to standard Java XML interfaces, one unique feature not
implemented by any other Java XML parser that we are aware is so-called
non-blocking (asynchronous) XML parsing: ability to parse XML without using
blocking I/O, necessary for fully asynchronous processing such as those with
Akka framework. Aalto non-blocking API is a minimalistic extension above
Stax/Stax2 API to allow indication of "not yet available" token
(EVENT_INCOMPLETE) as well as feeding of input (since InputStream can not be
used as it blocks).

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Djava.version=8

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc {README,SECURITY}.md release-notes/{VERSION,CREDITS,TODO}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
