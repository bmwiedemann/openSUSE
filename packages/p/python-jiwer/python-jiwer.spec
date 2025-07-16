#
# spec file for package python-jiwer
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


Name:           python-jiwer
Version:        4.0.0
Release:        0
Summary:        Evaluate your speech-to-text system with similarity measures
License:        Apache-2.0
URL:            https://github.com/jitsi/jiwer
Source:         https://files.pythonhosted.org/packages/source/j/jiwer/jiwer-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click >= 8.1.8}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rapidfuzz >= 3.9.7}
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 8.1.8
Requires:       python-rapidfuzz >= 3.9.7
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
JiWER is a simple and fast python package to evaluate an automatic speech recognition system.
It supports the following measures:

1. word error rate (WER)
2. match error rate (MER)
3. word information lost (WIL)
4. word information preserved (WIP)
5. character error rate (CER)

%prep
%autosetup -p1 -n jiwer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jiwer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative jiwer

%postun
%python_uninstall_alternative jiwer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jiwer
%{python_sitelib}/jiwer
%{python_sitelib}/jiwer-%{version}.dist-info

%changelog
