#
# spec file for package python-flower
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


Name:           python-flower
Version:        0.9.3
Release:        0
Summary:        A web frontend for monitoring and administrating Celery clusters
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mher/flower
Source:         https://files.pythonhosted.org/packages/source/f/flower/flower-%{version}.tar.gz
# Tornado 5+ update blocked by salt, so backport the missing piece
Patch0:         backport_run_in_executor.patch
BuildRequires:  %{python_module Babel >= 1.0}
BuildRequires:  %{python_module celery >= 3.1.0}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module kombu}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.2.0}
BuildRequires:  fdupes
BuildRequires:  python-futures
Requires:       python-Babel >= 1.0
Requires:       python-celery >= 3.1.0
Requires:       python-certifi
Requires:       python-pytz
Requires:       python-tornado >= 4.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-futures
%endif
%python_subpackages

%description
Flower is a web based tool for monitoring and administrating Celery clusters.

%prep
%setup -q -n flower-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/flower
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative flower

%postun
%python_uninstall_alternative flower

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/flower

%changelog
