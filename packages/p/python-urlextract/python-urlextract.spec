#
# spec file for package python-urlextract
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
%define skip_python2 1
Name:           python-urlextract
Version:        0.14.0
Release:        0
Summary:        Collects and extracts URLs from given text
License:        MIT
URL:            https://github.com/lipoja/URLExtract
Source:         https://github.com/lipoja/URLExtract/archive/v%{version}.tar.gz#/urlextract-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires:       python-idna
Requires:       python-uritools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uritools}
# /SECTION
%python_subpackages

%description
Collects and extracts URLs from given text.

%prep
%setup -q -n URLExtract-%{version}
sed -i '1{/^#!/d}' urlextract/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/urlextract
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative urlextract

%postun
%python_uninstall_alternative urlextract

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/urlextract
%{python_sitelib}/*

%changelog
