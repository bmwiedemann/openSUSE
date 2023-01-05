#
# spec file for package python-jedi
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


%define skip_python2 1
Name:           python-jedi
Version:        0.18.2
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/davidhalter/jedi
Source0:        https://files.pythonhosted.org/packages/source/j/jedi/jedi-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module parso >= 0.8.0 with %python-parso < 0.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# The author of jedi and parso takes pinning very seriously, adhere to it!
Requires:       (python-parso >= 0.8.0 with python-parso < 0.9)
BuildArch:      noarch
%python_subpackages

%description
Jedi is a static analysis tool for Python that can be used in
IDEs/editors. Its focus is autocompletion and static
analysis.

Jedi has support for two different goto functions. It's possible to
search for related names and to list all names in a Python file and
infer them. Jedi understands docstrings and you can use Jedi
autocompletion in your REPL as well.

Jedi uses an API to connect with IDEs. There is a reference
implementation as a VIM plugin which uses Jedi's autocompletion.

%prep
%autosetup -p1 -n jedi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
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
# https://github.com/davidhalter/jedi/issues/1846
skiptests+=" or (test_completion and conftest and 27)"
skiptests+=" or (test_completion and pytest and 142)"
# This fails on 15.4_py39 server-side but not locally (!?)
skiptests+=" or test_get_default_environment_when_embedded"
%pytest -k "not ($skiptests)"

%files %{python_files}
%doc AUTHORS.txt CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/jedi-%{version}.dist-info
%{python_sitelib}/jedi/

%changelog
