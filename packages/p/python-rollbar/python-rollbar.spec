#
# spec file for package python-rollbar
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


Name:           python-rollbar
Version:        1.0.0
Release:        0
Summary:        Report exceptions, errors, and log messages to Rollbar
License:        MIT
URL:            https://github.com/rollbar/pyrollbar
Source:         https://github.com/rollbar/pyrollbar/archive/v%{version}.tar.gz
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 0.12.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.14.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 0.12.1
Requires:       python-setuptools
Requires:       python-six >= 1.14.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Send messages and exceptions with arbitrary context, get back aggregates, and debug production issues quickly.

%prep
%autosetup -p1 -n pyrollbar-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rollbar
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_shorten_array or test_encode_empty_tuple)'

%post
%python_install_alternative rollbar

%postun
%python_uninstall_alternative rollbar

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/rollbar
%{python_sitelib}/rollbar
%{python_sitelib}/rollbar-%{version}*-info

%changelog
