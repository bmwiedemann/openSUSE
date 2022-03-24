#
# spec file
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


%define base_name       launcher
%define short_name      commons-%{base_name}
Name:           jakarta-%{short_name}
Version:        1.1
Release:        0
Summary:        A Cross-Platform Java Application Launcher
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://jakarta.apache.org/commons/launcher/
Source:         https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  junit
BuildRequires:  xml-commons-apis
BuildArch:      noarch

%description
Commons-launcher eliminates the need for a batch or shell script to
launch a Java class. Some situations where elimination of a batch or
shell script may be desirable are:

* You want to avoid having to determining where certain application
   paths are, for example, your application's home directory.
   Determining this dynamically in a Windows batch script is very
   tricky on some versions of Windows or when softlinks are used on
   Unix platforms.

* You want to avoid having to handle native file and path separators
   or native path quoting issues.

* You need to enforce certain system properties, such as
   java.endorsed.dirs when running with JDK 1.4.

* You want to allow users to pass custom JVM arguments or system
   properties without having to parse and reorder arguments in your
   script. This can be tricky or messy in batch and shell scripts.

* You want to bootstrap system properties from a configuration file
   instead of hard-coding them in your batch and shell scripts.

* You want to provide localized error messages, which is very tricky to
   do in batch and shell scripts.

%package        javadoc
Summary:        Javadoc for jakarta-commons-launcher
Group:          Development/Libraries/Java
Requires(pre):  coreutils

%description    javadoc
Commons-launcher eliminates the need for a batch or shell script to
launch a Java class.

This package contains the javadoc documentation for the Jakarta Commons
Launcher Package.

%prep
%setup -q -n %{short_name}

%build
mkdir lib
ant \
  -Dbuild.sysclasspath=only \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dsrcdir=. \
  -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
  jar javadoc

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/bin/%{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files
%license LICENSE.txt
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
