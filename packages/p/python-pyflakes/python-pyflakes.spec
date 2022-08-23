#
# spec file for package python-pyflakes
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-pyflakes
Version:        2.5.0
Release:        0
Summary:        Passive checker of Python programs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/pyflakes
Source:         https://files.pythonhosted.org/packages/source/p/pyflakes/pyflakes-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# the pkg_resources module is required at runtime
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pyflakes is program to analyze Python programs and detect various errors. It
works by parsing the source file, not importing it, so it is safe to use on
modules with side effects. It's also much faster.

%prep
%setup -q -n pyflakes-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pyflakes/
%python_clone -a %{buildroot}%{_bindir}/pyflakes

%check
%pyunittest discover -v

%post
%python_install_alternative pyflakes

%postun
%python_uninstall_alternative pyflakes

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst AUTHORS
%python_alternative %{_bindir}/pyflakes
%{python_sitelib}/pyflakes/
%{python_sitelib}/pyflakes-%{version}-py*.egg-info

%changelog
