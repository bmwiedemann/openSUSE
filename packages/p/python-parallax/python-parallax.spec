#
# spec file for package python-parallax
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
Name:           python-parallax
Version:        1.0.8
Release:        0
Summary:        Python module for multi-node SSH command execution and file copy
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/krig/parallax/
Source:         https://files.pythonhosted.org/packages/source/p/parallax/parallax-%{version}.tar.gz
Patch1:         0001-Fix-manager-writer-thread-can-only-be-started-once-b.patch

BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%define oldpython python
Obsoletes:      %{oldpython}-parallax < %{version}
Requires:       openssh
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
%else
Requires(post): %{_sbindir}/update-alternatives
Requires(postun):%{_sbindir}/update-alternatives
%endif
%python_subpackages

%description
Parallax SSH provides an interface to executing commands on multiple
nodes at once using SSH. It also provides commands for sending and receiving files to
multiple nodes using SCP.

%prep
%setup -q -n parallax-%{version}
%patch1 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/parallax-askpass

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative parallax-askpass

%postun
%python_uninstall_alternative parallax-askpass

%files %{python_files}
%doc AUTHORS README.md
%license COPYING
%{python_sitelib}/parallax
%{python_sitelib}/parallax-%{version}*.egg-info
%python_alternative %{_bindir}/parallax-askpass

%changelog
