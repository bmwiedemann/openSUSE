#
# spec file for package python-gsm0338
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-gsm0338
Version:        1.0.0
Release:        0
Summary:        Python Codec for 3GPP TS 23.038 / ETSI GSM 03.38
License:        MIT
URL:            https://github.com/dsch/gsm0338
#GIT-Clone:     https://github.com/dsch/gsm0338.git
Source:         https://github.com/dsch/gsm0338/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python Codec for 3GPP TS 23.038 / ETSI GSM 03.38.
The codec implements the encoding and decoding methods in the
stateless codecs.Codec class. With loading the module the
codec get's automatically registered.

%prep
%setup -q -n gsm0338-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/gsm0338
%{python_sitelib}/gsm0338-%{version}*-info

%changelog
