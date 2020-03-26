#
# spec file for package python-jedi
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
Name:           python-jedi
Version:        0.16.0+git55.17b3611c
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/davidhalter/jedi
Source0:        jedi-%{version}.tar.xz
Patch0:         unbundle.patch
BuildRequires:  %{python_module parso >= 0.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-typeshed
Requires:       python-parso >= 0.5.0
Requires:       python-typeshed
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
%setup -q -n jedi-%{version}
%patch0 -p1
rm -Rf jedi/third_party

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export LANG="en_US.UTF-8"
# Do not execute tests
# Reason here is that the upstream uses bundled typeshed of exact revision and we can't guarantee that
# Something like 20-30 tests always break with any typeshed change, and as such we can't do much
# %%pytest -k "not (test_venv_and_pths or test_completion or test_builtin_details or test_static_analysis or test_os_path_join or test_import or test_compiled_signature or test_module__file__ or test_sqlite3_conversion)"

%files %{python_files}
%doc AUTHORS.txt CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/jedi-*-py*.egg-info
%{python_sitelib}/jedi/

%changelog
