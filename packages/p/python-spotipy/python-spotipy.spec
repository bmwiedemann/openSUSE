#
# spec file for package python-spotipy
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-spotipy
Version:        2.4.4
Release:        0
Summary:        Client for the Spotify Web API
License:        MIT
Group:          Development/Languages/Python
Url:            http://spotipy.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/s/spotipy/spotipy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests >= 1.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 1.0
BuildArch:      noarch

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt
%{python_sitelib}/*

%changelog
