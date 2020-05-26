#
# spec file for package python-padatious
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-padatious
Version:        0.4.7
Release:        0
Summary:        A neural network intent parser
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/padatious
# https://github.com/MycroftAI/padatious/issues/14
Source:         https://github.com/MycroftAI/padatious/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-fann2
Requires:       python-padaos
Requires:       python-setuptools
Requires:       python-xxhash
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fann2}
BuildRequires:  %{python_module padaos}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xxhash}
# /SECTION
%python_subpackages

%description
A neural network intent parser used by the Mycroft AI

%prep
%setup -q -n padatious-%{version}
chmod 644 LICENSE

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/padatious
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/MycroftAI/padatious/issues/15
%pytest -k 'not test_train_timeout_subprocess'

%post
%python_install_alternative padatious

%postun
%python_uninstall_alternative padatious

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/padatious

%changelog
