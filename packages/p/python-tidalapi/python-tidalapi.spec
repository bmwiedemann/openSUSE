#
# spec file for package python-tidalapi
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


%{?sle15_python_module_pythons}
Name:           python-tidalapi
Version:        0.8.11
Release:        0
Summary:        Unofficial API for the TIDAL music streaming service
License:        LGPL-3.0-or-later
URL:            https://github.com/EbbLabs/python-tidal
Source:         https://files.pythonhosted.org/packages/source/t/tidalapi/tidalapi-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module isodate >= 0.7.2}
BuildRequires:  %{python_module mpegdash >= 0.4.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyaes >= 1.6.1}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module ratelimit >= 2.2.1}
BuildRequires:  %{python_module requests >= 2.32.3}
BuildRequires:  %{python_module typing_extensions >= 4.12.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-isodate >= 0.7.2
Requires:       python-mpegdash >= 0.4.1
Requires:       python-pyaes >= 1.6.1
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-ratelimit >= 2.2.1
Requires:       python-requests >= 2.32.3
Requires:       python-typing_extensions >= 4.12.2
BuildArch:      noarch
%python_subpackages

%description
Unofficial Python API for TIDAL, a music streaming service. It supports
OAuth login, browsing albums, artists, playlists and mixes, and
retrieving stream URLs and DASH manifests.

%prep
%autosetup -p1 -n tidalapi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The upstream test suite logs in to a TIDAL account and is not in the
# sdist, so only check that the module imports
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import tidalapi; print(tidalapi.__version__)"

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/tidalapi
%{python_sitelib}/tidalapi-%{version}.dist-info

%changelog
