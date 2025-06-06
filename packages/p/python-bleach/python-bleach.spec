#
# spec file for package python-bleach
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


%{?sle15_python_module_pythons}
Name:           python-bleach
Version:        6.2.0
Release:        0
Summary:        A whitelist-based HTML-sanitizing tool
License:        Apache-2.0
URL:            https://github.com/jsocol/bleach
Source:         https://files.pythonhosted.org/packages/source/b/bleach/bleach-%{version}.tar.gz
Patch0:         de-vendor.patch
# https://github.com/mozilla/bleach/pull/706
Patch1:         strip-spaces.patch
BuildRequires:  %{python_module html5lib >= 1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-html5lib >= 1.1
Requires:       python-webencodings
BuildArch:      noarch
%python_subpackages

%description
Bleach is an HTML sanitation library that escapes or strips markup and
attributes based on a white list. Bleach can also linkify text safely, applying
filters that Django's ``urlize`` filter cannot, and optionally setting ``rel``
attributes, even on links already in the text.

Bleach is intended for sanitizing text from *untrusted* sources.

Because it relies on html5lib, Bleach is as good as modern browsers at dealing
with weird, quirky HTML fragments. Bleach's methods will fix
unbalanced or mis-nested tags.

Documentation is at http://bleach.readthedocs.org/ .

%prep
%autosetup -p1 -n bleach-%{version}
rm -rf bleach/_vendor

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#mozilla/bleach#503
%pytest -k 'not test_uri_value_allowed_protocols'

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/bleach
%{python_sitelib}/bleach-%{version}*-info

%changelog
