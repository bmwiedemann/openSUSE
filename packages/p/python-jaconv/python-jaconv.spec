#
# spec file for package python-jaconv
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define pyname jaconv
Name:           python-%{pyname}
Version:        0.5.0
Release:        0
Summary:        Kana kanji simple inversion library
License:        MIT
URL:            https://github.com/ikegami-yukino/%{pyname}
Source:         https://files.pythonhosted.org/packages/source/j/%{pyname}/%{pyname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jaconv (Japanese Converter) is interconverter for Hiragana,
Katakana, Hankaku (half-width character) and Zenkaku (full-width character)

%prep
%autosetup -n %{pyname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst README_JP.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/%{pyname}
%{python_sitelib}/%{pyname}-%{version}.dist-info

%changelog
