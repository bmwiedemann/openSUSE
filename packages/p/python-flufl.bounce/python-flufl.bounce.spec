#
# spec file for package python-flufl.bounce
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
Name:           python-flufl.bounce
Version:        4.0
Release:        0
Summary:        Email bounce detectors
License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io/en/latest/
# https://gitlab.com/warsaw/flufl.bounce/merge_requests/10
Source0:        https://files.pythonhosted.org/packages/source/f/flufl.bounce/flufl.bounce-%{version}.tar.gz
Source1:        https://gitlab.com/warsaw/flufl.bounce/raw/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       python-zope.interface
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Email bounce detectors.

%prep
%setup -q -n flufl.bounce-%{version}

%build
cp %{SOURCE1} .
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/flufl
%{python_sitelib}/flufl/bounce
%{python_sitelib}/flufl.bounce-*.pth
%{python_sitelib}/flufl.bounce-%{version}*-info

%changelog
