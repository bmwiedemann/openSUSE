#
# spec file for package javahelp2
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


%define oname   javahelp
Name:           javahelp2
Version:        2.0.05
Release:        0
Summary:        Java online help system
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            https://javahelp.dev.java.net/
Source0:        %{name}-src-%{version}.tar.bz2
# svn export -r 59 https://javahelp.dev.java.net/svn/javahelp/trunk javahelp2-2.0.05 --username guest
Source1:        %{name}-jhindexer.sh
Source2:        %{name}-jhsearch.sh
Source3:        %{oname}-%{version}.pom
Source4:        https://javahelp.dev.java.net/license.txt
BuildRequires:  ant >= 1.6.5
BuildRequires:  fdupes
BuildRequires:  geronimo-jsp-2_0-api
BuildRequires:  geronimo-servlet-2_4-api
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
Requires:       geronimo-jsp-2_0-api
Requires:       geronimo-servlet-2_4-api
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
%setup -q
# fix files perms
chmod -R go=u-w *
# remove windows files
find . -type f -name .bat | xargs rm -f
#
# This class provides native browser integration and would require
# JDIC project to be present. Currently there is no such jpackage.org
# package, so deleting the class. When JDIC package is created,
# add BuildProvides and remove the "rm" call.
#
rm jhMaster/JavaHelp/src/new/javax/help/plaf/basic/BasicNativeContentViewerUI.java
mkdir javahelp_nbproject/lib
ln -s $(build-classpath geronimo-jsp-2.0-api) javahelp_nbproject/lib/jsp-api.jar
ln -s $(build-classpath geronimo-servlet-2.4-api) javahelp_nbproject/lib/servlet-api.jar
cp %{SOURCE4} .

%build
ant \
    -f javahelp_nbproject/build.xml \
	-Djavac.source=1.6 -Djavac.target=1.6 \
    -Djdic-jar-present=true \
    -Djdic-zip-present=true \
    -Dservlet-jar-present=true \
    -Dtomcat-zip-present=true \
    release javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/jh2indexer
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/jh2search
install -m 644 javahelp_nbproject/dist/lib/jhall.jar %{buildroot}%{_javadir}/%{name}.jar
#cp -pr jhMaster/JavaHelp/doc/public-spec/dtd %{buildroot}%{_datadir}/%{name}
cp -pr javahelp_nbproject/dist/lib/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files
%doc license.txt
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/%{name}.jar
#%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/dtd
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml

%files manual
%doc jhMaster/JavaHelp/doc/public-spec/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
