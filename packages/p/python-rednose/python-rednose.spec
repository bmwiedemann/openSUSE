#
# spec file for package python-rednose
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Weberhofer GmbH, Austria
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
Name:           python-rednose
Version:        1.3.0
Release:        0
Summary:        Pretty output formatter for python-nosetests
License:        MIT
Group:          Development/Languages/Python
Url:            https://pypi.python.org/pypi/rednose/
Source0:        https://files.pythonhosted.org/packages/source/r/rednose/rednose-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama
Requires:       python-nose
Requires:       python-termstyle
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Rednose is a nosetests plugin for adding colour (and readability) to nosetest console results.

%prep
%setup -q -n rednose-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
