#
# spec file for package python-Morfessor
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
Name:           python-Morfessor
Version:        2.0.6
Release:        0
Summary:        Unsupervised and semi-supervised morphological segmentation
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/aalto-speech/morfessor
Source:         https://files.pythonhosted.org/packages/source/M/Morfessor/Morfessor-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Morfessor is a tool for unsupervised and semi-supervised
morphological segmentation

%prep
%setup -q -n Morfessor-%{version}
sed -i -e '/^#!\//, 1d' morfessor/__init__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/morfessor-train
%python_clone -a %{buildroot}%{_bindir}/morfessor-segment
%python_clone -a %{buildroot}%{_bindir}/morfessor-evaluate
%python_clone -a %{buildroot}%{_bindir}/morfessor
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python morfessor/test/evaluation.py
}

%post
%python_install_alternative morfessor-train
%python_install_alternative morfessor-segment
%python_install_alternative morfessor-evaluate
%python_install_alternative morfessor

%postun
%python_uninstall_alternative morfessor-train
%python_uninstall_alternative morfessor-segment
%python_uninstall_alternative morfessor-evaluate
%python_uninstall_alternative morfessor

%files %{python_files}
%doc README
%license LICENSE
%python_alternative %{_bindir}/morfessor
%python_alternative %{_bindir}/morfessor-evaluate
%python_alternative %{_bindir}/morfessor-segment
%python_alternative %{_bindir}/morfessor-train
%{python_sitelib}/*

%changelog
