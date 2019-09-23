#
# spec file for package glassfish-dtd-parser
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


Name:           glassfish-dtd-parser
Version:        1.4
Release:        0
Summary:        Library for parsing XML DTDs
License:        CDDL-1.1 AND GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            http://java.net/projects/dtd-parser
Source0:        https://github.com/javaee/jaxb-dtd-parser/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildArch:      noarch

%description
Library for parsing XML DTDs.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jaxb-dtd-parser-%{version}

%build
pushd dtd-parser
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 9}%{!?pkg_vcmp:1}
rm -f src/module-info.java
%endif

%{mvn_file} :dtd-parser %{name}
%{mvn_build} -f -j

popd

%install
pushd dtd-parser
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f dtd-parser/.mfiles
%license dtd-parser/LICENSE.txt

%if 0
%files javadoc -f dtd-parser/.mfiles-javadoc
%license dtd-parser/LICENSE.txt
%endif

%changelog
