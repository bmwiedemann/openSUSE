#
# spec file for package python-jedi
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-jedi
Version:        0.18.1
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/davidhalter/jedi
Source0:        https://files.pythonhosted.org/packages/source/j/jedi/jedi-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module parso >= 0.8.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-parso >= 0.8.0
BuildArch:      noarch
%python_subpackages

%description
Jedi is a static analysis tool for Python that can be used in
IDEs/editors. Its focus is autocompletion and static
analysis.

Jedi has support for two different goto functions. It’s possible to
search for related names and to list all names in a Python file and
infer them. Jedi understands docstrings and you can use Jedi
autocompletion in your REPL as well.

Jedi uses an API to connect with IDEs. There is a reference
implementation as a VIM plugin which uses Jedi's autocompletion.

%prep
%autosetup -p1 -n jedi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF-8"
skiptests="test_venv_and_pths"
skiptests+=" or test_sqlite3_conversion"
# some architectures are too slow for these optimizer devel checks
skiptests+=" or test_speed"
# fails on some architectures
skiptests+=" or test_init_extension_module"
# https://github.com/davidhalter/jedi/issues/1824
skiptests+=" or (test_completion and lambdas and 112)"
%pytest -k "not ($skiptests)"

%files %{python_files}
%doc AUTHORS.txt CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/jedi-*-py*.egg-info
%{python_sitelib}/jedi/

%changelog
