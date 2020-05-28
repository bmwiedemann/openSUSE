#
# spec file for package python-num2words
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
Name:           python-num2words
Version:        0.5.10
Release:        0
Summary:        Modules to convert numbers to words
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/savoirfairelinux/num2words
Source:         https://files.pythonhosted.org/packages/source/n/num2words/num2words-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docopt >= 0.6.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module delegator.py}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
num2words is a library that converts numbers like "42" to words like "forty-two".
It supports multiple languages and can even generate ordinal numbers like "forty-second"
(although this last feature is a bit buggy for some languages at the moment).

%prep
%setup -q -n num2words-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/num2words
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_cli.py has 'python' command hardcoded
%pytest -k "not test_cli" tests

%post
%python_install_alternative num2words

%postun
%python_uninstall_alternative num2words

%files %{python_files}
%doc CHANGES.rst README.rst
%license COPYING
%{python_sitelib}/*
%python_alternative %{_bindir}/num2words

%changelog
