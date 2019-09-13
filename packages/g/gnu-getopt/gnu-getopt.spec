#
# spec file for package gnu-getopt
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


Name:           gnu-getopt
Version:        1.0.13
Release:        0
Summary:        Java getopt Implementation
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
Url:            http://www.urbanophile.com/arenn/hacking/download.html
Source0:        ftp://ftp.urbanophile.com/pub/arenn/software/sources/java-getopt-%{version}.tar.bz2
Patch0:         %{name}-java8compat.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The GNU Java getopt classes support short and long argument parsing in
a manner 100% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that this
is a port, not a new implementation.

%package javadoc
Summary:        Javadoc for gnu.getopt
Group:          Development/Libraries/Java

%description javadoc
The GNU Java getopt classes support short and long argument parsing in
a manner 100% compatible with the version of GNU getopt in glibc 2.0.6
with a mostly compatible programmer's interface as well. Note that this
is a port, not a new implementation.

This package contains the javadoc documentation for the GNU Java getopt
classes.

%prep
%setup -q -c
%patch0
mv gnu/getopt/buildx.xml build.xml

%build
ant jar javadoc

%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 644 build/lib/gnu.getopt.jar %{buildroot}%{_javadir}/gnu.getopt-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a build/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc gnu/getopt/COPYING.LIB gnu/getopt/README
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
