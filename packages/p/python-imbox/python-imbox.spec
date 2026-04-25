#
# spec file for package python-imbox
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-imbox
Version:        0.10.1
Release:        0
Summary:        Python IMAP for Human beings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/martinrusev/imbox
Source:         https://github.com/martinrusev/imbox/archive/refs/tags/%{version}.tar.gz#/imbox-%{version}-gh.tar.gz
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Python library for reading IMAP mailboxes and converting email content to machine readable data

%prep
%setup -q -n imbox-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/imbox
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative imbox

%post
%python_install_alternative imbox

%postun
%python_uninstall_alternative imbox

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/imbox
%{python_sitelib}/imbox
%{python_sitelib}/imbox-%{version}*-info

%changelog
