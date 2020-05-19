#
# spec file for package python-ptr
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
Name:           python-ptr
Version:        20.2.26
Release:        0
Summary:        Parallel asyncio Python setup(cfg|py) test runner
License:        MIT
URL:            https://github.com/facebookincubator/ptr
Source:         https://files.pythonhosted.org/packages/source/p/ptr/ptr-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Conflicts on site-packages/ptr.py
Conflicts:      python-pytest-runner
BuildArch:      noarch
%python_subpackages

%description
Parallel asyncio Python setup.(cfg|py) test runner.

%prep
%setup -q -n ptr-%{version}
sed -i 's/test_config/_test_config/' ptr_tests.py
sed -i '1{/^#!/d}' *.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ptr
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python %{buildroot}%{_bindir}/ptr --help
%python_exec setup.py test

%post
%python_install_alternative ptr

%postun
%python_uninstall_alternative ptr

%files %{python_files}
%doc CHANGES.md README.md
%python_alternative %{_bindir}/ptr
%{python_sitelib}/*

%changelog
