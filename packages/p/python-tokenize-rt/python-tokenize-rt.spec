#
# spec file for package python-tokenize-rt
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


Name:           python-tokenize-rt
Version:        6.1.0
Release:        0
Summary:        A wrapper around the stdlib `tokenize` which roundtrips
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asottile/tokenize-rt
Source:         https://github.com/asottile/tokenize-rt/archive/refs/tags/v{%{version}}.tar.gz#/tokenize-rt-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A wrapper around the stdlib `tokenize` which roundtrips.

%prep
%setup -q -n tokenize-rt-%{version}

%build
%python_build

%install
%python_install
%{python_clone -a %{buildroot}%{_bindir}/tokenize-rt}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative tokenize-rt

%postun
%python_uninstall_alternative tokenize-rt

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/tokenize-rt
%{python_sitelib}/tokenize_rt*
%{python_sitelib}/__pycache__/tokenize_rt*
%{python_sitelib}/tokenize_rt-%{version}*-info

%changelog
