#
# spec file for package python-pyusb
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


Name:           python-pyusb
Version:        1.3.1
Release:        0
Summary:        USB access on the Python language
# URL is incorrect on PyPI, gh#pyusb/pyusb#211
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyusb/pyusb
Source:         https://files.pythonhosted.org/packages/source/p/pyusb/pyusb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libusb-1_0-0
BuildArch:      noarch
Provides:       python-usb = %{version}-%{release}
Obsoletes:      python-usb < %{version}-%{release}
%python_subpackages

%description
Provides USB access to the Python language.

%prep
%setup -q -n pyusb-%{version}
# Convert dos format files to unix format
find .  -name "*.rst" -exec dos2unix {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Testing mostly requires a device, which is not mocked or emulated
# See https://github.com/pyusb/pyusb/issues/235
%pytest tests/test_find.py tests/test_util.py -k 'not FindDescriptorTest'

%files %{python_files}
%license LICENSE
%doc ACKNOWLEDGEMENTS README.rst docs/*
%{python_sitelib}/usb
%{python_sitelib}/pyusb-%{version}*info

%changelog
