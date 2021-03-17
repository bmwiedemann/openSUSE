#
# spec file for package python-google-resumable-media
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-google-resumable-media
Version:        0.5.0
Release:        0
Summary:        Utilities for Google Media Downloads and Resumable Uploads
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-resumable-media-python
Source:         https://files.pythonhosted.org/packages/source/g/google-resumable-media/google-resumable-media-%{version}.tar.gz
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Recommends:     python-requests >= 2.18.0
BuildArch:      noarch
%python_subpackages

%description
Utilities for Google Media Downloads and Resumable Uploads

%prep
%setup -q -n google-resumable-media-%{version}

%build
%python_build

%install
%python_install
%{python_expand touch %{buildroot}%{$python_sitelib}/google/__init__.py}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
