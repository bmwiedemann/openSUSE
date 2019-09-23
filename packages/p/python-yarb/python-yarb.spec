#
# spec file for package python-yarb
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
%define simple_name yarb
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{simple_name}
Version:        1.0.0
Release:        0
Url:            https://github.com/Itxaka/%{simple_name}
Summary:        Yet Another Rabbitmq Balancer
License:        GPL-2.0-only
Group:          Development/Languages/Python
Source:         %{simple_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires(post):   update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
yarb is an script that tries to balance a rabbitmq cluster by calculating and
deleting queues that should not be in a node in order to let them be recreated
in a different node, reaching a more balanced cluster.

%prep
%setup -q -n %{simple_name}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/yarb
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{simple_name}
%fdupes %{buildroot}%{_bindir}

%check
%python_exec setup.py test

%post
%python_install_alternative yarb

%postun
%python_uninstall_alternative yarb

%files  %{python_files}
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/yarb
%{python_sitelib}/yarb/
%{python_sitelib}/yarb-*.egg-info

%changelog
