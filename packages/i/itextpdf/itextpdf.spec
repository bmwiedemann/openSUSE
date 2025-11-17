#
# spec file for package itextpdf
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


Name:           itextpdf
Version:        5.5.13.4
Release:        0
Summary:        A Free Java-PDF library
License:        AGPL-3.0-only
Group:          Development/Libraries/Java
URL:            https://itextpdf.com
Source0:        https://github.com/itext/%{name}/archive/%{version}.tar.gz
Patch0:         0001-Upgrade-to-commons-imaging-1.0.0-alpha6.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.itextpdf:itext-parent:pom:)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-imaging)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.santuario:xmlsec)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15to18)
BuildArch:      noarch

%description
iText is a library that allows you to generate PDF files on the fly.
The iText classes are very useful for people who need to generate
read-only, platform independent documents containing text, lists,
tables and images. The library is especially useful in combination with
Java(TM) technology-based Servlets: The look and feel of HTML is
browser dependent; with iText and PDF you can control exactly how your
servlet's output will look.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

# Both need git access during the build
%pom_remove_plugin -r :jgitflow-maven-plugin itext
%pom_remove_plugin -r :buildnumber-maven-plugin

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license gnu-agpl-v3.0.md

%files javadoc -f .mfiles-javadoc
%license gnu-agpl-v3.0.md

%changelog
