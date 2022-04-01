#
# spec file for package javahelp2
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


%define oname   javahelp
Name:           javahelp2
Version:        2.0.05
Release:        0
Summary:        Java online help system
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/javaee/javahelp
Source0:        %{oname}-%{version}.tar.xz
BuildRequires:  ant >= 1.6.5
BuildRequires:  fdupes
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       glassfish-jsp-api
Requires:       glassfish-servlet-api
BuildArch:      noarch

%description
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%package manual
Summary:        Java online help system
Group:          Development/Libraries/Java

%description manual
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%package javadoc
Summary:        Java online help system
Group:          Development/Libraries/Java

%description javadoc
JavaHelp software is a full-featured, platform-independent, extensible
help system that enables developers and authors to incorporate online
help in applets, components, applications, operating systems, and
devices. Authors can also use the JavaHelp software to deliver online
documentation for the Web and corporate Intranet.

%prep
%setup -q -n %{oname}-%{version}

# fix files perms
chmod -R go=u-w *

# remove windows files
find . -type f -name .bat | xargs rm -f

# This class provides native browser integration and would require
# JDIC project to be present.
rm jhMaster/JavaHelp/src/new/javax/help/plaf/basic/BasicNativeContentViewerUI.java

mkdir javahelp_nbproject/lib
ln -s $(build-classpath glassfish-jsp-api) javahelp_nbproject/lib/jsp-api.jar
ln -s $(build-classpath glassfish-servlet-api) javahelp_nbproject/lib/servlet-api.jar

%build
ant \
    -f javahelp_nbproject/build.xml \
	-Djavac.source=1.8 -Djavac.target=1.8 \
    -Djdic-jar-present=true \
    -Djdic-zip-present=true \
    -Dservlet-jar-present=true \
    -Dtomcat-zip-present=true \
    release javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 javahelp_nbproject/dist/lib/jhall.jar %{buildroot}%{_javadir}/%{name}.jar

# maven artifact
%add_maven_depmap javax.help:javahelp:%{version} %{name}.jar

# scripts
%jpackage_script com.sun.java.help.search.Indexer "" "" javahelp2 jh2indexer true
%jpackage_script com.sun.java.help.search.QueryEngine "" "" javahelp2 jh2search true
#install -d -m 755 %{buildroot}%{_bindir}
#install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/jh2indexer
#install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/jh2search

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr javahelp_nbproject/dist/lib/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%attr(0755,root,root) %{_bindir}/*

%files manual
%doc jhMaster/JavaHelp/doc/public-spec/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
