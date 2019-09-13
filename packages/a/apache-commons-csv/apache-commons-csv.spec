#
# spec file for package apache-commons-csv
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


%global base_name csv
%global short_name commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.6
Release:        0
Summary:        A library to read and write files in variations of the Comma Separated Value (CSV) format
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-csv/
Source0:        http://archive.apache.org/dist/commons/csv/source/commons-csv-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildArch:      noarch

%description
Commons CSV reads and writes files in variations of the Comma Separated Value (CSV) format.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-csv-%{version}-src

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
