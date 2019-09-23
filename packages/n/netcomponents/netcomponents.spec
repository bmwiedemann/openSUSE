#
# spec file for package netcomponents
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           netcomponents
Version:        1.3.8
Release:        0
Summary:        Internet Protocol Suite Java Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
Url:            http://www.savarese.org/java/
Source:         http://www.savarese.org/downloads/NetComponents/NetComponents-1.3.8-src.tar.gz
Patch0:         %{name}-java14compat.patch
# PATCH-FIX-OPENSUSE Fix build due to non-existent overview-frame.html file
Patch1:         netcomponents-overview-frame.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  xml-commons-apis
BuildArch:      noarch

%description
NetComponents is an Internet protocol suite Java library originally
developed by ORO, Inc.	This version supports Finger, Whois, TFTP,
Telnet, POP3, FTP, NNTP, SMTP, and some miscellaneous protocols like
Time and Echo as well as BSD R command support.  The purpose of the
library is to provide fundamental protocol access, not higher-level
abstractions.  Therefore, some of the design violates object-oriented
design principles.  Its philosophy is to make the global functionality
of a protocal accesible (for example, TFTP send file and receive file)
when possible, but also provide access to the fundamental protocols
where applicable so that the programmer can construct custom
implementations (for example, the TFTP packet classes and the TFTP
packet send and receive methods are exposed).

%package javadoc
Summary:        Javadoc for netcomponents
Group:          Development/Libraries/Java

%description javadoc
NetComponents, is an Internet protocol suite Java library originally
developed by ORO, Inc.	This version supports Finger, Whois, TFTP,
Telnet, POP3, FTP, NNTP, SMTP, and some miscellaneous protocols like
Time and Echo as well as BSD R command support.  The purpose of the
library is to provide fundamental protocol access, not higher-level
abstractions.  Therefore, some of the design violates object-oriented
design principles.  Our philosophy is to make the global functionality
of a protocal accesible (e.g., TFTP send file and receive file) when
possible, but also provide access to the fundamental protocols where
applicable so that the programmer may construct his own custom
implementations (e.g, the TFTP packet classes and the TFTP packet send
and receive methods are exposed).

This package contains the javadoc documentation for netcomponents.

%prep
%setup -q -n NetComponents-%{version}
%patch0 -p1
%patch1 -p1

%build
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    jar javadocs

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/NetComponents-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc CHANGES README COPYRIGHT LICENSE
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
