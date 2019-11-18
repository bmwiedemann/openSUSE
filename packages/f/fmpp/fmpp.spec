#
# spec file for package fmpp
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           fmpp
Version:        0.9.16
Release:        0
Summary:        FreeMarker-based text file PreProcessor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://fmpp.sourceforge.net
Source0:        %{name}-%{version}.tar.xz
Patch0:         fmpp-0.9.16-build.xml.patch
Patch1:         fmpp-0.9.16-excise-imageinfo.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildArch:      noarch

%description

FMPP is a general-purpose text file preprocessor tool that uses
FreeMarker templates. It is particularly designed for HTML
preprocessor, to generate complete (static) homepages: directory
structure that contains HTML-s, image files, etc. But of course it can
be used to generate source code or whatever text files. FMPP is
extendable with Java classes to pull data from any data sources
(database, etc.) and embed the data into the generated files.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

build-jar-repository -s lib freemarker ant/ant bsh2 xml-resolver

%build

%{ant} \
	-Ddependency.freemarker.version=2.3.22 \
	-Ddependency.bsh.version=2.0b4 \
	-Ddependency.xmlResolver.version=1.2 \
	jar javadoc maven-pom

%{mvn_artifact} build/pom.xml lib/fmpp.jar

%install
%mvn_install -J build/docs/api
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc README.txt

%changelog
