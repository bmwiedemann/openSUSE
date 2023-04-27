#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global cluster jnr
Name:           %{cluster}-posix
Version:        3.1.16
Release:        0
Summary:        Java Posix layer
License:        CPL-1.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java,
written in Java and is part of the JNR project (http://github.com/jnr).

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%{mvn_file} : %{cluster}/%{name}

# Remove useless wagon extension.
%pom_xpath_remove "pom:build/pom:extensions"

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
