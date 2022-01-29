#
# spec file for package python-enrich
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

%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?python_enable_dependency_generator}
Name:           python-enrich
Version:        1.2.7
Release:        0
Summary:        Extends the python-rich library functionality
License:        MIT
URL:            https://github.com/pycontribs/enrich
Source:         https://files.pythonhosted.org/packages/source/e/enrich/enrich-%{version}.tar.gz
Patch0:         remove_setuptools_scm.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Extends the python-rich library functionality
with a set of changes that were not accepted to rich itself.

%prep
%setup -q -n enrich-%{version}
%patch0 -p1
sed -i 's/__VERSION__/%version/' setup.py
sed -i '/_scm/ d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/enrich*

%changelog
