#
# spec file for package matthewlib-java
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


%define orig_name libmatthew-java
Name:           matthewlib-java
Version:        0.8
Release:        0
Summary:        A few useful Java libraries
# actual upstream:
#URL: http://matthew.ath.cx/projects/java/
#Source0: http://matthew.ath.cx/projects/java/%{name}-%{version}.tar.gz
# upstream author is also the debian maintainer for this package.
# he gets newer releases into debian before he puts them up on
# the upstream website. so we use the "original" source from debian
# (ie, the source before debian patches are applied to it)
License:        MIT
Group:          Development/Libraries/Java
Source0:        libmatthew-java-0.8.tar.gz
Patch0:         install_doc.patch
Patch1:         classpath_fix.patch
Patch2:         libmatthew-java-0.8-jdk10.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
Requires:       java >= 1.8
Requires:       javapackages-tools
Provides:       %{orig_name}

%description
A collection of Java libraries: - Unix Sockets Library This is a
   collection of classes and native code to allow you to read and
   write Unix sockets in Java.

- Debug Library This is a comprehensive logging and debugging
   solution.

- CGI Library This is a collection of classes and native code to
   allow you to write CGI applications in Java.

- I/O Library This provides a few much needed extensions to the Java
   I/O subsystem.

- Hexdump This class formats byte-arrays in hex and ascii for display.

%package javadoc
Summary:        A few useful Java libraries
Group:          Development/Libraries/Java

%description javadoc
A collection of Java libraries: - Unix Sockets Library This is a
   collection of classes and native code to allow you to read and
   write Unix sockets in Java.

- Debug Library This is a comprehensive logging and debugging
   solution.

- CGI Library This is a collection of classes and native code to
   allow you to write CGI applications in Java.

- I/O Library This provides a few much needed extensions to the Java
   I/O subsystem.

- Hexdump This class formats byte-arrays in hex and ascii for display.

%prep
%setup -q -n %{orig_name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make \
    CFLAGS='%{optflags} -fpic -std=c99' \
    LIBDIR='%{_libdir}' \
    LD='gcc' \
    JCFLAGS='-target 1.8 -source 1.8'

%install
make install \
    DESTDIR=%{buildroot} \
    JARDIR=%{_javadir} \
    LIBDIR=%{_libdir}/ \
    DOCDIR=%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_javadir}/*jar
%{_libdir}/lib*.so*
%license COPYING
%doc README

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
