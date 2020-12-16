#
# spec file for package icingaweb2-module-ipl
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
%define basedir	%{_datadir}/icingaweb2
%define module_name ipl
Name:           icingaweb2-module-%{module_name}
Version:        0.5.0
Release:        0
Summary:        Business Processes Icinga Web 2 module
License:        MIT
Group:          System/Monitoring
URL:            https://www.icinga.org
Source0:        https://github.com/Icinga/icingaweb2-module-%{module_name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       icingaweb2
Requires:       icingaweb2-module-director
BuildArch:      noarch

%description
Create top-level views of your applications in a graphical editor.
Rules express dependencies between existing hosts and services and
let you alert on application level. Business processes are displayed
in a tree or list overview.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}/vendor
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}/asset
cp -prv vendor %{buildroot}%{basedir}/modules/%{module_name}
cp -prv asset %{buildroot}%{basedir}/modules/%{module_name}
cp -pv *.md *.php *.info %{buildroot}%{basedir}/modules/%{module_name}

%files
%license LICENSE
%doc README.md
%dir %{basedir}
%dir %{basedir}/modules
%dir %{basedir}/modules/%{module_name}
%{basedir}/modules/%{module_name}/*

%changelog
