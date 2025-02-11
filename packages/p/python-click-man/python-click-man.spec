#
# spec file for package python-click-man
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


%{?sle15_python_module_pythons}
Name:           python-click-man
Version:        0.5.0
Release:        0
Summary:        Automate generation of man pages for python click applications
License:        MIT
URL:            https://github.com/click-contrib/click-man
Source:         https://files.pythonhosted.org/packages/source/c/click_man/click_man-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Automate generation of man pages for Python Click applications.

%prep
%autosetup -p1 -n click_man-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/click-man

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative click-man

%postun
%python_uninstall_alternative click-man

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/click-man
%{python_sitelib}/click_man
%{python_sitelib}/click_man-%{version}.dist-info

%changelog
