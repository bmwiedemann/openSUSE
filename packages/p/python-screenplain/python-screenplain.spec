#
# spec file for package python-screenplain
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-screenplain
Version:        0.11.1+git.1701424578.13b79f2
Release:        0
Summary:        Convert text file to viewable screenplay
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.screenplain.com/
# Source:         https://files.pythonhosted.org/packages/source/s/screenplain/screenplain-%%{version}.tar.gz
# Tarball generated from gh#vilcans/screenplain#62
Source:         screenplain-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_entry_point.patch mcepl@suse.com
# entry point lead to incorrect function.
Patch0:         fix_entry_point.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-reportlab
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Screenplain allows you to write a screenplay as a plain text
file using a format called Fountain. Text files are simple
and supported by all text manipulation software. It's not
just for hackers, too. The simplicity of plain text allows
you to easily view and edit them on devices such as tablets
and phones. No need for specific screenwriting software.

The magic that Screenplain performs is to take your plain
text file and convert it to a good looking screenplay in an
industry standard format. Send that file off to your producer,
agent, director or screenwriting competition. Currently, the
supported output formats are FDX and HTML. PDF will hopefully
be supported in a not too distant future.

%prep
%setup -q -n screenplain-%{version}
%autopatch -p1

sed -i '1{/^#!.*env python/d}' screenplain/main.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/screenplain
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v -p '*test*.py'
%python_exec -mdoctest -v screenplain/*.py

%post
%python_install_alternative screenplain

%postun
%python_uninstall_alternative screenplain

%files %{python_files}
%python_alternative %{_bindir}/screenplain
%{python_sitelib}/screenplain
%{python_sitelib}/screenplain-0.11.1*-info

%changelog
