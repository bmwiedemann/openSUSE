#
# spec file for package jackson-parent
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           jackson-parent
Version:        2.9.1
Release:        0
Summary:        Parent pom for all Jackson components
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/jackson-parent
Source0:        https://github.com/FasterXML/jackson-parent/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildArch:      noarch

%description
Project for parent pom for all Jackson components.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%build
%{mvn_build} -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
