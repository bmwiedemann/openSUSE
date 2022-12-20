#
# spec file for package python-h2
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-h2
Version:        4.1.0
Release:        0
Summary:        HTTP/2 State-Machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/hyper-h2
Source0:        https://files.pythonhosted.org/packages/source/h/h2/h2-%{version}.tar.gz
# Taken from https://github.com/python-hyper/h2/pull/1274
Patch1:         fix-repr-checks-for-py311.patch
BuildRequires:  %{python_module hpack >= 2.3}
BuildRequires:  %{python_module hyperframe >= 6.0}
BuildRequires:  %{python_module hypothesis >= 5.49}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hpack >= 2.3
Requires:       python-hyperframe >= 6.0
BuildArch:      noarch
%python_subpackages

%description
Pure-Python implementation of a HTTP/2 protocol stack.
It's written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

%prep
%autosetup -p1 -n h2-%{version}

echo "
# increase test deadline for slow obs executions
import hypothesis
hypothesis.settings.register_profile(
    'obs',
    deadline=5000,
    suppress_health_check=[hypothesis.HealthCheck.too_slow]
)
" >> test/conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --hypothesis-profile=obs

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/h2
%{python_sitelib}/h2-%{version}*-info

%changelog
