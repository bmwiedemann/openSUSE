#
# spec file for package python-parso
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-parso
Version:        0.8.3
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
URL:            https://github.com/davidhalter/parso
Source0:        https://files.pythonhosted.org/packages/source/p/parso/parso-%{version}.tar.gz
Patch1:         https://github.com/davidhalter/parso/commit/cf5969d7a109798adbf9538d70e92138f077d700.patch
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python
versions). Parso is also able to list multiple syntax errors in your
python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax
tree.

%prep
%autosetup -p1 -n parso-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Python 3.10 has deviating exception messages -- gh#davidhalter/parso#192
python310_args=("-k" "not test_python_exception_matches")
%pytest "${$python_args[@]}"

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt CHANGELOG.rst README.rst
%{python_sitelib}/parso-%{version}-py*.egg-info
%{python_sitelib}/parso/

%changelog
