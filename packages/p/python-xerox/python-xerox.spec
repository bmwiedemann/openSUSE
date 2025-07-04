#
# spec file for package python-xerox
#
# Copyright (c) 2025 SUSE LLC
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


#%%define skip_python2 1
Name:           python-xerox
Version:        0.4.1
Release:        0
Summary:        Simple Copy + Paste in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kennethreitz/xerox
Source:         https://files.pythonhosted.org/packages/source/x/xerox/xerox-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xclip
BuildRequires:  xvfb-run
Requires:       xclip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python copy and paste library supporting OS X, X11 (Linux, BSD, etc.), and Windows.

%prep
%setup -q -n xerox-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/xerox
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand xvfb-run $python -m pytest

%post
%python_install_alternative xerox

%postun
%python_uninstall_alternative xerox

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/xerox
%{python_sitelib}/xerox
%{python_sitelib}/xerox-%{version}.dist-info

%changelog
