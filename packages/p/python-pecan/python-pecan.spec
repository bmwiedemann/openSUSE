#
# spec file for package python-pecan
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pecan
Version:        1.3.3
Release:        0
Summary:        A WSGI object-dispatching web framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pecan/pecan
Source:         https://files.pythonhosted.org/packages/source/p/pecan/pecan-%{version}.tar.gz
Patch0:         pecan-no-kajiki.patch
BuildRequires:  %{python_module Genshi >= 0.7}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module Mako >= 0.4.0}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WebOb >= 1.2}
BuildRequires:  %{python_module WebTest >= 1.3.1}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module logutils}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module virtualenv}
BuildRequires:  fdupes
BuildRequires:  python-pysqlite
BuildRequires:  python-rpm-macros
BuildRequires:  python2-singledispatch
Requires:       python-Mako >= 0.4.0
Requires:       python-WebOb >= 1.2
Requires:       python-WebTest >= 1.3.1
Requires:       python-logutils >= 0.3
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-singledispatch
%endif
%if 0%{?suse_version}
Suggests:       python-Genshi
Suggests:       python-Jinja2
Suggests:       python-gunicorn
%endif
%python_subpackages

%description
A WSGI object-dispatching web framework.

%prep
%setup -q -n pecan-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pecan
%python_clone -a %{buildroot}%{_bindir}/gunicorn_pecan

%check
%python_exec setup.py test

%post
%python_install_alternative pecan
%python_install_alternative gunicorn_pecan

%postun
%python_uninstall_alternative pecan
%python_uninstall_alternative gunicorn_pecan

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/pecan
%python_alternative %{_bindir}/gunicorn_pecan
%{python_sitelib}/*

%changelog
