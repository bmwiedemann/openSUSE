#
# spec file for package python-PGet
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-PGet
Version:        0.5.1
Release:        0
License:        Apache-2.0
Summary:        Download tool using chunks
URL:            https://github.com/halilozercan/pget
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/P/PGet/PGet-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.20.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives

%python_subpackages

%description
A tool and library to save large files by creating multiple connections.

%prep
%setup -q -n PGet-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pget

%post
%python_install_alternative pget

%postun
%python_uninstall_alternative pget

%files %{python_files}
%python_alternative %{_bindir}/pget
%{python_sitelib}/*

%changelog
