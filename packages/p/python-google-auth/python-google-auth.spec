#
# spec file for package python-google-auth
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-google-auth
Version:        1.6.3
Release:        0
Summary:        Google Authentication Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python
Source:         https://files.pythonhosted.org/packages/source/g/google-auth/google-auth-%{version}.tar.gz
Patch0:         pytest5.patch
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module cachetools}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oauth2client-gce}
BuildRequires:  %{python_module oauth2client}
BuildRequires:  %{python_module pyasn1-modules}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cachetools
Requires:       python-cryptography
Requires:       python-oauth2client
Requires:       python-oauth2client-gce
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-requests
Requires:       python-rsa
Requires:       python-setuptools
Requires:       python-six
Requires:       python-urllib3
BuildArch:      noarch
%python_subpackages

%description
This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.

%prep
%setup -q -n google-auth-%{version}
%patch0 -p1

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
%{python_sitelib}/*

%changelog
