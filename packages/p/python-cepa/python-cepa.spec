#
# spec file for package python-cepa
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


%{?sle15_python_module_pythons}
Name:           python-cepa
Version:        1.8.4
Release:        0
Summary:        Python controller library for Tor
License:        LGPL-3.0-only
URL:            https://github.com/onionshare/cepa
Source:         https://files.pythonhosted.org/packages/source/c/cepa/cepa-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mock.patch gh#onionshare/cepa#1 mcepl@suse.com
# Replace use of the external mock module with the one in stdlib.
Patch0:         mock.patch
Patch1:         use-fullargspec.patch
Patch2:         fix-assertions.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pycodestyle}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Recommends:     python-cryptography
Provides:       python-stem = %version-%release
Obsoletes:      python-stem < %version-%release

%python_subpackages

%description
Cepa is a fork of stem that adds support for v3 onion client authentication.

Stem is a Python controller library for Tor.
With it you can use Tor's control protocol to script against the Tor process, or build things such as Nyx.

%prep
%autosetup -p1 -n cepa-%{version}
sed -i '/"setuptools >= 65.4.1"/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tor-prompt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python run_tests.py -u
}

%post
%python_install_alternative tor-prompt

%postun
%python_uninstall_alternative tor-prompt

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/tor-prompt
%{python_sitelib}/stem
%{python_sitelib}/cepa-%{version}.dist-info

%changelog
