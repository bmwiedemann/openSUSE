#
# spec file for package python-plaster
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-plaster
Version:        1.1.2
Release:        0
Summary:        A loader interface around multiple config file formats
License:        MIT
Group:          Development/Languages/Python
URL:            http://docs.pylonsproject.org/projects/plaster/en/latest
# Wheels lack files with problematic noncommercial license
Source:         https://files.pythonhosted.org/packages/py2.py3/p/plaster/plaster-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Plaster is a loader interface around multiple config file formats.
It exists to define a common API for applications to use when they
wish to load a configuration. The library itself does not aim to
handle anything except a basic API that applications may use to find
and load configuration settings. Any specific constraints should be
implemented in a pluggable loader which can be registered via an
entrypoint.

%prep
%setup -q -c -T

%build
# Not Needed

%install
cp -a %{SOURCE0} .
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license %{python_sitelib}/plaster-%{version}.dist-info/LICENSE.txt
%{python_sitelib}/plaster-%{version}.dist-info/
%{python_sitelib}/plaster/

%changelog
