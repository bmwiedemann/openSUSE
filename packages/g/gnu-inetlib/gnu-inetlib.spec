#
# spec file for package gnu-inetlib
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


%define official_name inetlib
Name:           gnu-inetlib
Version:        1.1
Release:        0
Summary:        Library of clients for common internet protocols
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            http://www.gnu.org/software/classpath/inetlib.html
Source:         %{official_name}-%{version}.tar.bz2
Patch0:         gnu-inetlib-gcc44-build.patch
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  java-devel >= 1.8
BuildRequires:  unzip
Provides:       inetlib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
GNU inetlib is a library of clients for common internet protocols. The
following protocols are currently supported: Hypertext Transfer
Protocol (HTTP) File Transfer Protocol (FTP) Simple Mail Transfer
Protocol (SMTP) Internet Message Access Protocol (IMAP) Post Office
Protocol (POP) Network News Transfer Protocol (NNTP) Lightweight
Directory Access Protocol (LDAP) (alpha) Gopher Finger The inetlib
library is similar in intent to the Python internet protocols library -
the API is as close as possible to the intent of the underlying
protocol design. This allows for very efficient coding of user agents.
Additionally, inetlib includes URLStreamHandler implementations for
some of the protocols. These can be used to add support for the
corresponding URL scheme to the java.net.URL class.

%prep
%setup -q -n %{official_name}
%patch0 -p1

%build
export CLASSPATH=$(build-classpath glibj)
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist

%install
mkdir -p %{buildroot}/%{_javadir}
cp %{official_name}.jar %{buildroot}/%{_javadir}

%files
%defattr(-,root,root)
%{_javadir}/*

%changelog
