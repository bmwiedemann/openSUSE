#
# spec file for package python-langdetect
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


%{?sle15_python_module_pythons}
Name:           python-langdetect
Version:        1.0.9
Release:        0
Summary:        Language detection library ported from Google's language-detection
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Mimino666/langdetect
Source:         https://files.pythonhosted.org/packages/source/l/langdetect/langdetect-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
python-langdetect is a port of Google's language-detection library to Python.
It supports 55 languages out of the box:
af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw

%prep
%setup -q -n langdetect-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/langdetect
%{python_sitelib}/langdetect-%{version}*-info

%changelog
