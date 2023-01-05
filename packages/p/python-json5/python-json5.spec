#
# spec file for package python-json5
#
# Copyright (c) 2023 SUSE LLC
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


#
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-json5
Version:        0.9.12
Release:        0
Summary:        A Python implementation of the JSON5 data format
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/dpranke/pyjson5
Source:         https://github.com/dpranke/pyjson5/archive/v%{version}.tar.gz#/pyjson5-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-setuptools
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of the JSON5 data format.

JSON5 extends the JSON data interchange format to make it
slightly more usable as a configuration language:

  * JavaScript-style comments (both single and multi-line) are legal.
  * Object keys may be unquoted if they are legal ECMAScript identifiers
  * Objects and arrays may end with trailing commas.
  * Strings can be single-quoted, and multi-line string literals are allowed.

%prep
%setup -q -n pyjson5-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyjson5
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pyjson5

%post
%python_install_alternative pyjson5

%postun
%python_uninstall_alternative pyjson5

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyjson5
%{python_sitelib}/*

%changelog
