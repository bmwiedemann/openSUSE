#
# spec file
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


%global modname signedjson
%bcond_without python2
Name:           python-%{modname}
Version:        1.1.4
Release:        0
Summary:        Python module to sign JSON with Ed25519 signatures
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/%{name}
Source0:        https://files.pythonhosted.org/packages/source/s/signedjson/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl >= 0.3.0
Requires:       python-canonicaljson >= 1.0.0
Requires:       python-importlib-metadata
Requires:       python-typing_extensions >= 3.5
Requires:       python-unpaddedbase64 >= 1.0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyNaCl >= 0.3.0}
BuildRequires:  %{python_module canonicaljson >= 1.0.0}
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 3.5}
BuildRequires:  %{python_module unpaddedbase64 >= 1.0.1}
# /SECTION
%if %{with python2}
BuildRequires:  python2-typing >= 3.5
%endif
%ifpython2
Requires:       python-typing >= 3.5
%endif
%python_subpackages

%description
Features:

* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier to
  rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/signedjson
%{python_sitelib}/signedjson-%{version}*-info

%changelog
