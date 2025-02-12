#
# spec file for package python-stripe
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


Name:           python-stripe
Version:        11.5.0
Release:        0
Summary:        Python bindings for the Stripe API
License:        MIT
URL:            https://github.com/stripe/stripe-python
Source:         https://files.pythonhosted.org/packages/source/s/stripe/stripe-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp >= 3.9.4}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-mock >= 2.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typing_extensions >= 4.5.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  stripe-mock
Requires:       python-requests >= 2.20
Requires:       python-typing_extensions >= 4.5.0
Conflicts:      python-stripe-api
BuildArch:      noarch
%python_subpackages

%description
Python bindings for the Stripe API.

%prep
%autosetup -p1 -n stripe-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
stripe-mock &
pid=$!
# Raises invalid request
donttest="test_terminal_readers_process_setup_intent_post "
# Requires network
donttest+="or TestLiveHTTPClients or test_async_raw_request_timeout"
%pytest -k "not ($donttest)"
kill $pid

%files %{python_files}
%doc CHANGELOG.md README.md examples/
%license LICENSE
%{python_sitelib}/stripe
%{python_sitelib}/stripe-%{version}.dist-info

%changelog
