#
# spec file for package python-argparse-manpage
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-argparse-manpage
Version:        4.7
Release:        0
Summary:        Tool for automatic manual page building from a Python ArgumentParser object
License:        Apache-2.0
URL:            https://github.com/praiskup/argparse-manpage
Source:         https://github.com/praiskup/argparse-manpage/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  ca-certificates
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%if 0%{python_version_nodots} < 311
Requires:       python-tomli
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/argparse-manpage
%python_clone -a %{buildroot}%{_mandir}/man1/argparse-manpage.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Can't install examples in an isolated environment
%pytest -k 'not (test_old_example_file_name or TestAllExamples)'

%pre
%python_libalternatives_reset_alternative argparse-manpage

%post
%python_install_alternative argparse-manpage argparse-manpage.1

%postun
%python_uninstall_alternative argparse-manpage

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/argparse_manpage
%{python_sitelib}/build_manpages
%{python_sitelib}/argparse_manpage-%{version}.dist-info
%python_alternative %{_bindir}/argparse-manpage
%python_alternative %{_mandir}/man1/argparse-manpage.1%{?ext_man}

%changelog
