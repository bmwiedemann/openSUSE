#
# spec file for package python-Glances
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


%define         skip_python2 1
Name:           python-Glances
Version:        3.3.1
Release:        0
Summary:        A cross-platform curses-based monitoring tool
License:        LGPL-3.0-only
URL:            https://github.com/nicolargo/glances
Source:         https://github.com/nicolargo/glances/archive/v%{version}.tar.gz
Source2:        glances.service
Source3:        glances.firewalld
Patch0:         adjust-data-files.patch
Patch1:         remove-shebang.patch
Patch2:         skip-online-tests.patch
Patch3:         fix-tests.patch
Patch4:         unitest-wait-for-server.patch
BuildRequires:  %{python_module bottle}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module psutil >= 5.3.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ujson}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bottle
Requires:       python-defusedxml
Requires:       python-future
Requires:       python-psutil >= 5.3.0
Requires:       python-requests
Requires:       python-ujson
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-curses
Provides:       python-glances = %{version}
Obsoletes:      python-glances < %{version}
Provides:       glances
BuildArch:      noarch
%python_subpackages

%description
Glances is a cross-platform monitoring tool which presents a
large amount of monitoring information through a curses or Web
based interface. The information dynamically adapts depending on the
size of the user interface.

%package -n glances-common
Summary:        Service and firewalld files for glances
Requires:       glances

%description -n glances-common
Glances is a cross-platform monitoring tool which presents a
large amount of monitoring information through a curses or Web
based interface. The information dynamically adapts depending on the
size of the user interface.

This packages contains the service file to start a glances server
from systemd and a firewalld file to open the default port.

%prep
%setup -q -n glances-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_mandir}/man1/glances.1
%python_clone -a %{buildroot}%{_bindir}/glances
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rcglances
mkdir -p %{buildroot}%{_unitdir}
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/

mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
install -D -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/glances.xml

%check
export LANG=en_US.UTF-8
%python_exec unitest.py
%python_exec unitest-restful.py
%python_exec unitest-xmlrpc.py

%post
%python_install_alternative glances glances.1

%postun
%python_uninstall_alternative glances

%pre -n glances-common
%service_add_pre glances.service

%post -n glances-common
%service_add_post glances.service

%preun -n glances-common
%service_del_preun glances.service

%postun -n glances-common
%service_del_postun glances.service

%files %{python_files}
%license COPYING
%doc NEWS.rst README.rst
%python_alternative %{_bindir}/glances
%python_alternative %{_mandir}/man1/glances.1%{?ext_man}
%{python_sitelib}/glances
%{python_sitelib}/Glances-%{version}*-info
%exclude %{python_sitelib}/glances/outputs/static/.eslintrc.js
%exclude %{python_sitelib}/glances/outputs/static/.gitignore
%exclude %{python_sitelib}/glances/outputs/static/.prettierrc.js

%files -n glances-common
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/glances.xml
%{_unitdir}/glances.service
%{_sbindir}/rcglances

%changelog
