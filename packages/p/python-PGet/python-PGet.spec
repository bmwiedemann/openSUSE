#
# spec file for package python-PGet
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


Name:           python-PGet
Version:        0.5.1
Release:        0
License:        Apache-2.0
Summary:        Download tool using chunks
URL:            https://github.com/halilozercan/pget
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/P/PGet/PGet-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.20.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
Requires(post): alts
Requires(postun): alts

%python_subpackages

%description
A tool and library to save large files by creating multiple connections.

%prep
%setup -q -n PGet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pget

%post
%python_install_alternative pget

%postun
%python_uninstall_alternative pget

%files %{python_files}
%python_alternative %{_bindir}/pget
%{python_sitelib}/pget
%{python_sitelib}/[Pp][Gg]et-%{version}*dist-info

%changelog
