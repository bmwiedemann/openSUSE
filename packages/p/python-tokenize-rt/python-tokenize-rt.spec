#
# spec file for package python-tokenize_rt
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tokenize-rt
Version:        4.0.0
Release:        0
License:        MIT
Summary:        A wrapper around the stdlib `tokenize` which roundtrips
Url:            https://github.com/asottile/tokenize-rt
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/t/tokenize-rt/tokenize_rt-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch

%python_subpackages

%description
A wrapper around the stdlib `tokenize` which roundtrips.

%prep
%setup -q -n tokenize_rt-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tokenize-rt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative tokenize-rt

%postun
%python_uninstall_alternative tokenize-rt

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/tokenize-rt
%{python_sitelib}/*

%changelog
