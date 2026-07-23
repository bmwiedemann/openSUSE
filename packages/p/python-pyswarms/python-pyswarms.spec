#
# spec file for package python-pyswarms
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-pyswarms
Version:        1.3.0
Release:        0
Summary:        A Python-based Particle Swarm Optimization (PSO) library
License:        MIT
URL:            https://github.com/ljvmiranda921/pyswarms
Source:         https://files.pythonhosted.org/packages/source/p/pyswarms/pyswarms-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-attrs
Requires:       python-matplotlib
Requires:       python-numpy
Requires:       python-scipy
Requires:       python-tqdm
BuildArch:      noarch
%python_subpackages

%description
PySwarms is an extensible research toolkit for particle swarm optimization
(PSO) in Python.

It is intended for swarm intelligence researchers, practitioners, and
students who prefer a high-level declarative interface for implementing PSO
in their problems. PySwarms enables basic optimization with PSO and
interaction with swarm optimizations.

%prep
%autosetup -p1 -n pyswarms-%{version}
# Drop the sole Python 2 leftover: replace the "past.builtins.xrange"
# import with an alias to the built-in range, so the dead future/past
# package is not needed.
sed -i 's/^from past.builtins import xrange$/xrange = range/' pyswarms/utils/search/random_search.py
# ... and stop declaring the now-unused "future" runtime dependency
# (setup.py reads install_requires from requirements.in).
sed -i '/^future$/d' requirements.in

%build
%pyproject_wheel

%install
%pyproject_install
# Upstream ships its test suite as a top-level "tests" package; do not
# pollute site-packages with it.
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# %%pyproject_check_import is not provided by openSUSE python-rpm-macros;
# do an equivalent load-time import smoke test instead. scipy loads
# libopenblas.so.0 from the openblas-serial directory, so make sure it is
# on the loader path in the (minimal) check environment.
export LD_LIBRARY_PATH="$(dirname "$(echo %{_prefix}/lib*/openblas-serial/libopenblas.so.0)")"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import pyswarms"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyswarms
%{python_sitelib}/pyswarms-%{version}.dist-info

%changelog
