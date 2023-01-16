#
# spec file for package python-usfm2osis
#
# Copyright (c) 2023 SUSE LLC
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


%define modname usfm2osis
%define baseversion 0.6.1
Name:           python-usfm2osis
Version:        0.6.1+git.1613099315.8fda304
Release:        0
Summary:        Tools for converting Bibles from USFM to OSIS XML
License:        GPL-3.0+
URL:            https://github.com/chrislit/usfm2osis
Source:         %{modname}-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Tools for converting Bibles from USFM to OSIS XML

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/usfm2osis
%python_clone -a %{buildroot}%{_bindir}/usfmtags
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There are no working tests
# (gh#chrislit/usfm2osis#5 ... "improve" is rather generous word)

%post
%python_install_alternative usfm2osis usfmtags

%postun
%python_uninstall_alternative usfm2osis

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/usfm2osis
%python_alternative %{_bindir}/usfmtags
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{baseversion}*-info

%changelog
