#
# spec file for package python-autoflake
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-autoflake
Version:        1.3
Release:        0
# for license file
%define tag     44b07bb9dab60a74cb5da0b67cc78b734763785c
Summary:        Program to removes unused Python imports and variables
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/myint/autoflake
Source:         https://files.pythonhosted.org/packages/source/a/autoflake/autoflake-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pyflakes >= 1.1.0}
%endif
Requires:       python-pyflakes >= 1.1.0
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
Autoflake removes unused imports and unused variables from Python
code. It makes use of pyflakes to do this.

By default, autoflake only removes unused imports for modules that
are part of the standard library. (Other modules may have side
effects that make them unsafe to remove automatically.) Removal of
unused variables is also disabled by default.

autoflake also removes useless pass statements.

%prep
%setup -q -n autoflake-%{version}

%build
%python_build

%install
%python_install

%{python_expand chmod a-x %{buildroot}%{$python_sitelib}/autoflake.py
%fdupes %{buildroot}%{$python_sitelib}
}

%python_clone -a %{buildroot}%{_bindir}/autoflake

%if %{with test}
%check
export $LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%post
%python_install_alternative autoflake

%postun
%python_uninstall_alternative autoflake

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/autoflake
%{python_sitelib}/*

%changelog
