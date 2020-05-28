#
# spec file for package python-flit
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-flit
Version:        1.3
Release:        0
Summary:        Packaging tool for simple packages
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/takluyver/flit
Source:         https://files.pythonhosted.org/packages/source/f/flit/flit-%{version}.tar.gz
Patch0:         https://github.com/takluyver/flit/commit/6a6b7ff.patch#/merged_pr_278.patch
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest >= 2.7.3}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module requests-download}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testpath}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils
Requires:       python-pytoml
Requires:       python-requests-download
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{python3_version_nodots} < 36
BuildRequires:  %{python_module zipfile36}
%endif
%if %{python3_version_nodots} < 36
Requires:       python-zipfile36
%endif
%python_subpackages

%description
A simple packaging tool for simple packages.

%prep
%setup -q -n flit-%{version}
%patch0 -p1
sed -i 's/distutils.core/setuptools/' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/flit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_build_sdist is https://github.com/takluyver/flit/issues/133
# test_invalid_classifier requires internet
%pytest -k 'not (test_build_sdist or test_invalid_classifier)'

%post
%python_install_alternative flit

%postun
%python_uninstall_alternative flit

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/flit
%{python_sitelib}/*

%changelog
