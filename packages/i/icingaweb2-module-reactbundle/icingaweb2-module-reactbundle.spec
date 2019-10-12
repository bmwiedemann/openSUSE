#
# spec file for package icingaweb2-module-reactbundle
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
%define basedir	%{_datadir}/icingaweb2
%define module_name reactbundle
Name:           icingaweb2-module-%{module_name}
Version:        0.7.0
Release:        0
Summary:        ReactPHP-based 3rd party libraries
License:        MIT
Group:          System/Monitoring
URL:            https://www.icinga.org
Source0:        https://github.com/Icinga/icingaweb2-module-%{module_name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       icingaweb2 >= 2.6.0
Requires:       icingaweb2-module-director
BuildArch:      noarch

%description
Icinga Web 2 - ReactPHP-based 3rd party libraries

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}/vendor
cp -prv vendor %{buildroot}%{basedir}/modules/%{module_name}
cp -pv *.md *.php *.info %{buildroot}%{basedir}/modules/%{module_name}

%files
%license LICENSE
%doc README.md
%dir %{basedir}
%dir %{basedir}/modules
%dir %{basedir}/modules/%{module_name}
%{basedir}/modules/%{module_name}/*

%changelog
