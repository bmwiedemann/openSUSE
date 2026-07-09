#
# spec file for package aalto-xml
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


Name:           aalto-xml
Version:        1.4.0
Release:        0
Summary:        Ultra-high performance non-blocking XML processor (Stax API + extensions)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  stax2-api
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
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib stax2-api
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc {README,SECURITY}.md release-notes/{VERSION,CREDITS,TODO}

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
