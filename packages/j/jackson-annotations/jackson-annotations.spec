#
# spec file for package jackson-annotations
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


Name:           jackson-annotations
Version:        2.9.4
Release:        0
Summary:        Core annotations for Jackson data processor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/jackson-annotations/
Source0:        https://github.com/FasterXML/jackson-annotations/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
Core annotations used for value types,
used by Jackson data-binding package.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
sed -i 's/\r//' LICENSE

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
