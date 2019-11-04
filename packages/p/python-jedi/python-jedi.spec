#
# spec file for package python-jedi
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
Name:           python-jedi
Version:        0.15.1
Release:        0
Summary:        An autocompletion tool for Python
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/davidhalter/jedi
Source0:        https://files.pythonhosted.org/packages/source/j/jedi/jedi-%{version}.tar.gz
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
# in OBS venv isn't working and builtin completion tests dont work with unbundled typeshed
# test_static_analysis is flaky
# test_os_path_join is time based
# test_import gh#davidhalter/jedi#1429
%pytest -k "not (test_venv_and_pths or test_completion or test_builtin_details or test_static_analysis or test_os_path_join or test_import)"

%files %{python_files}
%doc AUTHORS.txt CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/jedi-%{version}-py*.egg-info
%{python_sitelib}/jedi/

%changelog
