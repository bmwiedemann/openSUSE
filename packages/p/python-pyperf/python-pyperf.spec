#
# spec file for package python-pyperf
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pyperf
Version:        2.7.0
Release:        0
Summary:        Python module to run and analyze benchmarks
License:        MIT
URL:            https://github.com/vstinner/pyperf
Source:         https://files.pythonhosted.org/packages/source/p/pyperf/pyperf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-psutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python module to run and analyze benchmarks.

%prep
%setup -q -n pyperf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyperf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pyperf

%postun
%python_uninstall_alternative pyperf

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/pyperf
%{python_sitelib}/*

%changelog
