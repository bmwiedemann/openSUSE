#
# spec file for package python-urlextract
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


Name:           python-urlextract
Version:        1.9.0
Release:        0
Summary:        Collects and extracts URLs from given text
License:        MIT
URL:            https://github.com/lipoja/URLExtract
Source:         https://github.com/lipoja/URLExtract/archive/v%{version}.tar.gz#/urlextract-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
Requires:       python-filelock
Requires:       python-idna
Requires:       python-platformdirs
Requires:       python-uritools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module filelock}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module platformdirs}
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/urlextract
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_dns'
find %{buildroot} -name tlds-alpha-by-domain.txt.lock -delete # avoid modification of build results by tests

%post
%python_install_alternative urlextract

%postun
%python_uninstall_alternative urlextract

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/urlextract
%{python_sitelib}/urlextract
%{python_sitelib}/urlextract-%{version}.dist-info

%changelog
