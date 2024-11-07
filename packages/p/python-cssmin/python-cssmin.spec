#
# spec file for package python-cssmin
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


Name:           python-cssmin
Version:        0.2.0
Release:        0
Summary:        YUI CSS compression algorithm
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/zacharyvoase/cssmin
Source:         https://files.pythonhosted.org/packages/source/c/cssmin/cssmin-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a Python port of the YUI CSS Compressor.

%prep
%autosetup -p1 -n cssmin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/cssmin.py
sed -i "s|^#!.*env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/cssmin.py
}
%python_clone -a %{buildroot}%{_bindir}/cssmin
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Good upstream have never even heard about the idea of tests

%post
%python_install_alternative cssmin

%postun
%python_uninstall_alternative cssmin

%files %{python_files}
%python_alternative %{_bindir}/cssmin
%{python_sitelib}/cssmin.py
%{python_sitelib}/cssmin-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
