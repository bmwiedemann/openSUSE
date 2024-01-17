#
# spec file for package python-mailman3-fedmsg-plugin
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
%define skip_python2 1
Name:           python-mailman3-fedmsg-plugin
Version:        0.5
Release:        0
Summary:        Emit fedmsg messages from mailman3
License:        LGPL-2.0-only
URL:            https://github.com/fedora-infra/mailman3-fedmsg-plugin
Source:         https://files.pythonhosted.org/packages/source/m/mailman3-fedmsg-plugin/mailman3-fedmsg-plugin-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Emit fedmsg messages from mailman3.

%prep
%setup -q -n mailman3-fedmsg-plugin-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream testsuite

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
