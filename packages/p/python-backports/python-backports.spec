#
# spec file for package python-backports
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
Name:           python-backports
Version:        1.0.0
Release:        0
Summary:        Namespace for backported Python features
License:        MIT
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/backports/
Source0:        __init__.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a common package that backports using the "backports" namespace
must depend on to avoid conflicts.  You shouldn't install this directly,
packages that require this will pultll it in automatically.

Please see these links for more details:
    https://pypi.python.org/pypi/backports/
    https://www.python.org/dev/peps/pep-0420/\%%23namespace-packages-today

If your package provides a module in the %%{python_sitelib}/backports
folder, please depend on this and delete any existing 
%%{python_sitelib}/backports/__init__.py file provided by that package.
configparser.

%prep
# Not needed

%build
# Not needed

%install
%{python_expand mkdir -p %{buildroot}%{$python_sitelib}/backports/
cp %{SOURCE0} %{buildroot}%{$python_sitelib}/backports/
%if 0%{?suse_version} >= 1320
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/backports/__init__.py
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/backports/__init__.py
%endif
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%defattr(-,root,root,-)
%dir %{python_sitelib}/backports/
%{python_sitelib}/backports/__init__.py*
%if 0%{?suse_version} >= 1320
%pycache_only %dir %{python_sitelib}/backports/__pycache__/
%pycache_only %{python_sitelib}/backports/__pycache__/__init__.*py*
%endif

%changelog
