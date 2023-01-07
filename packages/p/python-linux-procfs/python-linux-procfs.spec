#
# spec file for package python-linux-procfs
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-linux-procfs
Version:        0.7.1
Release:        0
Summary:        Linux /proc abstraction classes
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://rt.wiki.kernel.org/index.php/Tuna
Source:         https://cdn.kernel.org/pub/software/libs/python/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pflags
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec bitmasklist_test.py

%post
%python_install_alternative pflags

%postun
%python_uninstall_alternative pflags

%files %{python_files}
%{python_sitelib}/*
%python_alternative %{_bindir}/pflags
%license COPYING

%changelog
