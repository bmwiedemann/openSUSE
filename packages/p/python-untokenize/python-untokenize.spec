#
# spec file for package python-untokenize
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-untokenize
Version:        0.1.1
Release:        0
Summary:        Python module to transform tokens into original source code
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/myint/untokenize
Source:         https://files.pythonhosted.org/packages/source/u/untokenize/untokenize-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Untokenize transforms tokens into source code. Unlike the standard library's
tokenize.untokenize(), it preserves the original whitespace between tokens.

%prep
%setup -q -n untokenize-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_untokenize.py

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
