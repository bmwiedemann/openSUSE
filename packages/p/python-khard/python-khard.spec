#
# spec file for package python-khard
#
# Copyright (c) 2022 SUSE LLC
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

# TODO:
# generate documentation

%define skip_python2 1
Name:           python-khard
Version:        0.18.0
Release:        0
Summary:        Console carddav client
License:        GPL-3.0-only
URL:            https://github.com/lucc/khard
Source0:        https://files.pythonhosted.org/packages/source/k/khard/khard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module Unidecode}
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module vobject}
# /SECTION
Requires:       python-Unidecode
Requires:       python-atomicwrites
Requires:       python-configobj
Requires:       python-ruamel.yaml
Requires:       python-vobject
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python3-vdirsyncer
%python_subpackages

%description
Khard is an address book for the Unix console.
It creates, reads, modifies and removes carddav address book entries at your local machine.
Khard is also compatible to the email clients mutt and alot and the SIP client twinkle.

%prep
%autosetup -p1 -n khard-%{version}

sed -i -e '1{/^#!\/usr\/bin\/env python/d}' khard/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/khard
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pyunittest discover -v

%post
%python_install_alternative khard

%postun
%python_uninstall_alternative khard

%files %{python_files}
%license LICENSE
%doc CHANGES README.md todo.txt
%doc doc/source/examples/khard.conf.example
%{python_sitelib}/khard
%{python_sitelib}/khard-%{version}*-info
%python_alternative %{_bindir}/khard

%changelog
