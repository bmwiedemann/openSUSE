#
# spec file for package python-avro
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-avro
Version:        1.9.2
Release:        0
Summary:        A serialization and RPC framework for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://avro.apache.org/
Source:         https://files.pythonhosted.org/packages/source/a/avro/avro-%{version}.tar.gz
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-python-snappy
BuildArch:      noarch
%python_subpackages

%description
Avro is a serialization and RPC framework.

%prep
%setup -q -n avro-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/avro
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Dies on which is nowhere even in their VCS
#  E   ImportError: No module named set_avro_test_path
#%%pytest

%post
%python_install_alternative avro

%postun
%python_uninstall_alternative avro

%files %{python_files}
%python_alternative %{_bindir}/avro
%{python_sitelib}/*

%changelog
