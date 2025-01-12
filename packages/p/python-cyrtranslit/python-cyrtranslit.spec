#
# spec file for package python-cyrtranslit
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


Name:           python-cyrtranslit
Version:        1.1.1
Release:        0
Summary:        Bi-directional Cyrillic transliteration.
License:        MIT
URL:            https://github.com/opendatakosovo/cyrillic-transliteration
Source:         https://files.pythonhosted.org/packages/source/c/cyrtranslit/cyrtranslit-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Bi-directional Cyrillic transliteration. Transliterate Cyrillic script to Latin script and vice versa. Supports transliteration for Bulgarian, Montenegrin, Macedonian, Mongolian, Russian, Serbian, Tajik, and Ukrainian.

%prep
%autosetup -p1 -n cyrtranslit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cyrtranslit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no unittests, just text files in cyrilic

%post
%python_install_alternative cyrtranslit

%postun
%python_uninstall_alternative cyrtranslit

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/cyrtranslit
%{python_sitelib}/cyrtranslit
%{python_sitelib}/cyrtranslit-%{version}.dist-info

%changelog
