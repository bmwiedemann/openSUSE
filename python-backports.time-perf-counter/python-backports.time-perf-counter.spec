#
# spec file for package python-backports.time-perf-counter
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
%define skip_python3 1
Name:           python-backports.time-perf-counter
Version:        0.0.4
Release:        0
Summary:        Backport of time.perf_counter() for Python < 3.3
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ejd/backports.time_perf_counter
Source:         https://files.pythonhosted.org/packages/source/b/backports.time_perf_counter/backports.time_perf_counter-%{version}.tar.gz
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module setuptools}
BuildRequires:  python2-monotonic
# /SECTION
%ifpython2
Requires:       python-monotonic
%endif
%python_subpackages

%description
Backport of time.perf_counter() for Python < 3.3.

%prep
%setup -q -n backports.time_perf_counter-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__init__.py \
  %{buildroot}%{$python_sitelib}/backports/__pycache__/ \
  %{buildroot}%{$python_sitelib}/*nspkg.pth
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst
%{python_sitelib}/backports/time_perf_counter/
%{python_sitelib}/backports.time_perf_counter*.egg-info/

%changelog
