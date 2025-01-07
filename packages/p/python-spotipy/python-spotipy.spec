#
# spec file for package python-spotipy
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
Name:           python-spotipy
Version:        2.25.0
Release:        0
Summary:        Client for the Spotify Web API
License:        MIT
URL:            https://spotipy.readthedocs.org/
# https://github.com/plamere/spotipy/issues/454
Source:         https://github.com/plamere/spotipy/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-redis >= 3.5.3
Requires:       python-requests >= 2.25.0
Requires:       python-urllib3 >= 1.26.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
# /SECTION
%python_subpackages

%description
Spotipy is a Python library for the Spotify Web API.
With Spotipy, the user gets access to the music data
provided by the Spotify platform.

Documentation is available at
https://spotipy.readthedocs.io/

%prep
%setup -q -n spotipy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit/ -k 'not credentials_get_access_token'

%files %{python_files}
%license LICENSE.md
%doc CHANGELOG.md
%{python_sitelib}/spotipy
%{python_sitelib}/spotipy-*-info

%changelog
