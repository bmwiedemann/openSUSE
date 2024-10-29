#
# spec file for package noggit
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


Name:           noggit
Version:        0.8
Release:        0
Summary:        JSON streaming parser
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/yonik/%{name}
Source0:        %{url}/archive/refs/tags/noggit-0.8.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Noggit is the world’s fastest streaming JSON parser for Java.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
chmod 0644 LICENSE.txt README.md

%pom_remove_plugin :maven-compiler-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
