#
# spec file for package python-streamdeck
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


Name:           python-streamdeck
Version:        0.9.5
Release:        0
Summary:        Library to control Elgato StreamDeck devices
License:        MIT
URL:            https://github.com/abcminiuser/python-elgato-streamdeck
Source:         https://files.pythonhosted.org/packages/source/s/streamdeck/streamdeck-%{version}.tar.gz
Group:          Development/Languages/Python
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       libhidapi-libusb0
%python_subpackages

%description
Python library to control Elgato StreamDeck devices.

%prep
%setup -q -n streamdeck-%{version}
dos2unix CHANGELOG README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG README.md
%license LICENSE
%{python_sitelib}/StreamDeck*
%{python_sitelib}/streamdeck-%{version}*-info

%changelog
