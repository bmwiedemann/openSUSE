#
# spec file for package python-pixelmatch
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-pixelmatch
Version:        0.4.0
Release:        0
Summary:        A pixel-level image comparison library
License:        ISC
URL:            https://pypi.org/project/pixelmatch/
Source:         https://files.pythonhosted.org/packages/source/p/pixelmatch/pixelmatch-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A fast pixel-level image comparison library, originally created to compare
screenshots in tests.  Now with additional support of PIL.Image instances
Python port of https://github.com/mapbox/pixelmatch.

mismatch = pixelmatch(img_a, img_b, width, height, data_diff, includeAA=True)
```

%prep
%autosetup -p1 -n pixelmatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE LICENSE
%{python_sitelib}/pixelmatch
%{python_sitelib}/pixelmatch-%{version}.dist-info

%changelog
