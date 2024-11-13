#
# spec file for package python-pytest-recording
#
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


Name:           python-pytest-recording
Version:        0.13.2
Release:        0
Summary:        A pytest plugin that allows you recording of network interactions via VCRpy
License:        MIT
URL:            https://github.com/kiwicom/pytest-recording
Source:         https://github.com/kiwicom/pytest-recording/archive/refs/tags/v%{version}.tar.gz#/pytest-recording-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.5.0}
BuildRequires:  %{python_module vcrpy >= 2.0.1}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-mock}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.5.0
Requires:       python-vcrpy >= 2.0.1
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin that records network interactions in your tests
via VCR.py.

Features
 * Straightforward `pytest.mark.vcr`, that reflects
   `VCR.use_cassettes` API;
 * Combining multiple VCR cassettes
 * Network access blocking;
 * The `rewrite` recording mode that rewrites cassettes
   from scratch.

%prep
%autosetup -p1 -n pytest-recording-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip tests that require a network connection
%pytest -k "not (test_block_network_with_allowed_hosts or test_block_network_with_allowed_hosts or test_block_network_with_allowed_hosts or test_blocked)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_recording
%{python_sitelib}/pytest_recording-%{version}.dist-info

%changelog
