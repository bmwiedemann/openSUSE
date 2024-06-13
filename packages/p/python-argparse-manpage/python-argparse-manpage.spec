#
# spec file for package python-argparse-manpage
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


%define mod_name argparse-manpage
Name:           python-argparse-manpage
Version:        4.6
Release:        0
Summary:        Tool for automatic manual page building from a Python ArgumentParser object
License:        Apache-2.0
URL:            https://github.com/praiskup/argparse-manpage
Source:         https://github.com/praiskup/argparse-manpage/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE Skip pip install tests until pip can behave better
Patch0:         skip-pip-install.patch
BuildArch:      noarch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-tomli
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
This utility generates a manual page in an automatic way from an
ArgumentParser object, so the manpage 1:1 corresponds to the
automatically generated --help output. The manpage generator needs to
known the location of the object, user can specify that by (a) the
module name or corresponding python filename and (b) the object name
or the function name which returns the object. There's a limited
support for (deprecated) optparse objects, too.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/argparse-manpage
%python_clone -a %{buildroot}%{_mandir}/man1/argparse-manpage.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%{python_install_alternative argparse-manpage argparse-manpage.1}

%postun
%python_uninstall_alternative argparse-manpage

%files %{python_files}
%doc README*
%license LICENSE
%{python_sitelib}/argparse_manpage
%{python_sitelib}/build_manpages
%{python_sitelib}/argparse_manpage-%{version}*info
%python_alternative %{_bindir}/argparse-manpage
%python_alternative %{_mandir}/man1/argparse-manpage.1%{?ext_man}

%changelog
