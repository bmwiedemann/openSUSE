#
# spec file for package python-eradicate
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
Name:           python-eradicate
Version:        1.0
Release:        0
Summary:        Python utility for removing commented-out code
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/myint/eradicate
Source:         https://files.pythonhosted.org/packages/source/e/eradicate/eradicate-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/myint/eradicate/v%{version}/test_eradicate.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
With modern revision control available, there is no reason to save
commented-out code to your repository. "eradicate" helps cleans up
existing junk comments. It does this by detecting block comments that
contain valid Python syntax that are likely to be commented out code.
(It avoids false positives like the sentence "this is not good",
which is valid Python syntax, but is probably not code.)

%prep
%setup -q -n eradicate-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/eradicate

%post
%python_install_alternative eradicate

%postun
%python_uninstall_alternative eradicate

%check
export PYTHONPATH=.
%python_exec %{SOURCE1}

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/eradicate
%{python_sitelib}/*

%changelog
