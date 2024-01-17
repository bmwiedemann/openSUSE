#
# spec file for package uom-parent
#
# Copyright (c) 2020 SUSE LLC
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


Name:           uom-parent
Version:        1.3
Release:        0
Summary:        Units of Measurement Project Parent POM
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/unitsofmeasurement/uom-parent
Source0:        https://github.com/unitsofmeasurement/uom-parent/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-install-plugin
BuildRequires:  maven-local
BuildArch:      noarch

%description
Main parent POM for all Units of Measurement Maven projects.

%prep
%setup -q
%pom_remove_parent

%build
%{mvn_build}

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
