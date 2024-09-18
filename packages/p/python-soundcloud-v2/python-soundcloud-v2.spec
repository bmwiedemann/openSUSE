#
# spec file for package python-soundcloud-v2
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-soundcloud-v2
Version:        1.6.0
Release:        0
Summary:        Python wrapper for the internal v2 SoundCloud API
License:        MIT
URL:            https://github.com/7x11x13/soundcloud.py
Source:         https://files.pythonhosted.org/packages/source/s/soundcloud-v2/soundcloud-v2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dacite >= 1.8.1
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-requests
Suggests:       python-typing_extensions
Suggests:       python-coveralls
Suggests:       python-pdoc
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the internal v2 SoundCloud API. Does not require an API key.

%prep
%autosetup -p1 -n soundcloud-v2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Testsuite requires internet
exit 0

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/soundcloud
%{python_sitelib}/soundcloud_v2-%{version}.dist-info

%changelog
