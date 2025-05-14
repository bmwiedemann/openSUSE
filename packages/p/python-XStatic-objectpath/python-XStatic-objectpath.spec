#
# spec file for package python-XStatic-objectpath
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-XStatic-objectpath
Version:        1.2.1.0
Release:        0
Summary:        AngularJS library "objectpath" repackaged for the XStatic standard
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mike-marcacci/objectpath
Source:         https://files.pythonhosted.org/packages/source/X/XStatic-objectpath/XStatic-objectpath-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Angular JavaScript library packaged for setuptools (easy_install) / pip.
There are otherwise no changes.

You can find more info about the xstatic packaging way in the package `XStatic`.

%prep
%setup -q -n XStatic-objectpath-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt
%dir %{python_sitelib}/xstatic
%dir %{python_sitelib}/xstatic/pkg
%{python_sitelib}/xstatic/pkg/objectpath
%{python_sitelib}/[Xx][Ss]tatic[-_]objectpath-%{version}*-info
%{python_sitelib}/[Xx][Ss]tatic[-_]objectpath-%{version}*nspkg.pth

%changelog
