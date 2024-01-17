#
# spec file for package jnr-netdb
#
# Copyright (c) 2021 SUSE LLC
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
Name:           %{cluster}-netdb
Version:        1.2.0
Release:        0
Summary:        Network services database access for java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}/
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3).

It tries to use the native functions if possible, falling back to parsing
/etc/services directly, and finally to an inbuilt table for use in environments
where neither native code, nor filesystem access is possible.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%{mvn_file} : %{cluster}/%{name}

find . -name '*.jar' -delete

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
