#
# spec file for package python-colorlog
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
Name:           python-colorlog
Version:        4.2.1
Release:        0
Summary:        Log formatting with colors
License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source:         https://files.pythonhosted.org/packages/source/c/colorlog/colorlog-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
colorlog.ColoredFormatter is a formatter for use with Python's logging module.
It allows colors to be placed in the format string, which is mostly useful
when paired with a StreamHandler that is outputting to a terminal.
This is accomplished by added a set of terminal color codes to the record
before it is used to format the string.

%prep
%setup -q -n colorlog-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest colorlog/tests/

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/colorlog
%{python_sitelib}/colorlog-%{version}-py%{python_version}.egg-info

%changelog
