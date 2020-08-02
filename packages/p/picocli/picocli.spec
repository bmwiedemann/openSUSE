#
# spec file for package picocli
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


Name:           picocli
Version:        4.0.4
Release:        0
Summary:        Tiny Command Line Interface
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://picocli.info/
Source0:        https://github.com/remkop/%{name}/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  aqute-bnd
BuildArch:      noarch

%description
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%pom_xpath_set pom:project/pom:version %{version}

%build
%mvn_build -f
# Convert to OSGi bundle
bnd wrap \
 --bsn %{name} \
 --version %{version} \
 --output target/%{name}-%{version}.bar \
 --properties bnd.bnd \
 target/%{name}-%{version}.jar
mv target/%{name}-%{version}.bar target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
