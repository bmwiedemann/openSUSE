#
# spec file for package python-charset-normalizer
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-charset-normalizer
Version:        3.4.2
Release:        0
Summary:        Python Universal Charset detector
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source:         https://github.com/Ousret/charset_normalizer/archive/refs/tags/%{version}.tar.gz#/charset_normalizer-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Suggests:       python-unicodedata2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python Universal Charset detector.

%prep
%setup -q -n charset_normalizer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/normalizer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative normalizer

%post
%python_install_alternative normalizer

%postun
%python_uninstall_alternative normalizer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/normalizer
%{python_sitelib}/charset_normalizer
%{python_sitelib}/charset_normalizer-%{version}*-info

%changelog
