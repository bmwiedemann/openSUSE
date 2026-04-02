#
# spec file for package icingaweb2-module-monitoring
#
# Copyright (c) 2026 SUSE LLC
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


%define basedir	%{_datadir}/icingaweb2
%define module_name monitoring
Name:           icingaweb2-module-monitoring
Version:        2.12.6
Release:        0
Summary:        Icinga monitoring module
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://github.com/Icinga/icingaweb2-module-monitoring
Source0:        https://github.com/Icinga/icingaweb2-module-monitoring/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       icingaweb2 >= 2.13.0
Requires:       php >= 8.2
BuildArch:      noarch

%description
The Icinga monitoring module.
IDO accessor and UI for your monitoring. This is the initial instalment for
a graphical presentation of Icinga environments. The predecessor of Icinga DB.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}
mkdir -p %{buildroot}%{basedir}/modules/%{module_name}/{application,doc,library,public,test}
cp -prv application doc library public test %{buildroot}%{basedir}/modules/%{module_name}
cp -pv *.php *.info %{buildroot}%{basedir}/modules/%{module_name}

%files
%license
%doc
%dir %{basedir}
%dir %{basedir}/modules
%dir %{basedir}/modules/%{module_name}
%{basedir}/modules/%{module_name}/*


%changelog
